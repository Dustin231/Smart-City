# import the necessary packages
import time
import sys, os
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 18
# GPIO18
pin_button = 18
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# allow the camera to warmup
time.sleep(0.5)
i=0
while True:
    input_state = GPIO.input(pin_button)
    if input_state == False:
	print('button pressed')
        os.system("fswebcam -r 1280X720 -S 15 image_" + str(i) +".jpg")
        time.sleep(0.3)
        i += 1