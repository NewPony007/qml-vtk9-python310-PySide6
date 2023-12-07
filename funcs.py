import os
import traceback

from PySide6.QtCore import QEvent, QObject, QPointF, Qt
from PySide6.QtGui import QMouseEvent, QWheelEvent, QSurfaceFormat


def cloneMouseEvent(event: QMouseEvent):
    return QMouseEvent(
        event.type(),
        event.localPos(),
        event.windowPos(),
        event.screenPos(),
        event.button(),
        event.buttons(),
        event.modifiers(),
        event.source(),
    )


def cloneWheelEvent(event: QWheelEvent):
    return QWheelEvent(
        event.position(),
        event.globalPosition(),
        event.pixelDelta(),
        event.angleDelta(),
        event.buttons(),
        event.modifiers(),
        event.phase(),
        event.inverted(),
        event.source(),
    )


def convertToMouseEvent(
    eventType: QEvent.Type,
    localPos: QPointF,
    button: Qt.MouseButton,
    buttons: Qt.MouseButtons,
    modifiers: Qt.KeyboardModifiers,
):
    return QMouseEvent(eventType, localPos, button, buttons, modifiers)


def getQmlObject(qmlEngine, objectName, parentObj=None):
    referenceBuffer = []
    if parentObj is None:
        for root_object in qmlEngine.rootObjects():
            if root_object.property("objectName") == objectName:
                return root_object
            obj = root_object.findChild(QObject, objectName)
            if obj is not None:
                referenceBuffer.append(obj)
                return obj
    else:
        obj = parentObj.findChild(QObject, objectName)
        if obj is not None:
            referenceBuffer.append(obj)
            return obj
    return None


def setDefaultSurfaceFormat(stereoCapable):
    """ Ported from: https://github.com/Kitware/VTK/blob/master/GUISupport/Qt/QVTKRenderWindowAdapter.cxx
    """
    fmt = QSurfaceFormat()
    fmt.setRenderableType(QSurfaceFormat.OpenGL)
    fmt.setVersion(3, 2)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setSwapBehavior(QSurfaceFormat.DoubleBuffer)
    fmt.setRedBufferSize(8)
    fmt.setGreenBufferSize(8)
    fmt.setBlueBufferSize(8)
    fmt.setDepthBufferSize(8)
    fmt.setAlphaBufferSize(8)
    fmt.setStencilBufferSize(0)
    fmt.setStereo(stereoCapable)
    fmt.setSamples(0)

    return fmt


def exceptHook(errType, errMsg, errTraceback):
    error = dict()
    error["type"] = errType.__name__
    error["message"] = str(errMsg)
    try:
        error["file"] = os.path.split(errTraceback.tb_frame.f_code.co_filename)[1]
        error["line"] = errTraceback.tb_lineno
        error["traceback"] = "".join(traceback.format_tb(errTraceback))
    except AttributeError:
        pass
    print("ERROR:")
    for k, v in error.items():
        if k == "traceback":
            print("{}:\n{}".format(k.title(), v))
        else:
            print("{}: {}".format(k.title(), v))