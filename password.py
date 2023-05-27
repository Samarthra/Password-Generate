lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPRSTUVWXYZ'
special='!@#$%^&*()?'
decimal='0123456789'

import random

def contain(letters,password):
    for letter in letters:
        if letter in password:
            return True
    return False

def strongpassword(password):
    if not contain(lower,password):
        return False
    if not contain(upper,password):
        return False
    if not contain(special,password):
        return False
    if not contain(decimal,password):
        return False
    return  True

legal_char=lower+upper+special+decimal
while True:
    password=''
    for _ in range(16):
        password+=random.choice(legal_char)
    if strongpassword(password):
         password=password[:4]+'-'+password[4:8]+'-'+password[8:12]+'-'+password[12:]
         print(password)
         break