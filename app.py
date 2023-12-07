import logging
import os
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QTimer, Signal, QUrl
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtWidgets import QApplication
import vtk

from fbo import Fbo
from funcs import getQmlObject, setDefaultSurfaceFormat, exceptHook
from mainCtrl import MainCtrl

logging.basicConfig(filename="log.ini", level=logging.DEBUG)


def setVtkLog():
    logPath = os.path.join("log.ini")
    fow = vtk.vtkFileOutputWindow()
    fow.SetFileName(logPath)
    ow = vtk.vtkOutputWindow()
    ow.SetInstance(fow)


class App(QApplication):
    def __init__(self, sys_argv):
        if sys.platform == "win32":
            sys_argv += ["-style", "material"]  #! MUST HAVE
        elif sys.platform == "linux":
            sys_argv += ["-style", "Fusion"]  # ! MUST HAVE
        super(App, self).__init__(sys_argv)

        self.engine = QQmlApplicationEngine()

        self.__mainCtrl = MainCtrl(self.engine)

    def setup(self):
        mainView = getQmlObject(self.engine, "MainView")
        if mainView.property("active"):
            self.__mainCtrl.setup()
        else:
            QTimer.singleShot(0, self.setup)


def main():
    qmlRegisterType(Fbo, "QmlVtk", 1, 0, "Fbo")
    QSurfaceFormat.setDefaultFormat(setDefaultSurfaceFormat(False))

    app = App(sys.argv)

    if len(app.engine.rootObjects()) == 0:
        print("No QML file is loaded!")
        return

    #! Make sure MainView is active --> FboRenderer is created
    QTimer.singleShot(0, app.setup)
    sys.exit(app.exec())


if __name__ == "__main__":
    setVtkLog()

    sys.excepthook = exceptHook

    main()
