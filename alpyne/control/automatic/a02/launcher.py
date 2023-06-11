import time
from move import Move
from control.automatic.a02.controller import Controller
from control.sensor.camera import Camera
from control.sensor.brain import Brain


def launch(config):
    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    camera = Camera()
    brain = Brain("input/model/model.tflite")
    controller = Controller(move, camera, brain)

    while True:
        try:
            controller.run()
            time.sleep(1)
        except KeyboardInterrupt:
            break
