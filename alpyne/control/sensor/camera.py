import time
from picamera import PiCamera
import os


class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (64, 64)
        self.camera.color_effects = (128, 128)
        self.camera.start_preview()
        self.output_path = "output/media/image/"

    def capture(self, subdir):
        self.camera.capture(os.path.join(self.output_path, subdir, "{}.jpg".format(round(time.time()*1000))))
