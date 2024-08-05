#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for l in range(0,nr_letters):
    password += letters[random.randint(0,len(letters)-1)]
for s in range(0,nr_symbols):
    password += symbols[random.randint(0,len(symbols)-1)]
for n in range(0,nr_numbers):
    password += numbers[random.randint(0,len(numbers)-1)]
print(f"Your base password is {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
length = nr_letters + nr_symbols + nr_numbers
letters_check = nr_letters
symbols_check = nr_symbols
numbers_check =nr_numbers

new_password =''

while length > 0:
    index = random.randint(0,2)
    if index == 0 and letters_check > 0:
        new_password += letters[random.randint(0,len(letters)-1)]
        letters_check -= 1
        length -=1
    elif index == 1 and symbols_check > 0:
        new_password += symbols[random.randint(0,len(symbols)-1)]
        symbols_check -= 1
        length -= 1
    elif index == 2 and numbers_check > 0:
        new_password += numbers[random.randint(0,len(numbers)-1)]
        numbers_check -= 1
        length -= 1


print(f"Your rand password is {new_password}")