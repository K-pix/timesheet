import random
import string

#Function to generate a password of specified length
def generate_password(length):
    print("Password length must be at least 8 and lessthan 16 ")
    if length >= 8 and length<=16:
      
       ascii_characters = string.ascii_letters + string.digits + string.punctuation 
 
       password = ""
       for i in range(length):
        random_char = random.choice(ascii_characters)
        password += random_char
        password_1=password.capitalize()
    
       else:
        print("please enter valid length")
    return password_1
    
    

length = int(input("How long do you want your password to be? "))

print(generate_password(length))