# 导入tk

from time import strftime
from tkinter import *


# 设置背景透明

root = Tk()
root.attributes("-alpha", 0.5)

# 设置窗口标题
root.title("每日任务")

# 设置窗口大小
root.geometry("360x200")

# 设置窗口static/bg3.jpg图片为背景
bg = PhotoImage(file="static/bg10.png")
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 设置窗口背景透明
root.attributes("-alpha", 1)

# 设置窗口是否可变长、宽，True：可变，False：不可变
root.resizable(width=True, height=True)

# 添加时钟
def clock():
    # 获取当前时间
    time = strftime('%D \n %H:%M:%S %p')
    # 设置时钟
    clock_label.config(text=time)
    # 设置时钟延迟
    clock_label.after(1000, clock)

# 设置时钟
clock_label = Label(root, font=('楷体', 30), border=2, relief="groove")
# 背景透明
clock_label.config(bg=root.cget("bg"))
clock_label.pack(anchor='center',)
clock()


# 导入显示quests
from src.quests import Quest1

# 添加任务
Quest1(root).packs()




# 进入消息循环,不显示命令行
root.mainloop()
