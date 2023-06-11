import time
from picamera import PiCamera
import picamera.array
import os

class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (64, 64)
        self.camera.start_preview()
        self.output_path = "output/media/image/"

    def capture(self, subdir):
        self.camera.capture(os.path.join(self.output_path, subdir, "{}.jpg".format(round(time.time()*1000))))

    def test(self):
        with picamera.array.PiRGBArray(self.camera) as stream:
            self.camera.capture(stream, "rgb")
            print(stream.array.shape)
            print(stream.array)

c = Camera()

for i in range(10):
    c.test()
    time.sleep(1)