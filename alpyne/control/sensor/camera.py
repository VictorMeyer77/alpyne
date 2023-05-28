from datetime import datetime
from picamera import PiCamera
import os


class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (64, 64)
        self.camera.start_preview()
        self.output_path = "output/media/camera/"

    def capture(self, subdir):
        self.camera.capture(os.path.join(self.output_path, subdir, "{}.jpg".format(datetime.now())))
