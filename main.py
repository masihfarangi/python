import string,random
while True:
    length= int(input("please enter a preferd pasword length:"))
    chars = string.ascii_letters + string.digits + '!@#$^*&_+-'
    text = []
    for i in range(length):
        text.append(random.choice(chars))
    password = ''.join(text)

    print('your password:{}'.format(password))