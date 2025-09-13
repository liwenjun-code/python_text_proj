my_dict = {'name':'小明','age': 18,'height':1.81,'is_man':True,
            'hobby':['抽烟','喝酒','烫头']}
# 获取年龄信息(键存在)

print(my_dict['age'])
print(my_dict.get(('age')))

# 获取体重信息（键存在）
# print(my_dict['weight'])#代码会报错，原因是键不存在
print(my_dict.get('weight'))#None

# 获取第一个爱好（获取列表中的第一个数据）
print(my_dict['hobby'][0])
print(my_dict.get('hobby')[0])