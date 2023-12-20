import logging
import os
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QTimer, Signal, QUrl
from PySide6.QtGui import QSurfaceFormat, QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtWidgets import QApplication
import vtk

from src.ctrls import RenderingCtrl
from src.ctrls.page1Ctrl import Page1Ctrl
from src.ctrls.page2Ctrl import Page2Ctrl
from src.graphics.engines import Fbo
from src.utils import *

logging.basicConfig(filename="log.ini", level=logging.DEBUG)


def setVtkLog():
    logPath = os.path.join("log.ini")
    fow = vtk.vtkFileOutputWindow()
    fow.SetFileName(logPath)
    ow = vtk.vtkOutputWindow()
    ow.SetInstance(fow)


def registerCustomQml():
    qmlRegisterType(Fbo, "QmlVtk", 1, 0, "Fbo")


def compileQml():
    from src.utils import compileResourceFiles

    compileResourceFiles(rcDir="src/views", outDir="src/views")
    if os.path.isfile(os.path.join("src/views/rc_qml.py")):
        from src.views.rc_qml import qInitResources

        qInitResources()


class App(QApplication):
    def __init__(self, sys_argv):
        if sys.platform == "win32":
            sys_argv += ["-style", "material"]  #! MUST HAVE
        elif sys.platform == "linux":
            sys_argv += ["-style", "Fusion"]  # ! MUST HAVE
        super(App, self).__init__(sys_argv)
        self.engine = QQmlApplicationEngine()
        self.__page1 = Page1Ctrl(self.engine)
        self.__page2 = Page2Ctrl(self.engine)
        self.__rendering = RenderingCtrl(self.engine)
        self.engine.load(QUrl.fromLocalFile(f":/App.qml"))


def main():
    registerCustomQml()
    compileQml()
    QSurfaceFormat.setDefaultFormat(setDefaultSurfaceFormat(False))

    app = App(sys.argv)

    if len(app.engine.rootObjects()) == 0:
        print("No QML file is loaded!")
        return

    #! Make sure MainView is active --> FboRenderer is created
    # QTimer.singleShot(0, app.setup)
    sys.exit(app.exec())


if __name__ == "__main__":
    setVtkLog()

    sys.excepthook = exceptHook

    main()
