"""
import tools

result = tools.sum_2_num(10,20)
print(result)

from tools import sum_2_num

results = sum_2_num(10,20)
print(results)

"""
from random import randint

import tools
from 列表.hm_0812_列表定义 import my_list
from 模块和包.tools import add_2_num

result1 = add_2_num(10,20)
print(result1)

from tools import  add_3_num
result2 = add_3_num(1,2,3)
print(result2)

# 1.定义一个函数，make——data，在列表中随机创建10个1-100之间的数字
my_list11 = []
def make_data():

    for i in range(10):
        my_list11.append(randint(1, 100))
    print(my_list)

make_data()
# 2.定义一个函数，返回列表中最大值
def my_max():
    my_list11.sort()
    return my_list11[-1]

print(my_max())

#3.定义一个函数sum_set接收一个参数n，在函数中计算1+2+3+...+n的值，并打印结果
def sum_test(n):
    num = 0
    for i in range(n+1):
        num += i
    print(num)

sum_test(100)


"""
4.有如下列表：
my_list12= [{'id':1,''money':10},{'id':2,''money':20},{'id':3,''money':30},
{'id':4,''money':40}]
要求：定义一个函数func，功能如下
    1.如果字典中ID的值为奇数，则对money的值加20
    2.如果字典中ID的值为偶数，则对money的值加10
    3.打印输出列表，查看最终结果
"""
my_list12 = [{'id':1,'money':10},{'id':2,'money':20},{'id':3,'money':30},
{'id':4,'money':40}]

def func():
    for i in my_list12: #i 字典
        #判断字典的id值时奇数还是偶数
        if i.get('id') % 2 == 0:
            i['money'] += 10
        else:
            i['money'] += 20
    print(my_list12)

func()

"""
5.定义一个函数，作用：打印每个字符出现的次数
    要求：1.在函数内部提示输入一个字符串
        2.输出每个字符出现的次数
        3.相同的字符，只打印一次
    举例：aabcda
    a：3，b:1，c:1,d:1
"""
def func1():
    my_str12 = input('请输入一个字符串：')
    #需要一个 东西（字典，键 字符 ，值，出现的次数） 将每个字符出现的记录下来
    my_dict12 = {}
    for i in my_str12:
        my_dict12[i] = my_str12.count(i)
    print(my_dict12)
    for k,v in my_dict12.items():
        print(f'{k}:{v}')

func1()

"""
6.设计过7游戏，定义一个函数func，要求如下：
    1.该函数接收一个参数，为一个1-99之间的数字
    2.函数对该数字到99之间的所有数字进行判断，如果数字包含7，或者是7的倍数，则输出：“过...”，
    否则输出具体的数字
"""

def func13(n):
    i = n
    while i <= 99:
        if i % 7 == 0 or str(i).find('7') != -1:#count('7')！=0/'7' in str(i)
            print('过...')
        else:
            print(i)
        i += 1
func13(3)
