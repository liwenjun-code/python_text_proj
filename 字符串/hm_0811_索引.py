str1 = 'abcdefg'

print(str1[0])
# 打印输出字符串中 最后一个字符
print(str1[-1])

# 字符串的遍历for
for i in str1 :
    print(i, end=' ')


# 字符串的遍历while
i = 0 #下标
while i < len(str1):
    print(str1[i])
    i+=1