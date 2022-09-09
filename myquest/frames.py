
import sys
import tkinter
from django.conf import settings

from myquest.models import Quest

class QuestWindow(tkinter.Tk):
    def __init__(self,title):
        super().__init__()
        self.title(title)
        self.geometry("800x600")

        # 隐藏头部
        self.overrideredirect(True)
        # 背景透明
        self.config(
            bg="#000000",
            bd=0,
            highlightthickness=0,
        )
        
        #添加关闭按钮
         
        # 左边部分设定背景
        self.bg1=tkinter.PhotoImage(file=settings.STATIC_ROOT /  "QUESTFRAME/UI-QuestLogDualPane-Left.PNG")
    
        # 右边部分设定背景
        self.bg2=tkinter.PhotoImage(file=settings.STATIC_ROOT / "QUESTFRAME/UI-QUESTLOGDUALPANE-RIGHT.PNG")

    
        # 合并背景
        # self.bg=tkinter.PhotoImage()
        # self.bg.tk.call(self.bg, 'copy', self.bg1, '-compositingrule', 'over', self.bg2, '-compositingrule', 'over', 0, 0)

        # 设定背景
        self.canvas=tkinter.Canvas(self,width=800,height=600)
        self.canvas.create_image(0,0,image=self.bg1,anchor='nw')
        self.canvas.pack()







    def run(self):
        self.mainloop()