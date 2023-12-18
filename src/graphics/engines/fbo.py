from typing import List, Optional

from PySide6.QtCore import (
    QEvent,
    QPoint,
    QPointF,
    Qt,
    Slot,
)
from PySide6.QtGui import QMouseEvent, QWheelEvent, QOpenGLContext
from PySide6.QtQuick import QQuickFramebufferObject, QQuickItem

import vtk
from src.graphics import engines
from src.utils import *


class Fbo(QQuickFramebufferObject):
    def __init__(self):
        super().__init__()
        print("Fbo::init")
        self.__fboRenderer: engines.FboRenderer = None

        self.lastMouseButtonEvent: QMouseEvent = None
        self.lastMouseMoveEvent: QMouseEvent = None
        self.lastWheelEvent: QWheelEvent = None

        self.setAcceptedMouseButtons(Qt.AllButtons)
        self.setMirrorVertically(True)

        self.setAcceptHoverEvents(True)
        self.setAcceptTouchEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.AllButtons)

        self.setFlag(QQuickItem.Flag.ItemIsFocusScope)
        self.setFlag(QQuickItem.Flag.ItemHasContents)

    def render(self):
        print("Fbo::render")
        self.window().beginExternalCommands()

        # self.__fboRenderer.rw.SetReadyForRendering(True)
        # self.__fboRenderer.rw.SetIsCurrent(True)

        ostate = self.__fboRenderer.rw.GetState()
        ostate.Reset()
        ostate.Push()
        # ostate.vtkglDepthFunc()
        self.__fboRenderer.rw.SetReadyForRendering(True)
        self.__fboRenderer.rw.SetIsCurrent(True)
        self.__fboRenderer.rwi.ProcessEvents()
        self.__fboRenderer.rwi.Render()

        self.__fboRenderer.rw.SetReadyForRendering(False)
        ostate.Pop()

        # self.__fboRenderer.rwi.Render()

        self.window().endExternalCommands()

    def addRenderer(self, renderer: vtk.vtkRenderer):
        self.__fboRenderer.rw.AddRenderer(renderer)

    def setInteractorStyle(self, interactorStyle: vtk.vtkInteractorStyle):
        self.__fboRenderer.rwi.SetInteractorStyle(interactorStyle)

    def initRWI(self):
        self.__fboRenderer.rwi.Initialize()
        self.__fboRenderer.rwi.Start()

    def createRenderer(self) -> QQuickFramebufferObject.Renderer:
        if not self.__fboRenderer:
            self.__fboRenderer = engines.FboRenderer()
        return self.__fboRenderer

    def addCommand(self, command: "commands.Command"):
        with self.__fboRenderer.commandQueueLock:
            self.__fboRenderer.commandQueue.put(command)
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        self.__processMouseButtonEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.__processMouseButtonEvent(event)

    def __processMouseButtonEvent(self, event: QMouseEvent):
        self.lastMouseButtonEvent = cloneMouseEvent(event)
        self.lastMouseButtonEvent.ignore()
        event.accept()
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        self.lastMouseMoveEvent = cloneMouseEvent(event)
        self.lastMouseMoveEvent.ignore()
        event.accept()
        self.update()

    def wheelEvent(self, event: QWheelEvent):
        self.lastWheelEvent = cloneWheelEvent(event)
        self.lastWheelEvent.ignore()
        event.accept()
        self.update()

    @Slot()
    def onCompleted(self):
        print("Fbo::onCompleted")

    @Slot(float, float, int, int, int)
    def onMousePressed(
        self, x: float, y: float, button: int, buttons: int, modifiers: int
    ):
        self.lastMouseButtonEvent = convertToMouseEvent(
            QEvent.MouseButtonPress,
            QPointF(x, y),
            Qt.MouseButton(button),
            Qt.MouseButtons(buttons),
            Qt.KeyboardModifiers(modifiers),
        )
        self.lastMouseButtonEvent.ignore()
        self.update()

    @Slot(float, float, int, int, int)
    def onMouseReleased(
        self, x: float, y: float, button: int, buttons: int, modifiers: int
    ):
        self.lastMouseButtonEvent = convertToMouseEvent(
            QEvent.MouseButtonRelease,
            QPointF(x, y),
            Qt.MouseButton(button),
            Qt.MouseButtons(buttons),
            Qt.KeyboardModifiers(modifiers),
        )
        self.lastMouseButtonEvent.ignore()
        self.update()

    @Slot(float, float, int, int, int)
    def onMouseMove(
        self, x: float, y: float, button: int, buttons: int, modifiers: int
    ):
        self.lastMouseMoveEvent = convertToMouseEvent(
            QEvent.MouseMove,
            QPointF(x, y),
            Qt.MouseButton(button),
            Qt.MouseButtons(buttons),
            Qt.KeyboardModifiers(modifiers),
        )
        self.lastMouseMoveEvent.ignore()
        self.update()

    @Slot(QPoint, int, int, int, QPoint, float, float)
    def onMouseWheel(
        self,
        angleDelta: QPoint,
        buttons: int,
        inverted: int,
        modifiers: int,
        pixelDelta: QPoint,
        x: float,
        y: float,
    ):
        self.lastWheelEvent = QWheelEvent(
            QPointF(x, y),
            QPointF(x, y),
            pixelDelta,
            angleDelta,
            Qt.MouseButtons(buttons),
            Qt.KeyboardModifiers(modifiers),
            Qt.NoScrollPhase,
            bool(inverted),
        )
        self.lastWheelEvent.ignore()
        self.update()
