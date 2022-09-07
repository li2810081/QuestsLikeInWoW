from src import canvas_lable
from tkinter import *


root=Tk()

root.geometry("300x500")
root.title("任务")


# 锁定root宽度
root.grid_propagate(0)
root.resizable(0,0)


canvas = Canvas(root,highlightthickness=0)# 创建Canvas控件，并设置边框厚度为0
canvas.place(width=960,height=480)# 设置Canvas控件大小及位置
bg = PhotoImage(file='static/bg10.png')# 【这里记得要改成对应的路径】

canvas.create_image(300,240,image=bg)# 添加背景图片

# 添加时钟
canvas.create_text(50,10,text='',font=('楷体',15),fill='white',justify="center",anchor="nw",tag='time')
# 自动更新时间
def update_time():
    import time
    canvas.itemconfig('time',text=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    root.after(1000,update_time)

update_time()

from src.quests import *

print(canvas.find_all())
# 添加任务
q1=Quest1(canvas,50)


q2=Quest2(canvas,q1.end_y())

# 载入canvas



root.mainloop()

