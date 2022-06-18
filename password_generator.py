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

n = int(input('How many passwords do you need to generate? '))
length = int(input('How long should the password be? '))
add_digit = input('Should the numbers from 0 to 9 be included in the password? ')
add_lowercase = input('Should I include lowercase letters in the password? ')
add_uppercase = input('Should I include uppercase letters in the password? ')
add_punctuation = input('Should the characters "!#$%&*+-=?@^_"?" be included in the password? ')
remove_badsymbols = input('Should I exclude ambiguous characters "il1Lo0O"? ')

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