from PySide6.QtCore import QObject, QUrl, qDebug, qCritical, QFileInfo, QThread, Signal

from src.graphics.engines import *
from src.graphics.vtkModels import *
from src.utils import *
import vtk


class RenderingHelper(QObject):
    """
    'Talk' with Graphical Render Engine through Command pattern
    """

    def __init__(self, engine: ProcessingEngine, fbo: Fbo):
        super().__init__()
        self.__engine = engine
        self.__fbo = fbo

    def render(self):
        def config(*args, **kwargs):
            self.__fbo.render()

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def restoreCamera(self, cameraOrientation: dict):
        def config(*args, **kwargs):
            rendererModel: RendererModel = self.__engine.getModel(ModelName.BASE)
            rendererModel.setCamera(cameraOrientation)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def storeCamera(self, cameraOrientation: dict):
        def config(*args, **kwargs):
            rendererModel: RendererModel = self.__engine.getModel(ModelName.BASE)
            rendererModel.storeCamera(cameraOrientation)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def addInteractorStyle(self):
        def config(*args, **kwargs):
            interactorStyleModel = InteractorStyleModel(ModelName.INTERACTOR_STYLE_TRACKBALL)
            self.__fbo.setInteractorStyle(interactorStyleModel.model)
            self.__fbo.initRWI()
            self.__engine.registerModel(interactorStyleModel)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def addRenderer(self):
        def config(*args, **kwargs):
            rendererModel = RendererModel(ModelName.BASE)
            rendererModel.config()

            self.__fbo.addRenderer(rendererModel.model)
            self.__engine.registerModel(rendererModel)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def updateCylinderVisibility(self, visible: bool):
        def config(*args, **kwargs):
            if visible:
                rendererModel: RendererModel = self.__engine.getModel(ModelName.BASE)
                cylinderModel: CylinderModel = self.__engine.getModel(ModelName.CYLINDER_A)
                if not cylinderModel:
                    cylinderModel = CylinderModel(ModelName.CYLINDER_A)
                    self.__engine.registerModel(cylinderModel)
                    rendererModel.addActor(cylinderModel.actor)
                    rendererModel.focusCamera()
                else:
                    rendererModel.addActor(cylinderModel.actor)
            else:
                if self.__engine.hasModel(ModelName.CYLINDER_A):
                    cylinderModel = self.__engine.getModel(ModelName.CYLINDER_A)
                    rendererModel: RendererModel = self.__engine.getModel(ModelName.BASE)
                    rendererModel.removeActor(cylinderModel.actor)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def updateRendererColor(self, color: tuple):
        def config(*args, **kwargs):
            rendererModel: RendererModel = self.__engine.getModel(ModelName.BASE)
            rendererModel.setBackgroundColor(color)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)

    def updateModelColor(self, color: tuple):
        def config(*args, **kwargs):
            model = self.__engine.getModel(ModelName.CYLINDER_A)
            if model:
                model.setColor(color)

        cmd = Cmd(callback=config)
        self.__fbo.addCommand(cmd)
