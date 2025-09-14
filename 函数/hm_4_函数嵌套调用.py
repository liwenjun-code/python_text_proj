def fun1():
    print(1)
    print('func 1')
    print(2)

def fun2():
    print(3)
    fun1()
    print(4)


print(5)
fun2()
print(6)
