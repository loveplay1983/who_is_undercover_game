# use a Tkinter label as a panel/frame with a background image
# (note that Tkinter reads only GIF and PGM/PPM images)
# put a button on the background image

from tkinter import *

if False:
    root = Tk()
    root.title('Who is undercover???')
    root.config(bg='green')

    w = 800
    h = 650
    x = 450
    y = 130
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

    image = PhotoImage(file='undercover.gif')
    main = Frame(root)

    avatar = Label(main, image=image)
    description = Message(main,
                          text=
                          """游戏规则如下：
    1. 游戏有卧底和平民２种身份。
    2. 平民得到同一词语，卧底得到与之相关的另一词语。
    3. 每人每轮用一句话描述自己拿到的词语，既不能让卧底察觉，也要给同伴以暗示。
    4. 每轮描述完毕，所有在场的人投票，选出怀疑谁是卧底的人。得票数最多的人出局，
    若出现平局，平局的人再进行描述，大家再进行投票选出其中一人。
    5. 若有卧底撑到最后一轮（人数为两人），则卧底获胜，反之，则平民胜利。""",
                          width=800)
    description.config(font=('Helvetica', 13, 'bold'), anchor=W)
    description.config(bd=2, relief=SUNKEN)

    avatar.pack(side=TOP, fill=BOTH, expand='yes')
    description.pack(fill=X)

    main.pack(fill=BOTH)

    avatar.image = image
    root.mainloop()

class App:

    def __init__(self, root):
        self.root = root

    def set_root(self, w, h, x, y):
        master = self.root
        title = master.title('who is undercover???')
        bg = master.config(bg='green')
        geometry = master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        return title, bg, geometry

    def set_frame(self):
        img = PhotoImage(file='undercover.gif')
        frame = Frame(self.root)
        avatar = Label(frame, image=img)
        description = Message(frame,
                              text="""
游戏规则如下：
1. 游戏有卧底和平民２种身份。
2. 平民得到同一词语，卧底得到与之相关的另一词语。
3. 每人每轮用一句话描述自己拿到的词语，既不能让卧底察觉，也要给同伴以暗示。
4. 每轮描述完毕，所有在场的人投票，选出怀疑谁是卧底的人。得票数最多的人出局，
若出现平局，平局的人再进行描述，大家再进行投票选出其中一人。
5. 若有卧底撑到最后一轮（人数为两人），则卧底获胜，反之，则平民胜利。""",
                              width=800)
        description.config(font=('Helvetica', 13, 'bold'), anchor=W)
        description.config(bd=2, relief=SUNKEN)

        avatar.pack(side=TOP, fill=BOTH, expand='yes')
        description.pack(side=TOP, fill=X)

        frame.pack(fill=BOTH)
        self.root.mainloop()


main = Tk()
app = App(main)
app.set_root(800, 650, 450, 130)
app.set_frame()


