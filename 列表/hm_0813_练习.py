
import random

#1.使用随机数向列表添加10个1-20之间的随机整数
my_list = []
for i in range(10):
    num = random.randint(1,20)
    my_list.append(num)
print(my_list)
# 2.统计数据8出现的个数
print(f'数据8在列表中出现的次数：{my_list.count(8)}')
# 3.删除最后一个数据
my_list.pop()
print(my_list)
# 4.修改第一个数据为8
my_list[0] = 8
print(my_list)
# 5.再次统计数据8出现的个数
print(f'数据8在列表中出现的次数：{my_list.count(8)}')
