# 1.使用单引号定义
my_str1 = 'hello'
# 2.使用双引号定义
my_str2 = "hello"
# 3.使用三引号定义
my_str3 = """hello"""
my_str4 = '''hello'''


# 4.字符串本身包含单引号，定义的时候，不能使用单引号定义，使用双引号定义
# 字符串本身包含双引号，定义的时候，不能使用双引号定义，使用单引号定义

# i'm jack
my_str5 = "i'm jack"

# 5.使用转义字符

# 原生字符串，即在字符串前边加上r“”表示字符串中的内容不会进行转义，一般用在Windows的路径中
my_str6 = r'i\'m jack'
print(my_str6)
