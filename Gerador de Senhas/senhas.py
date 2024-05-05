'''
Roberto Junior, 2024/05/01
Title: Gerador de Senhas (Password Generator)
'''

import random
import string

def password_generator(len_pass = 8):
    ascii_opt = string.ascii_letters
    number_opt = string.digits
    punct_opt = string.punctuation
    opt = ascii_opt + number_opt + punct_opt

    password = ''

    for i in range(0, len_pass):
        digit = random.choice(opt)
        password = password + digit

    return password

answer_user = input('Senha de quantos dígitos? ')

if answer_user.isdigit():
    answer_user = int(answer_user)
else:
    print('Entrada inválida!')
    quit()

passw = password_generator(len_pass = answer_user)

print(f'A senha gerada é: {passw}')
