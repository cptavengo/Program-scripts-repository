#!/usr/bin/env python3

import random
import PySimpleGUI as sg

def rockpaperscissorslizardspock():
    #setup various variables that are needed for different calls
    choice_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    player_wins = 0
    computer_wins = 0

    layout = [
    [sg.Text("Choose rock, paper, scissors, lizard, or Spock")],
    [sg.Button("Rock"), sg.Button("Paper"), sg.Button("Scissors"), sg.Button("Lizard"),
    sg.Button("Spock")],
    [sg.Text("Player wins:"), sg.Text(player_wins, k="-PLAYER-"), sg.Text("PC wins:"), sg.Text(computer_wins, k="-PC-")]
    ]

    window = sg.Window("", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Rock":
            random_number = int(random.randint(1,5))
            computer_choice = choice_list[random_number - 1]
            if computer_choice == choice_list[1]:
                sg.Popup("Paper covers rock. PC wins!", title=" ")
                computer_wins += 1

            elif computer_choice == choice_list[2]:
                sg.Popup("Rock crushes scissors. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[3]:
                sg.Popup("Rock crushes lizard. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[4]:
                sg.Popup("Spock vaporizes rock. PC wins!", title=" ")
                computer_wins += 1

            else:
                sg.Popup("Result is a tie!", title=" ")

            window["-PC-"].update(computer_wins)
            window["-PLAYER-"].update(player_wins)

        if event == "Paper":
            random_number = int(random.randint(1,5))
            computer_choice = choice_list[random_number - 1]
            if computer_choice == choice_list[0]:
                sg.Popup("Paper covers rock. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[2]:
                sg.Popup("Scissors cuts paper. PC wins!", title=" ")
                computer_wins += 1

            elif computer_choice == choice_list[3]:
                sg.Popup("Scissors decapitates lizard. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[4]:
                sg.Popup("Spock smashes scissors. PC wins!", title=" ")
                computer_wins += 1

            else:
                sg.Popup("Result is a tie!", title=" ")

            window["-PC-"].update(computer_wins)
            window["-PLAYER-"].update(player_wins)

        if event == "Scissors":
            random_number = int(random.randint(1,5))
            computer_choice = choice_list[random_number - 1]
            if computer_choice == choice_list[0]:
                sg.Popup("Rock crushes scissors. PC wins!", title=" ")
                computer_wins += 1

            elif computer_choice == choice_list[1]:
                sg.Popup("Scissors cuts paper. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[3]:
                sg.Popup("Scissors decapitates lizard. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[4]:
                sg.Popup("Spock smashes scissors. PC wins!", title=" ")
                computer_wins += 1

            else:
                sg.Popup("Result is a tie!", title=" ")

            window["-PC-"].update(computer_wins)
            window["-PLAYER-"].update(player_wins)

        if event == "Lizard":
            random_number = int(random.randint(1,5))
            computer_choice = choice_list[random_number - 1]
            if computer_choice == choice_list[0]:
                sg.Popup("Rock crushes lizard. PC wins!", title=" ")
                computer_wins += 1

            elif computer_choice == choice_list[1]:
                sg.Popup("Scissors decapitates lizard. PC wins!", title=" ")
                computer_wins += 1

            elif computer_choice == choice_list[2]:
                sg.Popup("Lizard eats paper. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[4]:
                sg.Popup("Lizard poisons Spock! You win!", title=" ")
                player_wins += 1

            else:
                sg.Popup("Result is a tie!", title=" ")

            window["-PC-"].update(computer_wins)
            window["-PLAYER-"].update(player_wins)

        if event == "Spock":
            random_number = int(random.randint(1,5))
            computer_choice = choice_list[random_number - 1]
            if computer_choice == choice_list[0]:
                sg.Popup("Spock vaporizes rock. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[1]:
                sg.Popup("Paper disproves Spock. PC wins!", title=" ")
                computer_wins += 1

            elif computer_choice == choice_list[2]:
                sg.Popup("Spock smashes scissors. You win!", title=" ")
                player_wins += 1

            elif computer_choice == choice_list[3]:
                sg.Popup("Lizard poisons Spock. PC wins!", title=" ")
                computer_wins += 1

            else:
                sg.Popup("Result is a tie!", title=" ")

            window["-PC-"].update(computer_wins)
            window["-PLAYER-"].update(player_wins)

if __name__ == "__main__":
    rockpaperscissorslizardspock()
