#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




password = ""
option = "yes"
while(option == "yes"):
  print("Welcome to the PyPassword Generator!")
  nr_char= int(input("How many total characters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  if(nr_char > (nr_symbols + nr_numbers)):
    for symbol in range(0,nr_symbols):
      password += random.choice(symbols)
    for number in range(0,nr_numbers):
      password += random.choice(numbers)
    for char in range(0,nr_char - (nr_symbols + nr_numbers)):
      password += random.choice(letters)
    option = "no"
  else:
    option = input("Numbers of letters should be greater than the number and symbols combined. Do you want to start again? Type \"yes\" or \"no\" : ").lower()



new_password = ("".join(random.sample(password, len(password))))

print(f"Here is your password: {new_password}")




