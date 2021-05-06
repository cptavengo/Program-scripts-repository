#!/usr/bin/env python3

import random

random_int = random.randint(0,20)
guessed_number = input("Guess the number chosen: ")
guessed_number = int(guessed_number)
while guessed_number != random_int:
  if guessed_number == random_int:
    break

  elif guessed_number > random_int:
    print("The guess is too high.")
    guessed_number = input("Guess another lower number: ")
    guessed_number = int(guessed_number)

  elif guessed_number < random_int:
    print("The guess is too low.")
    guessed_number = input("Guess another higher number: ")
    guessed_number = int(guessed_number)

print("That was the number!")
print("Now exiting.")
