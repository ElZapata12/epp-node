from abc import abstractmethod, ABC
from ultralytics import YOLO


class IAModel(ABC):

    def __init__(self, model):
        self._model = model

    @abstractmethod
    def scan_frame(self):
        pass


class YoloEPPDetector(IAModel):


    def scan_frame(self):
        pass
