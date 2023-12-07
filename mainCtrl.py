from pathlib import Path

import vtk
from PySide6.QtCore import QObject, QUrl, Signal
from PySide6.QtQml import QQmlApplicationEngine

import random

from cylinderModel import CylinderModel
from fbo import Fbo
from funcs import getQmlObject


class MainCtrl(QObject):
    sigPosXChanged = Signal(float)
    sigPosYChanged = Signal(float)

    def __init__(self, engine: QQmlApplicationEngine):
        super().__init__()
        self.cylinderVisible = True
        self.__engine = engine

        self.__posX = 0.0
        self.__posY = 0.0

        ctxt = self.__engine.rootContext()
        ctxt.setContextProperty("MainCtrl", self)


        main_qml = Path(__file__).resolve().parent / "main.qml"
        self.__engine.load(QUrl.fromLocalFile(main_qml))

        self.__fbo: Fbo = getQmlObject(self.__engine, "fbo")
        self.__fbo.createRenderer()

    def setup(self):
        cylinderSource = vtk.vtkCylinderSource()
        cylinderSource.SetCenter(0.0, 0.0, 0.0)
        cylinderSource.SetRadius(5.0)
        cylinderSource.SetHeight(7.0)
        cylinderSource.SetResolution(100)
        cylinderSource.Update()
        self.polyData = cylinderSource.GetOutput()
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputData(self.polyData)
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

        self.renderer = vtk.vtkRenderer()
        self.renderer.AddActor(self.actor)
        self.renderer.SetBackground(0, 0, 0)
        self.renderer.GradientBackgroundOn()
        self.renderer.ResetCameraClippingRange()
        self.renderer.ResetCamera()

        self.__fbo.addRenderer(self.renderer)
        self.__fbo.setInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.__fbo.initRWI()
        self.__fbo.render()

