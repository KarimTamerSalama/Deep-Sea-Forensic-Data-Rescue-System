# Autonomous Deep-Sea Forensic & Exploration Data Rescue System

**Official Certifications & Licenses:**
* **OSHWA Certified:** `UID EG000005` — [View Official Certificate](https://certification.oshwa.org/eg000005.html)
* **Hardware License:** [CERN-OHL-S-2.0](https://ohwr.org)
* **Software & Documentation License:** [MIT License](https://opensource.org)


## Overview
An autonomous, self-ejecting deep-sea capsule designed to preserve critical scientific exploration records and forensic micro-SSD media under extreme abyssal pressure. The system encapsulates storage media within a Grade-5 Titanium alloy hull filled with non-conductive dielectric fluid, featuring an ESP32-controlled fail-safe solenoid latch, nitrogen-gas hydraulic ejection pistons, and underwater acoustic telemetry.

* **Official OSHWA Certification:** UID `EG000005` — [View Certificate](https://certification.oshwa.org/eg000005.html)
* **Author & Maintainer:** Karim Tamer Salama (Independent Researcher, Alexandria, Egypt)

---

## Repository Structure & Documentation
* **`ESP32_CODE.py`**: MicroPython firmware for the ESP32-WROOM-32 microcontroller, interfacing with the BMP280 pressure sensor via SPI and controlling the fail-safe solenoid valve.
* **`CapsuleCircuit.pdf`**: Complete electrical schematic designed in KiCad E.D.A.
* **`BOM.txt`**: Bill of Materials detailing all electronic, structural, and actuation components.
* **`Capsule.stl`**: Open 3D CAD model of the Grade-5 Titanium pressure hull (also viewable via [Public 3D Preview](https://www.tinkercad.com/things/dN6JhisA1Ix-titanium-capsule?sharecode=LrnVDv7l5KebKseZvE2AwixCXxzA2PnjqhyDs2wvqG0)).
* **`Deep_Sea_Rescue_System(1).pdf`**: Full technical research paper detailing system architecture, fluid pressure equalization, and acoustic recovery protocols.

---

## UN Sustainable Development Goals (SDG) Alignment
This project directly contributes to **UN SDG 14: Life Below Water**, specifically targeting:
* **Target 14.a**: *Increase scientific knowledge, develop research capacity, and transfer marine technology* by providing an affordable, open-source hardware standard to safeguard irreplaceable oceanographic, biological, and deep-sea expedition data from catastrophic loss.

---

## Data Extraction & Privacy Compliance
* **Open Data Formats**: Preserved micro-SSD media utilizes standard, non-proprietary file systems (`ext4`, `NTFS`, `GPT/MBR`) allowing researchers to extract raw bit-stream images using standard open-source tools (e.g., `dd`, `Autopsy`).
* **Privacy & No PII**: This system exclusively captures environmental sensor telemetry and scientific expedition records. It does not collect, store, or process any Personally Identifiable Information (PII).

---

## Safety Guidelines (Do No Harm)
* **High-Pressure & Pneumatic Hazard**: The ejection mechanism utilizes pressurized nitrogen-gas hydraulic pistons. Assembly and pressure testing must only be conducted by qualified personnel using certified hydrostatic test chambers and appropriate personal protective equipment (PPE).
* **Battery Safety**: Handle the LiPo battery pack (`7.4V / 12V`) in accordance with standard marine waterproofing and thermal protection protocols to prevent short circuits or over-discharge.

---

## Licensing
In full alignment with our **OSHWA Certification (`EG000005`)**, this project is licensed under open, standard-compliant licenses:
* **Hardware, Schematics, BOM & 3D CAD (`CapsuleCircuit.pdf`, `BOM.txt`, `Capsule.stl`)**: Licensed under the **CERN Open Hardware Licence Version 2 - Strongly Reciprocal (`CERN-OHL-S-2.0`)**.
* **Software (`ESP32_CODE.py`)**: Licensed under the **MIT License**.
* **Documentation & Research Paper (`README.md`, `Deep_Sea_Rescue_System(1).pdf`)**: Licensed under the **MIT License**.
