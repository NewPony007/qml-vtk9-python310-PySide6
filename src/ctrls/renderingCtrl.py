import logging
import os.path
from pathlib import Path

from PySide6.QtCore import QObject, QUrl, Signal, Property, Slot
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType, QQmlEngine
from PySide6.QtWidgets import QApplication

from src.ctrls import RenderingHelper
from src.models import BusinessModel
from src.graphics.engines import Fbo, ProcessingEngine
from src.utils import getQmlObject

import random


class RenderingCtrl(QObject):
    sigPosXChanged = Signal(float)
    sigPosYChanged = Signal(float)

    def __init__(self, engine: QQmlApplicationEngine):
        super().__init__()
        print("RenderingCtrl::init")
        self.__engine = engine
        self.__procEngine = ProcessingEngine()

        self.__posX = 0.0
        self.__posY = 0.0

        self.__fbo = None
        self.__hp = None
        self.__businessModel = BusinessModel()

        ctxt = self.__engine.rootContext()
        ctxt.setContextProperty("RenderingCtrl", self)

    def createRenderer(self):
        print("RenderingCtrl::createRenderer")
        # if self.__fbo is None:
        self.__fbo = getQmlObject(self.__engine, "fbo")
        self.__fbo.createRenderer()
        self.__hp = RenderingHelper(self.__procEngine, self.__fbo)


    def setup(self):
        print("RenderingCtrl::setup")
        self.__hp.addInteractorStyle()
        self.__hp.addRenderer()
        self.__hp.updateRendererColor(self.__businessModel.getRendererColor())
        self.__hp.render()

        self.connectSignals()

    def connectSignals(self):
        print("RenderingCtrl::connectSignals")
        self.sigPosXChanged.connect(self.__changeRendererColorInBusinessModel)
        self.sigPosYChanged.connect(self.__changeRendererColorInBusinessModel)

        self.__businessModel.sigVisualCylinderChanged.connect(
            self.__updateCylinderVisibility
        )
        self.__businessModel.sigRendererColorChanged.connect(self.__updateRendererColor)

        self.__businessModel.sigVisualCylinderChanged.emit(self.__businessModel.getVisualCylinder())


    def disconnectSignals(self):
        print("RenderingCtrl::disconnectSignals")
        self.disconnect(self)
        self.__businessModel.disconnect(self)

    def getPosX(self):
        return self.__posX

    def setPosX(self, val: float):
        if self.__posX != val:
            self.__posX = val
            self.sigPosXChanged.emit(val)

    posX = Property(float, fget=getPosX, fset=setPosX, notify=sigPosXChanged)

    def getPosY(self):
        return self.__posY

    def setPosY(self, val: float):
        if self.__posY != val:
            self.__posY = val
            self.sigPosYChanged.emit(val)

    posY = Property(float, fget=getPosY, fset=setPosY, notify=sigPosYChanged)

    @Slot()
    def contentLoaded(self):
        print("RenderingCtrl::contentLoaded")
        # if self.__fbo is None:
        self.createRenderer()
        self.setup()

    @Slot()
    def onStackViewActivated(self):
        print("RenderingCtrl::onStackViewActivated")
        # if self.__fbo is None:
        # self.createRenderer()
        # self.setup()

    @Slot()
    def onStackViewDeactivated(self):
        print("RenderingCtrl::onStackViewDeactivated")
        self.disconnectSignals()

    @Slot(int, float, float)
    def showPos(self, buttons: int, x: float, y: float):
        self.posX = x
        self.posY = y

    @Slot()
    def toggleCylinder(self):
        print("RenderingCtrl::toggleCylinder")
        newVal = not self.__businessModel.getVisualCylinder()
        self.__businessModel.setVisualCylinder(newVal)

    def __updateCylinderVisibility(self, val: bool):
        self.__hp.updateCylinderVisibility(val)
        if val:
            self.__hp.updateModelColor(self.__businessModel.getPolyDataColor())
        self.__hp.focusCamera()
        self.__hp.render()

    def __updateRendererColor(self, color: tuple):
        self.__hp.updateRendererColor(color)
        self.__hp.render()

    def __changeRendererColorInBusinessModel(self):
        temp = (self.posX + self.posY) / 2
        newVal = (self.posX, self.posY, temp)
        summ = sum(newVal)
        if summ != 0:
            summ = 1
        color = [i / (sum(newVal)) for i in newVal]
        self.__businessModel.setRendererColor(color)


