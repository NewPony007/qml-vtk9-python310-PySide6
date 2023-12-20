import vtk
from PySide6.QtCore import QObject, Signal
from src.utils import SingletonQObjectMeta


class BusinessModel(QObject, metaclass=SingletonQObjectMeta):
    """
    Cache business data
    """

    sigVisualCylinderChanged = Signal(bool)
    sigRendererColorChanged = Signal(tuple)
    sigPolyDataColorChanged = Signal(tuple)

    def __init__(self):
        super().__init__()

        self.__visualCylinder = False
        self.__cameraPosition = dict()
        self.__rendererColor = [50/255, 168/255, 82/255]
        self.__polyDataColor = [10/255, 100/255, 180/255]

    def getVisualCylinder(self) -> bool:
        return self.__visualCylinder

    def setVisualCylinder(self, val: bool):
        if self.__visualCylinder != val:
            self.__visualCylinder = val
            self.sigVisualCylinderChanged.emit(val)

    def getRendererColor(self) -> bool:
        return self.__rendererColor

    def setRendererColor(self, val: bool):
        if self.__rendererColor != val:
            self.__rendererColor = val
            self.sigRendererColorChanged.emit(val)

    def getPolyDataColor(self) -> bool:
        return self.__polyDataColor

    def getCameraPosition(self):
        return self.__cameraPosition

