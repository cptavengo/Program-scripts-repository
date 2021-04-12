#!/usr/bin/env python3

import random
import PySimpleGUI as sg

#initialize empty lists for win counter
computer_wins = []
player_wins = []

#function call to continuously loop when more games are desired
def rockpaperscissors():
  #setup various variables that are needed for different calls
  choice_list = ["Rock", "Paper", "Scissors"]
  random_number = int(random.randint(1,3))
  computer_choice = choice_list[random_number - 1]
  #create window that allows for selection
  layout = [[sg.Text("Choose rock, paper, or scissors")], [sg.Button("Rock")], [sg.Button("Paper")], [sg.Button("Scissors")]]
  window = sg.Window("Rock, paper, scissors 2.0!", layout)
  while True:
      event, values = window.read()
      if event == "Rock":
          player_choice = choice_list[0]
          break
      if event == "Paper":
          player_choice = choice_list[1]
          break
      if event == "Scissors":
          player_choice = choice_list[2]
          break
      if event == sg.WIN_CLOSED:
          break
  window.close()
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
  #ask player if they would like to go again; creates window for Y/N input
  yn_list = ["Y", "N"]
  ynlayout = [[sg.Text("Would you like to play again?")], [sg.Button("Yes")], [sg.Button("No")]]
  window = sg.Window("Play again?", ynlayout)
  while True:
      event, values = window.read()
      if event == "Yes":
          player_rematch = yn_list[0]
          break
      if event == "No":
          player_rematch = yn_list[1]
          break
      if event == sg.WIN_CLOSED:
          break
  window.close()
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