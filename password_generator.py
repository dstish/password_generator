import random

def generate_passwords(long, chars):
    password = ''
    for _ in range(long):
        password += random.choice(chars)
    print(password)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ' '

n = int(input('Сколько паролей вам нужно сгенерировать? '))
length = int(input('Какой длины должен быть пароль? '))
add_digit = input('Включать ли в пароль цифры от 0 до 9? ')
add_lowercase = input('Включать ли в пароль прописные буквы? ')
add_uppercase = input('Включать ли в пароль строчные буквы? ')
add_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
remove_badsymbols = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if add_digit.lower() in ('да', 'yes', 'д'):
    chars += digits
if add_lowercase.lower() in ('да', 'yes', 'д'):
    chars += lowercase_letters
if add_uppercase.lower() in ('да', 'yes', 'д'):
    chars += uppercase_letters
if add_punctuation.lower() in ('да', 'yes', 'д'):
    chars += punctuation
if remove_badsymbols.lower()in ('да', 'yes', 'д'):
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for _ in range(n):
    generate_passwords(length, chars)