#1.定义空字典
# 变量 = dict()
# 变量 = {}
my_dict = dict()
my_dict1 = {}
print(my_dict,my_dict1,type(my_dict),type(my_dict1))

# 2.定义非空字典
# 变量  = {键：数据值，键：数据值，....}
my_dict2 = {'name':'小明','age': 18,'height':1.81,'is_man':True,
            'hobby':['抽烟','喝酒','烫头']}
print(my_dict2,len(my_dict2))