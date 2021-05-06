#!/usr/bin/env python3

import random
import PySimgleGUI as sg

#initialize empty dict for win counter
wins = {"player_wins": 0, "computer_wins": 0}

#function call to continuously loop when more games are desired
def rockpaperscissorslizardspock():
  #setup various variables that are needed for different calls
  choice_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
  random_number = int(random.randint(1,5))

  computer_choice = choice_list[random_number - 1]
  #player input line, and capitalize first letter to compare to choice list
  player_choice = input("Choose rock, paper, scissors, lizard, or Spock: ")
  player_choice = player_choice.capitalize()
  #while loop to force player to choose a valid option of the 5 given
  while player_choice not in choice_list:
    player_choice = input("Not a valid option. Please choose rock, paper, scissors, lizard, or Spock: ")
    player_choice = player_choice.capitalize()
  #if elif statments for each option in the game results; includes a win counter
  if player_choice == choice_list[0] and computer_choice == choice_list[1]:
    print("Paper covers rock. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[0] and computer_choice == choice_list[2]:
    print("Rock crushes scissors. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[0] and computer_choice == choice_list[3]:
    print("Rock crushes lizard. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[0] and computer_choice == choice_list[4]:
    print("Spock vaporizes rock. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[1] and computer_choice == choice_list[0]:
    print("Paper covers rock. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[1] and computer_choice == choice_list[2]:
    print("Scissors cuts paper. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[1] and computer_choice == choice_list[3]:
    print("Scissors decapitates lizard. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[1] and computer_choice == choice_list[4]:
    print("Spock smashes scissors. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[2] and computer_choice == choice_list[0]:
    print("Rock crushes scissors. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[2] and computer_choice == choice_list[1]:
    print("Scissors cuts paper. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[2] and computer_choice == choice_list[3]:
    print("Scissors decapitates lizard. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[2] and computer_choice == choice_list[4]:
    print("Spock smashes scissors. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[3] and computer_choice == choice_list[0]:
    print("Rock crushes lizard. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[3] and computer_choice == choice_list[1]:
    print("Scissors decapitates lizard. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[3] and computer_choice == choice_list[2]:
    print("Lizard eats paper. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[3] and computer_choice == choice_list[4]:
    print("Lizard poisons Spock! You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[4] and computer_choice == choice_list[0]:
    print("Spock vaporizes rock. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[4] and computer_choice == choice_list[1]:
    print("Paper disproves Spock. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  elif player_choice == choice_list[4] and computer_choice == choice_list[2]:
    print("Spock smashes scissors. You win!")
    wins[player_wins] += 1
    print("You have won: " + str(wins[player_wins]) + " times!")

  elif player_choice == choice_list[4] and computer_choice == choice_list[3]:
    print("Lizard poisons Spock. PC wins!")
    wins[computer_wins] += 1
    print("The PC has won: " + str(wins[computer_wins]) + " times!")

  else:
    print("Result is a tie!")
  #ask player if they would like to go again
  yn_list = ["Y", "N"]
  player_rematch = input("Would you like to play again? [Y/N]")
  player_rematch = player_rematch.capitalize()
  #while loop to force either a y or n answer
  while player_rematch not in yn_list:
    player_rematch = input("Not a valid option. Please choose Y or N: ")
    player_rematch = player_rematch.capitalize()
  #what happens on y or n selection
  if player_rematch == "Y":
    rockpaperscissorslizardspock()
  if player_rematch == "N":
    if wins[player_wins] > wins[computer_wins]:
      print("The player won " + str(wins[player_wins]) + " games, while the PC won only " + str(wins[computer_wins]) + ".")
    elif wins[player_wins] < wins[computer_wins]:
      print("The PC won " + str(wins[player_wins]) + " games, while you won only " + str(wins[computer_wins]) + ".")
    elif wins[player_wins] == wins[computer_wins]:
      print("You and the PC won the same amount of games: " + str(wins[player_wins]) + "!")
  #function call to initiate the program
rockpaperscissorslizardspock()
