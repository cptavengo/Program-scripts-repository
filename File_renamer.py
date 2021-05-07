import PySimpleGUI as sg
import os.path
import os
import sys
import re
import io
from PIL import Image

def photo_yes_no():
    layout = [[sg.Text("Would you like to rename photos?")],
              [sg.Button("Yes"), sg.Button("No")],
             ]

    window = sg.Window(" ", layout)

    while True:
        event, values = window.read()
        if event == "Yes":
            window.close()
            photo_folder_selector()
        elif event == "No":
            print("You selected no")
            window.close()
        if event == sg.WIN_CLOSED:
            break

def photo_folder_selector():
    layout = [[sg.Text("Select folder for photos to be renamed"),
              sg.In(enable_events=True, key="-FOLDER-"),
              sg.FolderBrowse()],[sg.Button("OK")],
             ]
    window = sg.Window(" ", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
        elif event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []

        elif event == "OK":
            if values["-FOLDER-"].isspace() == True or values["-FOLDER-"] == "":
                sg.popup("The folder field cannot be empty", title = " ")
            else:
                window.close()
                photo_renamer(file_list, folder)

    return file_list, folder

def photo_renamer(file_list, folder):
    photo_column = [[sg.Text("Select photo to be renamed")],
              [sg.Listbox(values=file_list, enable_events=True, size=(40,20),
              key="-FILE LIST-")]]
    viewer_column = [
        [sg.Image(key="-IMAGE-")],
        [sg.Text("New photo name:")],
        [sg.In(enable_events=True, key="-INPUT-"), sg.Button("OK")],
    ]

    layout = [
        [
            sg.Column(photo_column),
            sg.VSeperator(),
            sg.Column(viewer_column),
        ]
    ]
    for f in file_list:
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
    window = sg.Window(" ", layout, finalize=True)
    window["-FILE LIST-"].update(fnames)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
        elif event == "-FILE LIST-":
            try:
                filename = os.path.join(
                    folder, values["-FILE LIST-"][0]
                )
                image = Image.open(filename)
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
            except:
                pass
        if event == "OK":
            if values["-INPUT-"].isspace() == True or values["-INPUT-"] == "":
                sg.popup("The file field cannot be empty", title = " ")
            else:
                regex = r"(\.\w+)$"
                file_extension = re.search(regex, values["-FILE LIST-"][0])
                file_extension.groups()
                if values["-INPUT-"].endswith(file_extension[0]) == True:
                    new_filename = os.path.join(folder, values["-INPUT-"])
                    os.rename(filename, new_filename)
                    file_list = os.listdir(folder)
                    fnames = [
                        f
                        for f in file_list
                        if os.path.isfile(os.path.join(folder,f))
                        and f.lower().endswith((".png", ".jpg", ".jpeg"))
                        ]
                    window["-FILE LIST-"].update(fnames)
                else:
                    new_filename = os.path.join(folder, values["-INPUT-"] + file_extension[0])
                    os.rename(filename, new_filename)
                    file_list = os.listdir(folder)
                    fnames = [
                        f
                        for f in file_list
                        if os.path.isfile(os.path.join(folder,f))
                        and f.lower().endswith((".png", ".jpg", ".jpeg"))
                        ]
                    window["-FILE LIST-"].update(fnames)
photo_yes_no()
