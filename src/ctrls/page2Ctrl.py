from PySide6.QtCore import QObject, Property
from PySide6.QtQml import QQmlApplicationEngine


class Page2Ctrl(QObject):
    def __init__(self, engine: QQmlApplicationEngine):
        super().__init__()
        self.__engine = engine

        ctxt = self.__engine.rootContext()
        ctxt.setContextProperty("Page2Ctrl", self)

    @Property(str, constant=True)
    def stackViewTxt(self) -> str:
        return "Page 2 View"