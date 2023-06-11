import tflite_runtime.interpreter as tflite
import numpy as np


class Brain:

    def __init__(self, model_path):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def predict(self, input_array):
        self.interpreter.set_tensor(self.input_details[0]["index"], input_array)
        self.interpreter.invoke()
        return self.interpreter.get_tensor(self.output_details[0]["index"]).argmax()
