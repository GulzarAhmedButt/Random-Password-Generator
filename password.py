import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
get_password = input("Enter your password length: ")
password = ''.join(random.sample(s,int(get_password)))
print(password)
