from PySide6.QtCore import QObject, Property
from PySide6.QtQml import QQmlApplicationEngine

from src.ctrls import RenderingCtrl
from src.ctrls.page2Ctrl import Page2Ctrl


class Page1Ctrl(QObject):
    def __init__(self, engine: QQmlApplicationEngine):
        super().__init__()
        self.__engine = engine

        ctxt = self.__engine.rootContext()
        ctxt.setContextProperty("Page1Ctrl", self)

    @Property(str, constant=True)
    def stackViewTxt(self) -> str:
        return "Page 1 View"