#!/usr/local/bin/python3
"""
谁是卧底也是深受很多人喜欢的游戏，起码要三人以上才能玩，大致分为几个阶段：1.分配平民词语和卧底词语--->2.
玩家依次发言--->3.根据发言投票认为谁是卧底--->4.得到票数最多的玩家出局--->5.出局玩家刚好是卧底则平民胜利，
如果出局玩家是平民则被冤死并继续第2步，当剩下的平民只有1个时卧底胜利。

特殊情况是，出现两名或以上的玩家票数相同，则相同票数的玩家重新发言，然后全体针对这几个玩家投票。

程序设计思想：输入玩家数num，玩家编号为0～num-1，然后定义三个含有num个元素的列表：词语列表，计算玩家票数的列表，
死亡玩家的列表。列表下标从0～num-1，随机产生该区间的数x，代表x号玩家是卧底，然后分配卧底词和平民词。注意，
提示几号玩家是卧底或冤死的时候，要将打印信息时候的下标加1，比如下标数0代表的其实是1号玩家。在生活中，
没多少人会习惯说自己是“第0个人”这种说法吧，除了程序员- -；

在每轮游戏中，依次进行发言，投票，票数最多的玩家出局（出现相同票数则重新发言），出局玩家归入死亡玩家列表。
然后开始下一轮。

那么，如果有num位玩家，则最多有多少轮游戏结束？因为进行到只有2位玩家游戏就结束了，所以答案是num-2轮！
也就是说上述流程要循环num-2次。

编程思想定了就可以敲代码了，程序代码如下：
"""
import random
from spyword import spyword

num = int(input('请输入玩家数（至少为3）\n'))
# 卧底玩家
spy = random.randint(0, num - 1)

# 随机产生词语 定义词语列表 计算玩家票数的列表 统计死亡玩家的列表
list_rand = spyword.popitem()
word = []
cnt = []
dead = []

# 给三个列表赋值
for i in range(0, num):
    word.append('a')
    cnt.append(0)
    dead.append(num + 2)

# 给玩家词语 其中print是调试用的,sanmeVote是出现相同票数的标志，spyWin是卧底胜利的判决条件
for i in range(0, num):
    if (i == spy):
        word[i] = str(list_rand[1])
    else:
        word[i] = str(list_rand[0])
    print(word[i])
sameVote = 0
spyWin = 0
# 游戏开始
for x in range(0, num - 1):
    for k in range(0, num):
        if ((k not in dead) & (sameVote == 0)):
            print('%d号玩家发言时间' % (k + 1))
    print('发言环节结束')

    # 将各位玩家的票数置0
    for j in range(0, num):
        if (j not in dead):
            cnt[j] = 0

    for j in range(0, num):
        if (j not in dead):
            vote2p = int(input('请%d号玩家投票' % (j + 1))) - 1
            cnt[vote2p] = cnt[vote2p] + 1
            sameVote = 0

    for y in range(0, num):
        if ((cnt[y] == max(cnt)) & (y != cnt.index(max(cnt)))):
            print('不止一位玩家得到最高票数,请这些玩家重新发言')
            sameVote = 1

    if (sameVote == 0):
        dead[x] = cnt.index(max(cnt))
        if (dead[x] == spy):
            print('卧底得到最多票数，游戏结束')
            spyWin = 1
            break
        print('%d号玩家被冤死!' % (dead[x] + 1))

        # 游戏结束
if (spyWin == 0):
    print('只剩两名玩家，卧底胜利！')