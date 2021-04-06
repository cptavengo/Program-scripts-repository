#!/usr/bin/env python3

import random

number_characters = input("How many characters do you want in the password? ")
while number_characters.isnumeric() == False:
   number_characters = input("Please choose a number. ")
def password_generator(number_characters):
  password = ""
  for i in range(0, number_characters):
    if i < number_characters:
      random_letter = random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
      random_capitalize = random.randint(0,1)
      if random_capitalize == 1 and random_letter.isalpha():
        random_letter = random_letter.upper()
      i += 1
      password += random_letter
  return print("Your randomly generated password is: " + str(password))

password_generator(int(number_characters))
