my_str = 'abcdefg'

 # 字符串[start:end:step]
 # 1.1取出字符串abc三个数据
print(my_str[0:3:1])
# 1.1如果step=1，可以不写
print(my_str[0:3])
# 1.2如果step为正数（大于0），开始位置为0，可以不写
print(my_str[:3])


# 2.取出字符串中efg三个数据
print(my_str[4:7])

# 2.1如果结束位置是字符串的长度（即最后一个数据要取到），可以不写
print(my_str[4:])

print(my_str[:])

print(my_str[::2])#从0开始，取到最后，步长为2

print(my_str[1:-1:3])#be

print(my_str[:-1:2])#ace

# 特殊情况，步长为负数，表示从右向左取，一般用法为字符串的反转，倒置
print(my_str[::-1])