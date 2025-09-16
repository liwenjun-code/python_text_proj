from service.login_service import login

print(login('admin','123456','8888'))
print(login('admin','123456','9999'))
print(login('admin','123321','8888'))
print(login('root','123456','8888'))
