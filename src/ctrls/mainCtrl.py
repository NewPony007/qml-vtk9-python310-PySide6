from PySide6.QtCore import QObject, Property
from PySide6.QtQml import QQmlApplicationEngine

from src.ctrls import RenderingCtrl
from src.ctrls.startCtrl import StartCtrl


class MainCtrl(QObject):
    def __init__(self, engine: QQmlApplicationEngine):
        super().__init__()
        self.__engine = engine

        ctxt = self.__engine.rootContext()
        ctxt.setContextProperty("MainCtrl", self)

        self.startCtrl = StartCtrl(engine)
        self.renderCtrl = RenderingCtrl(engine)

    @Property(str, constant=True)
    def stackViewTxt(self) -> str:
        return "Main View"