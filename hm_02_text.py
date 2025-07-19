"""
name = '张三'
age = 18
print(name,age)
"""
from sys import flags

# shift+回车——换行

"""
# 整型
num = 10
print(num,type(num))  # 10 <class 'int'>

# 浮点型
num2 = 3.14
print(num2,type(num2)) # 3.14 <class 'float'>
# 布尔型
num3 = True
print(num3,type(num3)) # True <class 'bool'>
#字符串类型
name = "lisi"
print(name,type(name))

"""

"""
age = input("请输入你的名字：")
print(age)

num = input("请输入一个数字：")
print(num)

"""

"""
age = input("please input your age:")
Int_age = int(age)
print(age,type(age))
print(Int_age,type(Int_age))

num = input("please number:")
Num_1 = float(num)
print(num,type(num))

name = input("please input your name:")
Name_1 = str(name)
print(name,type(name))
print(Name_1,type(Name_1))

"""

"""
name = '张三'
age = 18
height = 1.98

# 按照如下的格式显示个人信息
# 我的名字是xx，年龄是xx岁，身高xxm
print('我的名字是 {},年龄是 {} 岁, 身高 {} m'.format(name,age,height))
print(f'我的名字是{name},年龄是{age}岁，身高{height}m')

num1 = float(input("please inpur num1:"))
num2 = float(input("please input num2:"))
sum = num1 + num2
print(f'{num1}+{num2} = {sum}')

"""

"""
print(9/2)
print(9//2)
print(9%2)
print(9*2)
print(9**2)
# 先乘除 求商 求余 再加减 不知道加括号，优先级最高

"""

"""
name = input("please input your name:")
age = input("please age :")
height = input("please your heigth:")
print("我的名字是{}，年龄是{}岁，身高是{}厘米".format(name,age,height))
print(f"我的名字是{name}，年龄是{age}岁，身高是{163}厘米")




use_name = input("请输入用户名：")
password = input("请输入密码：")
print("用户名是：{},密码是：{}".format(use_name,password))
print(f"用户名是：{use_name},密码是：{password}")

day = int(input("请输入天数："))
second = day * 24 * 3600
print(f"{day}天等于{second}秒")


age = int(input("please input your age:"))
if age >= 18:
    print("It is ok")
else:
    print("Minors are prohibited from entering")


score = int(input("please your score:"))
if score >= 90:
    print("优")
elif 80 <= score < 90:
    print("良")
elif score >=70 and score < 80 :
    print("中")
elif score >=60 and score < 70 :
    print("差")
else:
    print("不及格")


"""

password = int(input("please your password:"))
if password == 123456 :
    print("password correct !")
    qukuan = int(input("please your qukuan:"))
    if qukuan <= 1000:
        print("请输入您要取款的金额:{}".format(qukuan))
    else:
        print("余额不足")
else:
    print("密码错误")








