import RPi.GPIO as GPIO


class Move:

    def __init__(self, motor_one_pins, motor_two_pins):
        self.motor_one_pins = motor_one_pins
        self.motor_two_pins = motor_two_pins
        self._init_gpio_output()
        self.pwm_one, self.pwm_two = self._create_pwm()
        self.stop()

    def _init_gpio_output(self):
        GPIO.setup(int(self.motor_one_pins["Enable"]), GPIO.OUT)
        GPIO.setup(int(self.motor_one_pins["InputOne"]), GPIO.OUT)
        GPIO.setup(int(self.motor_one_pins["InputTwo"]), GPIO.OUT)
        GPIO.setup(int(self.motor_two_pins["Enable"]), GPIO.OUT)
        GPIO.setup(int(self.motor_two_pins["InputOne"]), GPIO.OUT)
        GPIO.setup(int(self.motor_two_pins["InputTwo"]), GPIO.OUT)

    def _create_pwm(self):
        pwm_one = GPIO.PWM(int(self.motor_one_pins["Enable"]), 100)
        pwm_two = GPIO.PWM(int(self.motor_two_pins["Enable"]), 100)
        pwm_one.start(100)
        pwm_two.start(100)
        return pwm_one, pwm_two

    @staticmethod
    def motor_forward(motor_pins):
        GPIO.output(int(motor_pins["InputOne"]), GPIO.HIGH)
        GPIO.output(int(motor_pins["InputTwo"]), GPIO.LOW)

    @staticmethod
    def motor_backward(motor_pins):
        GPIO.output(int(motor_pins["InputOne"]), GPIO.LOW)
        GPIO.output(int(motor_pins["InputTwo"]), GPIO.HIGH)

    @staticmethod
    def motor_stop(motor_pins):
        GPIO.output(int(motor_pins["InputOne"]), GPIO.LOW)
        GPIO.output(int(motor_pins["InputTwo"]), GPIO.LOW)

    def forward(self):
        self.motor_forward(self.motor_one_pins)
        self.motor_forward(self.motor_two_pins)

    def backward(self):
        self.motor_backward(self.motor_one_pins)
        self.motor_backward(self.motor_two_pins)

    def right(self):
        self.motor_stop(self.motor_two_pins)
        self.motor_forward(self.motor_one_pins)

    def left(self):
        self.motor_stop(self.motor_one_pins)
        self.motor_forward(self.motor_two_pins)

    def stop(self):
        self.motor_stop(self.motor_one_pins)
        self.motor_stop(self.motor_two_pins)
