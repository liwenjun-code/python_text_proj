from traceback import format_exc

my_dict = {'name':'小明','age': 18,'height':1.81}

print('遍历字典的键')
for k in my_dict:
    print(k)

print('_'*30)
print(my_dict.keys())
print('_'*30)

for k in my_dict.keys():
    print(k)

print('\n遍历字典的值\n')
print(my_dict.values(),tuple(my_dict.values()))
for v in my_dict.values():
    print(v)

print('遍历字典的键对值')
for k,v in my_dict.items():
    print((k,v))
