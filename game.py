import random

people = int(input("请输入参与游戏人数(必须3人以上)："))
terms = {'钢笔':'铅笔', '美人痣':'青春痘', '陈奕迅':'张学友'}

mole_term1 = terms.popitem()
mole_term = mole_term1[1]
mole_number = random.randint(0, people-1)

print(mole_number)
print(mole_term)


terms_list = []
ballot = []
out = []

for i in range(0, people):
    terms_list.append(1)
    ballot.append(0)
    out.append(0)

print(terms_list)
print(ballot)
print(out)


for c in range(0, people-2):
    for a in range(0, people):
        if out[a] == 1:
            continue
        else:
            terms_list[a] = mole_term1[0]
            terms_list[mole_number] = mole_term
            print('%s号玩家请发言'%a)
    print('发言结束')
    print(terms_list)

    for b in range(0, people):
        if out[b] == 1:
            continue
        else:
            ballots = int(input('%s号玩家请投票：'%b))
            ballot[ballots] = ballot[ballots] + 1
        # print(ballot)
    print('投票结束')

    if ballot.index(max(ballot)) == mole_number:
       print('卧底得票最多，平民胜利')
       break

    else:
        out.insert(ballot.index(max(ballot)), 1)
        print('%s号玩家冤死，继续发言'%ballot.index(max(ballot)))
        ballot[ballot.index(max(ballot))] = 0

    if out.count(1) >= people - 2:
        print('平民人数不足，卧底获胜')
        break
