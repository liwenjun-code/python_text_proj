my_str = 'good good study'

# 1.将字符串中所有的good 替换为GOOD
my_str1 = my_str.replace('good','GOOD')
print(my_str1)

# 2.将字符串my_str中的第一个good替换为Good
my_str2 = my_str.replace('good','Good',1)
print(my_str2)

# 3.将字符串my_str中的第二个good替换为Good
# 先将前两个替换为Good，再将第一个替换为good
my_str3 = my_str.replace('good','Good',2).replace('Good','good',1)#链式编程
print(my_str3)
