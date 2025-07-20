import random

while True:
    player = int(input("玩家出拳（石头1，剪刀2，布3,退出0）："))
    if player == 0 :
        print("欢迎下次使用本游戏！")
        break
    elif player != 1 or player !=2    or player != 3:
        print("输入的内容不对，请重新输入！")
        continue
    computer = random.randint(1, 3)
    print("电脑出拳：{}".format(computer))
    if (player==1 and computer == 2) or (player==2 and computer == 3) or (player==3 and computer == 1):
        print("玩家胜利！")
    elif player == computer :
        print("平局")
    else:
        print("电脑胜利！")
    # 1、player输入的是字符串记得强制转换为整型才能比较
    # 2、random随机数的使用