from PySide6.QtCore import QObject, Property
from PySide6.QtQml import QQmlApplicationEngine


class StartCtrl(QObject):
    def __init__(self, engine: QQmlApplicationEngine):
        super().__init__()
        self.__engine = engine

        ctxt = self.__engine.rootContext()
        ctxt.setContextProperty("StartCtrl", self)

    @Property(str, constant=True)
    def stackViewTxt(self) -> str:
        return "Start View"