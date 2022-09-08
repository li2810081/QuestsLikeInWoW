
import sys
from django.conf import settings
from PySide6 import QtCore, QtWidgets, QtGui
# 基于pyside6的任务窗口框体
class MyWidget(QtWidgets.QWidget):
    def __init__(self,title:str):
        super().__init__()
        self.setWindowTitle(title)
        # 不显示表头
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 设置背景图片
        self.bg=QtGui.QPixmap(settings.STATIC_ROOT  / "question-background.png")
        # 设置背景图片拉伸
        self.bg=self.bg.scaled(self.width(),self.height())
        
        self.setAutoFillBackground(True)
        # 设置窗口大小
        self.resize(300, 700)
        
class QuestWindow():
    def __init__(self, title: str):
        self.title = title
    def run(self):
        from .widget import MainWidget
        app = QtWidgets.QApplication([])

        widget = MainWidget(self.title)
        widget.show()
        
        sys.exit(app.exec())