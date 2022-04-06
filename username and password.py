passwords = {'benp':'123321', 'josew':'chead123'}
username = input('username: ')
password = input('password: ')
if password == passwords[username]:
    print('You are logged in')
else:
    print('Error, please try again.')
