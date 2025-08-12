my_str = 'hello Python and itcast and itheima'

# 1,将字符串拆分为每个单词
result = my_str.split(' ')#['hello', 'Python', 'and', 'itcast', 'and', 'itheima']
print(result)
result1 = my_str.split()#['hello', 'Python', 'and', 'itcast', 'and', 'itheima']
print(result1)

# 2.按照and 进行拆分
result2 = my_str.split('and')#'hello Python ', ' itcast ', ' itheima']
print(result2)