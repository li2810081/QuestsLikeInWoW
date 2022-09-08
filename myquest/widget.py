from PySide6 import QtCore, QtWidgets, QtGui
from django.conf import settings

from myquest.models import Quest


# 基于pyside6的任务窗口框体
class MainWidget(QtWidgets.QWidget):
    def __init__(self,title:str):
        super().__init__()
        self.setWindowTitle(title)
    #    # 设置窗口背景透明
    #     self.setWindowFlags(QtCore.Qt.FramelessWindowHint)        
    #     self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 可拖动
        self.setMouseTracking(True)

        # 设置窗口大小
        self.resize(300, 700) 

        self.layout = QtWidgets.QVBoxLayout()

     
        # 载入任务部件
        for quest in Quest.objects.all()[:5]:
            _q_quest=QuestWidget(quest)
            _q_quest.follow()
            self.layout.addWidget(_q_quest)
        
        self.setLayout(self.layout)

    def move(self,offset:QtCore.QPoint):
        self.move(self.pos()+offset)

# 拖动锚点
class AnchorWidget(QtWidgets.QWidget):
    def __init__(self,parent:QtWidgets.QWidget=None):
        super().__init__()
        self.setFixedSize(20, 20)
        self.setStyleSheet("background-color: #000000; border-radius: 15px;")
        self.help = QtWidgets.QLabel(self)
        self.help.setText("拖动")
        self.parent=parent

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPos = event.globalPos() - self.frameGeometry().topLeft()
            self.parent.move(self.dragPos)
            event.accept()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPos)
            self.parent.move(event.globalPos() - self.dragPos)
            event.accept()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPos)
            self.parent.move(event.globalPos() - self.dragPos)
            event.accept()
        

class QuestWidget(QtWidgets.QWidget):
    def __init__(self,quest:Quest):
        super().__init__()
        self.quest=quest
        self.levels_color = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#8b00ff"]



    def follow(self):
        # 设定楷书
        # 任务名称
        self.q_name = QtWidgets.QLabel(self.quest.name)      
        self.q_name.setStyleSheet("font-family:'楷书';font-size: 18px; font-weight: bold; color: %s;" % self.levels_color[self.quest.level])
        # 字体描边
        self.q_name.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=2, yOffset=2))

        self.q_remark=QtWidgets.QLabel(self.quest.remark)
        self.q_remark.setStyleSheet("font-size: 12px; color: #ff0000;")
        # 任务按钮点击事件
        # self.q_name.clicked.connect(self.on_button_clicked)
     
        # 任务布局
        self.quest_layout=QtWidgets.QVBoxLayout()
        self.quest_layout.addWidget(self.q_name)
        self.quest_layout.addWidget(self.q_remark)
        self.setLayout(self.quest_layout)

    def on_button_clicked(self):
        print("开始任务:%s" % self.quest.name)



    