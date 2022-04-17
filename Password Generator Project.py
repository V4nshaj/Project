#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
l1=len(letters)
l2=len(numbers)
l3=len(symbols)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
s=''
for i in range(0,nr_letters):
    s+=random.choice(letters)#choice to choose random letters
for i in range(0,nr_numbers):
    s+=random.choice(numbers)

for i in range(0,nr_symbols):
    s+=random.choice(symbols)
print("Password: ", s)
#hard level
password = []#declaring list variable
for i in range(0,nr_letters):
    password+=random.choice(letters)#choice to choose random letters
for i in range(0,nr_numbers):
    password.append(random.choice(numbers))

for i in range(0,nr_symbols):
    password.append(random.choice(symbols))#append is same as + but at last
print("Password in sequence: ", password)
random.shuffle(password)
t=''
for i in password:
    t=t+i
print("Password: ", t)

