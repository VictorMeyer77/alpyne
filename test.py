# Import required modules
import time
import RPi.GPIO as GPIO

enable = 12
ain_one = 38
ain_two = 36

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(enable, GPIO.OUT) # Connected to PWMA
GPIO.setup(ain_two, GPIO.OUT) # Connected to AIN2
GPIO.setup(ain_one, GPIO.OUT) # Connected to AIN1

# Drive the motor clockwise
GPIO.output(ain_one, GPIO.HIGH) # Set AIN1
GPIO.output(ain_two, GPIO.LOW) # Set AIN2

# Set the motor speed
GPIO.output(enable, GPIO.HIGH) # Set PWMA


# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
GPIO.output(ain_one, GPIO.LOW) # Set AIN1
GPIO.output(ain_two, GPIO.HIGH) # Set AIN2

# Set the motor speed
GPIO.output(enable, GPIO.HIGH) # Set PWMA



# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(ain_one, GPIO.LOW) # Set AIN1
GPIO.output(ain_two, GPIO.LOW) # Set AIN2
GPIO.output(enable, GPIO.LOW) # Set PWMA