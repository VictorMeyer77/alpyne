from RPi import GPIO


class Move:

    def __init__(self, motor_one_pins, motor_two_pins):
        self.motor_one_pins = motor_one_pins
        self.motor_two_pins = motor_two_pins
        self._init_gpio_output()
        GPIO.PWM(motor_one_pins["Enable"], 100).start(100)
        GPIO.PWM(motor_two_pins["Enable"], 100).start(100)

    def _init_gpio_output(self):
        GPIO.setup(self.motor_one_pins["Enable"], GPIO.OUT)
        GPIO.setup(self.motor_one_pins["InputOne"], GPIO.OUT)
        GPIO.setup(self.motor_one_pins["InputTwo"], GPIO.OUT)
        GPIO.setup(self.motor_two_pins["Enable"], GPIO.OUT)
        GPIO.setup(self.motor_two_pins["InputOne"], GPIO.OUT)
        GPIO.setup(self.motor_two_pins["InputTwo"], GPIO.OUT)

    @staticmethod
    def motor_forward(motor_pins):
        GPIO.output(motor_pins["InputOne"], GPIO.HIGH)
        GPIO.output(motor_pins["InputTwo"], GPIO.LOW)

    @staticmethod
    def motor_backward(motor_pins):
        GPIO.output(motor_pins["InputOne"], GPIO.LOW)
        GPIO.output(motor_pins["InputTwo"], GPIO.HIGH)

    @staticmethod
    def motor_stop(motor_pins):
        GPIO.output(motor_pins["InputOne"], GPIO.LOW)
        GPIO.output(motor_pins["InputTwo"], GPIO.LOW)

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
