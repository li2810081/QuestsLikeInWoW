# 导入虚拟类
from abc import ABCMeta, abstractmethod
import os
from tkinter import Canvas, Event, PhotoImage, Tk
import tkinter
from turtle import title


# 任务类
class Quest(metaclass=ABCMeta):
    font_name="楷体"
    name_font=16
    note_font=12
    levels=["日","周","月","年"]
    levels_color=["orange","yellow","green","blue"]

    def __init__(self,canvas,y1:float, name:str, level:int, note:list ,description:str):
        self.name = name
        self.level = level
        self.note = note
        self.description = description
        self.canvas = canvas
        self.x1=5  # 任务的左x坐标
        self.x2=self.x1+300 # 任务的右边x坐标
        self.y1=y1 # 任务的上y坐标
        self.y2=self.y1+self.name_font+10 # 任务名称的下y坐标
        self.y3=self.y2+self.note_font*(len(self.note)+1)+10 # 任务的下y坐标

        self.q_name= self.canvas.create_text(self.x1,self.y1,**self._q_name_str())
        self.q_notes=[]
        for nt in range(len(self.note)):
            note=self.note[nt]
            self.q_notes.append(self.canvas.create_text(self.x1,self.y2+self.note_font*nt,**self._q_note_str(note)))
        self.after()        
        
        self.canvas.tag_bind(self.q_name,'<Enter>',self.move_on)
        self.canvas.tag_bind(self.q_name,'<Leave>',self.move_off)
        self.canvas.tag_bind(self.q_name,'<Button-1>',self.on_click)
        

    def _q_name_str(self):
        return {
            "text":"[%s]%s"%(self._q_level_str(),self.name),
            "font":(self.font_name, self.name_font,"bold"),
            "fill":self.levels_color[self.level],
            "anchor":"nw",
            }
    
    def _q_note_str(self,note):
        return {
            "text":"   - "+note,
            "font":(self.font_name, self.note_font,"italic"),
            "fill":"#ffe5e5",
            "anchor":"nw",
        }
    
    def _q_level_str(self):
        return self.levels[self.level]



    def end_y(self):
        return self.y3

    def on_click(self):
        pass

    def move_on(self,event:Event=None):
        # 字体外发光
        self.canvas.itemconfig(self.q_name,fill="white")
        [self.canvas.itemconfig(x,fill="white") for x in self.q_notes]

    def move_off(self,event:Event=None):
        # 字体恢复
        self.canvas.itemconfig(self.q_name,fill=self.levels_color[self.level])
        [self.canvas.itemconfig(x,fill=self.levels_color[self.level]) for x in self.q_notes]


    def Move(self,event:Event):
        # 打印所有的pos
        print(event.x,event.y)
        print(self.canvas.coords(self.q_name))
        ## ------- 焦点半获取状态检测 ------- ##
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y3:
            self.move_on()
        else:
            self.move_off()
    
    @abstractmethod
    def on_click(self,event:Event):
        pass        

    @abstractmethod
    def after(self):
        pass  

# 任务详情页面 
class QuestDetail:
    def __init__(self,quest:Quest):
        self.tk= tkinter.Toplevel() 
        self.tk.title(quest.name)
        self.tk.geometry("400x600")
        self.tk.resizable(0,0)
        # 获取父路径
        path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 设定背景图片
        self.bg=PhotoImage(file=path+"/static/question-background.png")
        self.canvas=Canvas(self.tk,width=900,height=1600)
        self.canvas.create_image(0,0,anchor="nw",image=self.bg,tag="bg")
        # 图片拉伸
        self.canvas.pack(expand="yes")
        self.canvas.create_text(200,20,text=quest.name,font=(quest.font_name,quest.name_font,"bold"),fill=quest.levels_color[quest.level],anchor="n") 
        self.tk.mainloop()           
        


# 任务1
class Quest1(Quest):
    def __init__(self,root,y1:float):
        super().__init__(root,y1,"任务任务1的备注1",0,["任务1的备任务1的备注任务1的备注注"],"任务1的描述")
    
    def on_click(self, event: Event):
        print("任务1被点击了")
        QuestDetail(self)

    def after(self):
        pass

# 任务2

class Quest2(Quest):
    def __init__(self,root,y1:float):
        super().__init__(root,y1,"任务2的备注",1,["任务2的备注"],"任务2的描述")
    
    def on_click(self, event: Event):
        print("任务2被点击了")

    def after(self):
        pass

