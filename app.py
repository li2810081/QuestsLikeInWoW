# from src import canvas_lable
from tkinter import * 
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

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

# 载入url页面
def load_url(url):
    import webbrowser
    webbrowser.open(url)

# 添加按钮
canvas.create_text(50,50,text='打开百度',font=('楷体',15),fill='white',justify="center",anchor="nw",tag='baidu')
canvas.tag_bind('baidu','<Button-1>',lambda e:load_url('https://www.baidu.com'))

# 添加文本
canvas.create_text(50,100,text='这是一段文本',font=('楷体',15),fill='white',justify="center",anchor="nw",tag='text')

# 添加图片
canvas.create_image(50,150,image=PhotoImage(file='static/bg10.png'))

# 添加输入框



# 载入canvas



root.mainloop()

