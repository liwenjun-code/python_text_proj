"""
需求：定义函数get_max 返回两个数字中比较大的数字
"""

def get_max(a,b):
    if a > b:
        return a
    else :
        return b

result = get_max(10,20)
print(result)
#使用返回值可以得到这个数据值，可以对这个数据值进行其他的计算
result += 10
print(result)