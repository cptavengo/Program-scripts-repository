#!/usr/bin/env python3

import random
#initialize empty lists for win counter
computer_wins = []
player_wins = []
#function call to continuously loop when more games are desired
def rockpaperscissors():
  #setup various variables that are needed for different calls
  choice_list = ["Rock", "Paper", "Scissors"]
  random_number = int(random.randint(1,3))

  computer_choice = choice_list[random_number - 1]
  #player input line, and capitalize first letter to compare to choice list
  player_choice = input("Choose rock, paper, or scissors: ")
  player_choice = player_choice.lower().capitalize()
  #while loop to force player to choose a valid option of the 3 given
  while player_choice not in choice_list:
    player_choice = input("Not a valid option. Please choose rock, paper, or scissors: ")
    player_choice = player_choice.lower().capitalize()
  #if elif statments for each option in the game results; includes a win counter
  if player_choice == choice_list[0] and computer_choice == choice_list[1]:
    print("Paper beats rock. PC wins!")
    computer_wins.append("w")
    print("The PC has won: " + str(len(computer_wins)) + " times!")

  elif player_choice == choice_list[0] and computer_choice == choice_list[2]:
    print("Rock beats scissors. You win!")
    player_wins.append("w")
    print("You have won: " + str(len(player_wins)) + " times!")

  elif player_choice == choice_list[1] and computer_choice == choice_list[0]:
    print("Paper beats rock. You win!")
    player_wins.append("w")
    print("You have won: " + str(len(player_wins)) + " times!")

  elif player_choice == choice_list[1] and computer_choice == choice_list[2]:
    print("Scissors beats paper. PC wins!")
    computer_wins.append("w")
    print("The PC has won: " + str(len(computer_wins)) + " times!")

  elif player_choice == choice_list[2] and computer_choice == choice_list[0]:
    print("Rock beats scissors. PC wins!")
    computer_wins.append("w")
    print("The PC has won: " + str(len(computer_wins)) + " times!")

  elif player_choice == choice_list[2] and computer_choice == choice_list[1]:
    print("Scissors beats paper. You win!")
    player_wins.append("w")
    print("You have won: " + str(len(player_wins)) + " times!")

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
    rockpaperscissors()
  if player_rematch == "N":
    if len(player_wins) > len(computer_wins):
      print("The player won " + str(len(player_wins)) + " games, while the PC won only " + str(len(computer_wins)) + ".")
    elif len(player_wins) < len(computer_wins):
      print("The PC won " + str(len(computer_wins)) + " games, while you won only " + str(len(player_wins)) + ".")
    elif len(player_wins) == len(computer_wins):
      print("You and the PC won the same amount of games: " + str(len(player_wins)) + "!")
  #function call to initiate the program
rockpaperscissors()
