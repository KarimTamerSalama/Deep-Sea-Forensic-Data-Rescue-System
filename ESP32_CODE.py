from machine import Pin, SPI
import time
import struct

# 1. Initialize SPI and GPIO pins matching the KiCad schematic
spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(16), miso=Pin(17))
cs = Pin(18, Pin.OUT, value=1)
solenoid_pin = Pin(1, Pin.OUT, value=0)

# 2. Helper functions for BMP280 SPI communication
def bmp280_write(reg, val):
    cs.value(0)
    spi.write(bytearray([reg & 0x7F, val]))
    cs.value(1)

def bmp280_read(reg, length):
    cs.value(0)
    spi.write(bytearray([reg | 0x80]))
    data = spi.read(length)
    cs.value(1)
    return data

# Wake up sensor in normal measurement mode and read calibration coefficients
bmp280_write(0xF4, 0x27)
calib = bmp280_read(0x88, 24)
dig_T1, dig_T2, dig_T3, dig_P1, dig_P2, dig_P3, dig_P4, dig_P5, dig_P6, dig_P7, dig_P8, dig_P9 = struct.unpack('<HhhHhhhhhhhh', calib)

# 3. Convert raw sensor bytes to calibrated pressure in hPa (Bosch standard formula)
def read_pressure_hpa():
    data = bmp280_read(0xF7, 6)
    adc_p = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
    adc_t = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)

    var1 = (((adc_t >> 3) - (dig_T1 << 1)) * dig_T2) >> 11
    var2 = (((((adc_t >> 4) - dig_T1) * ((adc_t >> 4) - dig_T1)) >> 12) * dig_T3) >> 14
    t_fine = var1 + var2

    var1 = (t_fine >> 1) - 64000
    var2 = (((var1 >> 2) * (var1 >> 2)) >> 11) * dig_P6
    var2 = var2 + ((var1 * dig_P5) << 1)
    var2 = (var2 >> 2) + (dig_P4 << 16)
    var1 = (((dig_P3 * (((var1 >> 2) * (var1 >> 2)) >> 13)) >> 3) + ((dig_P2 * var1) >> 1)) >> 18
    var1 = ((32768 + var1) * dig_P1) >> 15
    if var1 == 0:
        return 0
    p = (((1048576 - adc_p) - (var2 >> 12)) * 3125)
    if p < 0x80000000:
        p = (p << 1) // var1
    else:
        p = (p // var1) * 2
    var1 = (dig_P9 * (((p >> 3) * (p >> 3)) >> 13)) >> 12
    var2 = ((p >> 2) * dig_P8) >> 13
    pressure_pa = p + ((var1 + var2 + dig_P7) >> 4)
    
    return pressure_pa / 100.0

# Submersible Cabin Pressure Monitoring (Normal human cabin = 1 atm / ~1013.25 hPa).
# In case of hull breach at abyssal depths (4,000m - 11,000m), cabin pressure spikes above 1 bar.
# Threshold set to 1050.0 hPa (~1.05 bar) to trigger the Nitrogen hydraulic ejection piston immediately.
SAFE_PRESSURE_LIMIT_HPA = 1050.0

while True:
    current_pressure = read_pressure_hpa()
    print("Current Pressure (hPa):", round(current_pressure, 2))
    
    # Release the solenoid latch immediately if pressure exceeds the safe limit
    if current_pressure > SAFE_PRESSURE_LIMIT_HPA:
        solenoid_pin.value(1)  # Trigger deployment mechanism / open latch
    else:
        solenoid_pin.value(0)  # Keep latch locked under normal pressure
        
    time.sleep(1)
