import RPi.GPIO as GPIO
import time


def ultrasonic_loop(ultrasonic_pins, queue):
    while True:
        tmp = ultrasonic_distance(ultrasonic_pins)
        queue.put(tmp)


def ultrasonic_distance(ultrasonic_pins):
    GPIO.output(int(ultrasonic_pins["Trigger"]), True)
    time.sleep(0.00001)
    GPIO.output(int(ultrasonic_pins["Trigger"]), False)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(int(ultrasonic_pins["Echo"])) == 0:
        start_time = time.time()
    while GPIO.input(int(ultrasonic_pins["Echo"])) == 1:
        stop_time = time.time()
    return (stop_time - start_time) * 34300.0 / 2.0
