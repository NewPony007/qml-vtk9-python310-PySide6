import vtk
from PySide6.QtCore import QObject


class CylinderModel(QObject):
    def __init__(self, name: str):
        cylinderSource = vtk.vtkCylinderSource()
        cylinderSource.SetCenter(0.0, 0.0, 0.0)
        cylinderSource.SetRadius(5.0)
        cylinderSource.SetHeight(7.0)
        cylinderSource.SetResolution(100)
        cylinderSource.Update()
        self._polyData = cylinderSource.GetOutput()
        self._mapper = vtk.vtkPolyDataMapper()
        self._mapper.SetInputData(self._polyData)
        self._actor = vtk.vtkActor()
        self._actor.SetMapper(self._mapper)
        self.name = name

    @property
    def model(self):
        return self._polyData

    @property
    def mapper(self):
        return self._mapper

    @property
    def actor(self):
        return self._actor
