my_list = [1,2,3]
print(my_list)

my_list1 = my_list[::-1]
print('切片进行反转，原列表的数据不会发生改变')
print('my_list:',my_list)
print('my_list1:',my_list1)

my_list.reverse()
print('使用reverse方法，直接修改原列表')
print(my_list)