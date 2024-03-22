# Raspberry Pi Motion Detection System

## Overview

This project implements a motion detection system using a Raspberry Pi and various hardware components. It detects motion using a Passive Infrared (PIR) sensor and captures images and videos using the Raspberry Pi Camera module when motion is detected.

## Requirements

- Raspberry Pi (any model with GPIO pins)
- Passive Infrared (PIR) sensor
- LED
- Buzzer
- Raspberry Pi Camera module

## Installation

1. Ensure you have Python installed on your Raspberry Pi.
2. Install the required Python libraries using pip:

pip install requests picamera2

markdown
Copy code

## Usage

1. Connect the PIR sensor, LED, and buzzer to the appropriate GPIO pins on the Raspberry Pi.
2. Run the `motion_detection.py` script:

python motion_detection.py

vbnet
Copy code

3. The system will continuously monitor for motion using the PIR sensor.
4. When motion is detected:
- An API request is made to update a field on ThingSpeak, indicating motion detection.
- The LED and buzzer are turned on to provide visual and audible feedback.
- An image and a 10-second video clip are captured using the Raspberry Pi Camera module.
- The captured media files are saved in the current directory.

## Configuration

- Update the `URL` variable in the script with your ThingSpeak API URL for data logging.
- Adjust GPIO pin numbers according to your hardware setup if necessary.

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the re
