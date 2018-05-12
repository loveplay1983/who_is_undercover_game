from tkinter import *
from tkinter.ttk import *
import spy_temp

class App:
    def __init__(self, spy_temp):
        # 当轮玩家数
        self._pnum = 0
        # PlayGame类
        self.playgame = spy_temp
        # 随机选出的单词
        self.wpcuword = []
        self.wplayers = []
        self.wnlayers = []
        # 被投票玩家
        self._voteflag = 0
        # label上面显示的文本
        self._txt = []
        # 开始按键标志
        self.bstpress = 0
        # button 显示 标识
        self.bshshowflag = 1
        # 当前玩家数
        self.bshowflag = 0
        # 显示按键点击几次标志
        self.bshpress = 1
        # 投票按键点击几次标识
        self.bvtpress = 1
        self.tmp = []

    def spy(self):
        root = Tk()
        root.title('谁是卧底')  # 标题
        root.geometry('640x320+0+0')  #  窗口大小
        root.resizable(False, False)  # 设置窗口不可变

        # 创建Label
        label = Label(root, text='''游戏规则：\n
        1、游戏有卧底和平民两种身份。\n
        2、平民得到同一种词语，卧底得到与之相关的另一个词语。\n
        3、每人每轮用一句话描述自己拿到的词语，既不能让卧底察觉，也要给同伴以暗示。\n
        4、每轮描述完毕，所有在场的人投票，选出怀疑谁是卧底的人，得到票数最多的人出局。
        若出现平局，平局的人再进行描述，大家再进行投票选出其中一人。\n
        5、若有卧底撑到最后一轮（人数为两人），则卧底获胜，反之则平明胜利。
        ''')
        label.pack(side='top')

        frame = Frame(root)   # 定义一个窗体
        frame.pack(side='bottom')

        # 玩家数量框体
        plnu = Combobox(frame, width=12, state='readonly')  # 添加多选框
        plnu['values'] = ('玩家数量', 3, 4, 5, 6, 7, 8)  # 选项值
        plnu.grid(column=1, row=1)  # 设置位置
        plnu.current(0)  # 设定选择内容
        plnu.bind('<<ComboboxSelected>>', self.getpnum(plnu))  # 选择时触发函数事件

        # 开始Button
        bst = Button(frame, text='开始', command=lambda: self.bstart(label, plnu))
        bst.grid(column=2, row=1)

        # 投票玩家框体
        vonu = Combobox(frame, width=12, state='readonly')

        # 显示词语Button
        bsh = Button(frame, text='查看单词', command=lambda: self.bshow(label, vonu))
        bsh.grid(column=3, row=1)

        vonu.grid(column=4, row=1)
        vonu.bind('<<ComboboxSelected>>', self.getpnum(vonu))

        # 投票Button
        bvt = Button(frame, text='投票', command=lambda: self.bvote(label, vonu))
        bvt.grid(column=5, row=1)

        # 关闭Button
        bcl = Button(frame, text='结束游戏', command=self.bclose)
        bcl.grid(column=6, row=1)

        root.mainloop()

    def getpnum(self, plnu):
        pass

    def bstart(self, label, plnu):
        if self.bstpress == 0:
            label.configure(text='游戏开始')
            self.pnum = int(plnu.get())
            self.bshowflag = self.pnum
            self.bstpress = 1
            self.wplayers, self.wpcuword = self.playgame.startplay(self.pnum)
            for i in range(0, len(self.wplayers)):
                self.tmp.append(self.wplayers[i].name)
        else:
            label.configure(text='游戏正在运行')

    def bshow(self, label, vonu):
        # 显示玩家
        if self.bshpress <= self.bshowflag:
            txt = '玩家%d: %s' % (self.bshpress, self.wplayers[self.bshpress - 1].card)
        else:
            txt = '显示完毕，请投票'
        label.configure(text=txt)
        vonu['value'] = self.tmp
        self.bshpress += 1

    def bvote(self, label, vonu):
        self.pnum = len(self.wplayers)
        print(vonu.get(), ':  type:', type(vonu.get()))

        if self.bvtpress <= self.pnum:
            self.playgame.pgvote(int(vonu.get()))
            label.configure(text='玩家%s获得1票 %s/%s' % (vonu.get(), self.bvtpress, self.pnum))
        elif self.bvtpress == self.pnum + 1:

            self.wnlayers, self.wplayers = self.playgame.judge()
            if len(self.wnlayers) != 0:
                for i in range(0, len(self.wnlayers)):
                    self._txt.append(str(self.wnlayers[i].name))
                    if self.wnlayers[i].card == self.wpcuword[1]:
                        wtxt = '平民胜利'
                        label.configure(text=wtxt)
                        return
                    if self.wnlayers[i].name in self.tmp:
                        self.tmp.remove(self.wnlayers[i].name)
                        self.playgame.players.remove(self.wnlayers[i])
                str1 = " ".join(self._txt)
                label.configure(text= str1 + '号玩家已被淘汰, 游戏继续')
                vonu['value'] = self.tmp

                self._txt = []
            else:
                cards = []
                for i in range(0, len(self.wplayers)):
                    cards.append(self.wplayers[i].card)
                if len(self.wplayers) <= 2 and self.wpcuword[1] in cards:
                    txt = '卧底胜利'
                    label.configure(text=txt)
                    return
        else:
            label.configure(text='请等待进行下一轮投票')
            self.bvtpress = 1
            self.playgame.nplayers = []

        print(vonu.get())
        self.bvtpress += 1

    def bclose(self):
        exit()

    # @property
    # def pnum(self):
    #     return self._pnum
    #
    # @pnum.setter
    # def pnum(self, value):
    #     self._pnum = value
    #
    # @property
    # def voteflag(self):
    #     return self._voteflag
    #
    # @voteflag.setter
    # def voteflag(self, value):
    #     self._voteflag = value
    #
    # @property
    # def text(self):
    #     return self._txt
    #
    # @text.setter
    # def text(self, value):
    #     self._txt = value


if __name__ == '__main__':
    pg = spy_temp.PlayGame()
    w = App(pg)
    w.spy()
    print(w.pnum)
    print(w.text)
