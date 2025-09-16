def login(username,password,code):
    if code == '8888':
        if username == 'admin' and password == '123456':
            return '登录成功'
        else:
            return '用户名和密码错误'
    else:
        return '验证码错误'
