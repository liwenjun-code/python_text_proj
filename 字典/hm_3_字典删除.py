my_dict = {'name':'小明','age': 18,'height':1.81,'is_man':True,
            'hobby':['抽烟','喝酒','烫头']}
print(my_dict)
# 删除 is_man
my_dict.pop('is_man')
print(my_dict)

# 删除抽烟的爱好
my_dict['hobby'].pop(0)
print(my_dict)
# 添加爱好 学习
my_dict['hobby'].append('学习')
print(my_dict)

# 括号的使用规则
# 等号左边出现的一定是[],主要通过下标修改列表中的数据；通过键修改（添加）字典中得数据
# 通过点（xx.xx()) 一定是小括号
