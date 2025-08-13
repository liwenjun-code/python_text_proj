#方式一 类实例化
# 1.1 空元组 没有实际意义
my_tuple = tuple()

# 1.2 类型转换
# 1.2.1 将字符串转换为元组
my_tuple1 =tuple('love')
print(my_tuple1)
# 1.2.2 将列表转换为元组，即将列表的中括号变为小括号
my_tuple2 = tuple([1,2,3])
print(my_tuple2)
# 方式二 直接使用()
# 2.1 空元组 没有实际意义
my_tuple3 = ()
# 2.2 非空
my_tuple4 = ('小明',18,1.81,True)
print(my_tuple4)


# 特殊：定义一个数据的元组，在数据后边必须加上一个逗号
my_tuple5 = (10,)
print(my_tuple5)

# len(),count()
# 下标
print(my_tuple4[0])

# 元组和列表最大的差别就是元组不可以修改增加删除