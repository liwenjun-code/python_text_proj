# 列表去重
my_list = [1,2,3,3,2,1,'a','a','c','b']

print(my_list)
my_list = list(set(my_list))
print(my_list)

# in/not in 可以判断数据是否存在容器里，对于字典来说，判断的是键（key）是否存在

if 3 in my_list:
    print('存在')
else:
    print('不存在')

