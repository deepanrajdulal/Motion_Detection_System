import time
import requests
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview  # Correct import
from picamera2.encoders import H264Encoder


GPIO.setmode(GPIO.BCM)

pir_pin = 15
led_pin = 18
buzzer_pin = 23
picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)
picam.start()




GPIO.setup(pir_pin, GPIO.IN)  # PIR sensor is an input
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(pir_pin):
            print("Motion detected")
            URL = "https://api.thingspeak.com/update?api_key=HWGLTCE0X3OKP8HU&field5=1"
            r = requests.get(URL)
            print(r)
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn on the buzzer
            
            
            picam.capture_file(f"img.jpg")
            picam.stop()
            print("Picture captured")
            video_config = picam.create_video_configuration()
            picam.configure(video_config)
            encoder = H264Encoder(10000000)
            picam.start_recording(encoder, 'test.h264')
            time.sleep(10)
            picam.stop_recording()
            print("Video captured")
            break
            time.sleep(5)  # Wait for 5 seconds
        else:
            data = 0
            URL = "https://api.thingspeak.com/update?api_key=HWGLTCE0X3OKP8HU&field5="+str(data)
            r = requests.get(URL)
            print(r)
            GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer
            print("Motion not detected")
            time.sleep(3)  # Wait for 3 seconds
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit
    
    print("Program ended")
    
