import RPi.GPIO as GPIO
import time


class Ultrasonic:

    def __init__(self, ultrasonic_pins):

        self.ultrasonic_pins = ultrasonic_pins
        GPIO.setup(int(self.ultrasonic_pins["Trigger"]), GPIO.OUT)
        GPIO.setup(int(self.ultrasonic_pins["Echo"]), GPIO.IN)

    def get_distance(self):
        GPIO.output(int(self.ultrasonic_pins["Trigger"]), True)
        time.sleep(0.00001)
        GPIO.output(int(self.ultrasonic_pins["Trigger"]), False)
        start_time = time.time()
        stop_time = time.time()
        while GPIO.input(int(self.ultrasonic_pins["Echo"])) == 0:
            start_time = time.time()
        while GPIO.input(int(self.ultrasonic_pins["Echo"])) == 1:
            stop_time = time.time()
        return (stop_time - start_time) * 34300.0 / 2.0
