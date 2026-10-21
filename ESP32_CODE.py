from machine import Pin, ADC
import time

# 1. Component Initialization
solenoid_pin = Pin(15, Pin.OUT)       # Solenoid latch control pin
pressure_sensor = ADC(Pin(34))        # Pressure sensor connected to ADC pin
pressure_sensor.atten(ADC.ATTN_11DB)  # Set full-range voltage reading

# 2. Safe pressure threshold (representing standard operating pressure like 1 bar)
safe_pressure_limit = 1000  

while True:
    # Read the current pressure from the sensor
    current_pressure = pressure_sensor.read()
    print("Current Pressure Reading:", current_pressure)
    
    # 3. Core condition: If the pressure exceeds the safe limit, release the latch immediately
    if current_pressure > safe_pressure_limit:
        solenoid_pin.value(1) # Trigger the mechanism / open the latch
    else:
        solenoid_pin.value(0) # Keep the latch locked under normal pressure
        
    # Short delay between readings to stabilize the system
    time.sleep(1)