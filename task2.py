
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8']
symbols=['.','#','@','!']
print("welcome to password genrator")
n_letters=int(input("how many letter you want in password="))
n_symbols=int(input("how many symbol you want in password="))
n_numbers=int(input("how many number you want in password="))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list += char

for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list += char

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list += char

random.shuffle(password_list)

print(password_list)

password=""
for char in password_list:
    password += char
print(password)                                             