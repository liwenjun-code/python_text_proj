data =[
{'desc':'登录失败，用户名为空','username':'','password':"123456",'verify_code':'8888','expect':'用户名不能为空'},
{'desc':'登录失败，密码错误','username':'13888888','password':"123321",'verify_code':'8888','expect':'密码错误'},
{'desc':'登录失败，验证码错误','username':'1388888','password':"123456",'verify_code':'9999','expect':'验证码错误'}
] #列表里有字典--->列表里有元组

new_list = []
# 1.按照如下格式打印输出内容
# 用户名：xxx 密码：xxx 验证码：xxx 期望结果：xxx
for d in data: #d 字典
    print(f"用户名:{d.get('username')} 密码:{d.get('password')} 验证码:{d.get('verify_code')} 期望结果:{d.get('expect')}")
    d.pop('desc')#转换为元组之后不需要desc的值
    aa = tuple(d.values()) #获取每个字典的value值，转换为元组类型
    new_list.append(aa)#转换后的数据添加到列表中
# 2.将测试数据组成[(),()] --->后续自动化测试中，需要的数据类型
# [('','123456','8888','用户名不能为空'),(),()]
print(new_list)
