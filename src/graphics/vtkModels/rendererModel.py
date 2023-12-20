from src.graphics.vtkModels import VtkModel

import vtk


class RendererModel(VtkModel):
    @property
    def model(self):
        return self.__renderer

    def __init__(self, name: str):
        super().__init__(name)
        self.__renderer = vtk.vtkRenderer()

    def config(self):
        self.__renderer.SetBackground(0, 0, 0)
        self.__renderer.GradientBackgroundOn()
        self.__renderer.ResetCameraClippingRange()
        self.__renderer.ResetCamera()

    def focusCamera(self):
        camera = self.__renderer.GetActiveCamera()
        camera.SetFocalPoint(0, 0, 0)
        camera.SetViewUp(0, 0, 1)
        camera.SetPosition(0, -1, 0)
        self.__renderer.ResetCameraClippingRange()
        self.__renderer.ResetCamera()

    def setCamera(self, cameraOrientation: dict):
        camera = self.__renderer.GetActiveCamera()
        try:
            camera.SetPosition(cameraOrientation['position'])
            camera.SetFocalPoint(cameraOrientation['focal point'])
            camera.SetViewUp(cameraOrientation['view up'])
            camera.SetDistance(cameraOrientation['distance'])
            camera.SetClippingRange(cameraOrientation['clipping range'])
        except KeyError:
            camera.SetFocalPoint(0, 0, 0)
            camera.SetViewUp(0, 0, 1)
            camera.SetPosition(0, -1, 0)
            self.__renderer.ResetCameraClippingRange()
            self.__renderer.ResetCamera()

    def storeCamera(self, cameraOrientation: dict):
        camera = self.__renderer.GetActiveCamera()
        cameraOrientation['position'] = camera.GetPosition()
        cameraOrientation['focal point'] = camera.GetFocalPoint()
        cameraOrientation['view up'] = camera.GetViewUp()
        cameraOrientation['distance'] = camera.GetDistance()
        cameraOrientation['clipping range'] = camera.GetClippingRange()
        cameraOrientation['orientation'] = camera.GetOrientation()

    def addActor(self, actor: vtk.vtkActor):
        self.__renderer.AddActor(actor)

    def removeActor(self, actor: vtk.vtkActor):
        self.__renderer.RemoveActor(actor)

    def setBackgroundColor(self, color: tuple):
        self.__renderer.SetBackground(color)
