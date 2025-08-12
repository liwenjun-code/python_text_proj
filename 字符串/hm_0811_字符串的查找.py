#1.现有字符串数据：‘黑马程序员’
my_str = '黑马程序员'
# 2.请设计程序，实现判断“黑马”和“白马”是否存在语数据中
name = input('请输入要判断的数据：')
result = my_str.find(name)
# 3.要求如果数据存在，则输出数据所在的位置
if result == -1:
    print(f'没有找到{name}这个数据')
else:
    print(f'找到了{name}这个数据，所在的位置为{result}')