def sum_2_num(a,b):
    return a + b

def add_2_num(c,d):
    return c + d

def add_3_num(e,f,g):
    return e + f + g

# 固定写法，作用：代码中作为模块被导入的时候，不想执行的代码，写在这个缩进中
# 一般来说：函数掉用都写在缩进中，函数的定义不写在缩进中
if __name__ == '__main__':
    print(add_2_num(10, 20), __name__)

# 1.如果运行代码文件，发现__name__的值是__main__
# 2.如果是作为模块导入运行，__name__的值，不是__main__是模块名
