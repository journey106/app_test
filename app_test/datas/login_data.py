user_login_success = [{'mobile':'18684720553', 'pwd': 'python', 'msg':'我的账号[python10]'}]
# 手机号错误
user_mobile_error = [
    {'mobile': '123', 'pwd': 'python', 'msg': '无效的手机号'},
    {'mobile': '', 'pwd': 'python', 'msg': '无效的手机号'},
    {'mobile': '1868472055', 'pwd': 'python', 'msg': '无效的手机号'}
]

# 密码错误
user_pwd_error = [
    {'mobile': '18684720553', 'pwd': 'py', 'msg': '手机号或密码错误'},
    {'mobile': '18684720553', 'pwd': 'python1', 'msg': '手机号或密码错误'}
]

user_invalid = [
    {'mobile': '13657890546', 'pwd': '12', 'msg': ''},
    {'mobile': '1868472055', 'pwd': '1234567', 'msg': ''}
]
