import PySimpleGUI as sg
import os.path
import os
import sys
import re
import io
from PIL import Image

def main():
    #defines layout for first window of module
    layout = [[sg.Text("Would you like to rename photos?"),
             sg.Checkbox("Yes", key="-YES-"), sg.Checkbox("No", k="-NO-")],
             [sg.Text("Are multiple folders needed for renaming?"),
             sg.Checkbox("Yes", k="-YES_1-"), sg.Checkbox("No", k="-NO_1-")],
             #[sg.Text("Keep folders after upload?"),
             #sg.Checkbox("Yes", k="-YES2-"), sg.Checkbox("No", k="-NO2-")],
             [sg.Button("OK")],
             ]

    window = sg.Window(" ", layout)

    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        if event == "OK":
            #defines what happens for first row of checkboxes
            if values["-YES-"] == True and values["-NO-"] == False:
                if values["-YES_1-"] == True and values["-NO_1-"] == False:
                    window.close()
                    #return values["-YES_1-"], values["-NO_1-"]
                    photo_folder_selector(values["-YES_1-"], values["-NO_1-"])
                if values["-NO_1-"] == True and values["-YES_1-"] == False:
                    window.close()
                    photo_folder_selector(values["-YES_1-"], values["-NO_1-"])
                    #return values["-YES_1-"], values["-NO_1-"]
                if values["-NO_1-"] == True and values["-YES_1-"] == True:
                    sg.popup("Please on select yes or no.")
            if values["-NO-"] == True and values["-YES-"] == False:
                print("You selected no")
                window.close()
            if values["-NO-"] == True and values["-YES-"] == True:
                sg.popup("Please on select yes or no.")

def input_field_check(input_field):
    """Helper function to perform input field checks against all spaces and illegal characters"""
    #This checks to make sure that the input is not blank or spaces
    if input_field.isspace() == True or input_field == "":
        sg.popup("The file field cannot be empty", title = " ")
        return True
    #This checks for invalid file characters
    if input_field.find("<") != -1 or input_field.find(">") != -1 \
        or input_field.find(":") != -1 or input_field.find("\\") != -1 \
        or input_field.find("/") != -1 or input_field.find("\"") != -1 \
        or input_field.find("|") != -1 or input_field.find("?") != -1 \
        or input_field.find("*") != -1:
            sg.popup("The following characters cannot be used:"
                "< > : \ / \" | ? * ")
            return True
    else:
        return False

def photo_folder_selector(yes_values, no_values):
    #defines photo folder layout
    layout = [[sg.Text("Select folder for photos to be renamed"),
              sg.In(enable_events=True, key="-FOLDER-"),
              sg.FolderBrowse()], [sg.Button("OK")],
             ]
    window = sg.Window(" ", layout)

    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            sys.exit()
        elif event == "-FOLDER-":
            #This takes the folder field and lists all the files in the
            #folder selected
            folder = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []

        elif event == "OK":
            #This checks to make sure that the folder field is not empty and
            #then calls the next function when done
            if values["-FOLDER-"].isspace() == True or values["-FOLDER-"] == "":
                sg.popup("The folder field cannot be empty", title =" ")
            else:
                if no_values == True and yes_values == False:
                    window.close()
                    photo_renamer(file_list, folder)
                    #return file_list, folder
                if yes_values == True and no_values == False:
                    window.close()
                    #return file_list, folder
                    multiple_photo_folders(file_list, folder)


def mass_renamer(list_files, folder):
    layout = [
    [sg.Text("Input name to be mass labeled:")],
    [sg.In(enable_events=True, key="-IN-"), sg.Button("OK")],
    ]
    window = sg.Window(" ", layout)

    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        if event == "OK":
            if input_field_check(values["-IN-"]) == True:
                pass
            else:
                try:
                    count = 1
                    for file in list_files:
                        regex = r"(\.\w+)$"
                        file_extension = re.search(regex, file)
                        file_extension.groups()
                        if values["-IN-"].endswith(file_extension[0]) == True:
                            filename = os.path.join(folder + "\\" + file)
                            values["-IN-"] = values["-IN-"].replace(file_extension[0], "")
                            new_file = values["-IN-"] + "(" + str(count) + ")" + file_extension[0]
                            new_filename = os.path.join(folder, new_file)

                            if new_file in os.listdir(folder):
                                sg.popup("This name is already in use")
                            else:
                                os.rename(filename, new_filename)
                                file_list = os.listdir(folder)
                                new_fnames = [
                                    f
                                    for f in file_list
                                    if os.path.isfile(os.path.join(folder,f))
                                    and f.lower().endswith((".png", ".jpg", ".jpeg"))
                                ]
                                window.close()
                                return new_fnames
                        else:
                            filename = os.path.join(folder + "\\" + file)
                            new_file = values["-IN-"] + "(" + str(count) + ")" + file_extension[0]
                            new_filename = os.path.join(folder, new_file)

                            if new_file in os.listdir(folder):
                                sg.popup("This name is already in use")
                            else:
                                os.rename(filename, new_filename)
                                file_list = os.listdir(folder)
                                new_fnames = [
                                    f
                                    for f in file_list
                                    if os.path.isfile(os.path.join(folder,f))
                                    and f.lower().endswith((".png", ".jpg", ".jpeg"))
                                ]
                                window.close()
                                return new_fnames
                        count += 1

                except:
                    sg.popup("Something screwed up")

def photo_renamer(file_list, folder):
    #This sets up what will be on the left side of the window
    photo_column = [[sg.Text("Select photo to be renamed")],
              [sg.Listbox(values=file_list, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
              enable_events=True, size=(40,20),key="-FILE LIST-")]]
    #This sets up what will be on the right side of the window
    viewer_column = [
        [sg.Image(key="-IMAGE-")],
        [sg.Text("New photo name:")],
        [sg.In(key="-INPUT-", do_not_clear=False), sg.Button("OK")],
        [sg.Button("Mass rename"), sg.Button("Done")],
    ]
    #This sets up the window with a vertical line seperating the two sections
    layout = [
        [
            sg.Column(photo_column),
            sg.VSeperator(),
            sg.Column(viewer_column),
        ]
    ]
    #This creates a list of files that end in the file extensions shown;
    #this is reused a few times
    for f in file_list:
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
    #This creates the new window, finalize makes it so that it doesn't throw
    #a warning when the window gets updated
    window = sg.Window(" ", layout, finalize=True)
    window["-FILE LIST-"].update(fnames)

    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            sys.exit()
        elif event == "-FILE LIST-":
            #The following block of code converts the picture from its original
            #size to a viewable thumbnail, while storing it in memory
            #The original file is unmodified during this conversion
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
            if input_field_check(values["-INPUT-"]) == True:
                pass
            else:
                #This sets up a check to verify the file name is not in use,
                #and the searches the input field to see if the file extension
                #was typed there. If it was, it only uses the input field, else
                #it adds the file_extension from the original file.
                try:
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
                        new_filename = os.path.join(folder, values["-INPUT-"]
                        + file_extension[0])
                        os.rename(filename, new_filename)
                        file_list = os.listdir(folder)
                        fnames = [
                            f
                            for f in file_list
                            if os.path.isfile(os.path.join(folder,f))
                            and f.lower().endswith((".png", ".jpg", ".jpeg"))
                            ]
                        window["-FILE LIST-"].update(fnames)
                except:
                    #exception block to verify unique names and to select a
                    #photo to begin renaming.
                    if values["-INPUT-"] in file_list or values["-INPUT-"] + file_extension[0] in file_list:
                        sg.popup("This name is already in use", title = " ")
                    else:
                        sg.popup("Please select a file from the left", title = " ")
        if event == "Mass rename":
            list_files = values["-FILE LIST-"]
            window["-FILE LIST-"].update(mass_renamer(list_files, folder))
        if event == "Done":
            print("This function is being added soon.",
                  "The function may also be disabled in the script.")

def multiple_photo_folders(file_list, folder):
    #define layout for folder creation Window
    layout = [[sg.Text("How many folders need to be created?"),
             sg.Input("", k ="-IN-")],
             [sg.Button("OK")]]
    window = sg.Window(" ", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "OK":
            if values["-IN-"].strip().isdigit() != True:
                sg.popup("Please enter a number")
            else:
                window.close()
                #for loop iterates to max value input in folders desired field
                for folder_num in range(int(values["-IN-"])):
                    layout_1 = [[sg.Text("Folder {} name:".format(folder_num + 1)),
                               sg.Input("", k ="-IN_1-")],
                               [sg.Button("OK")]]
                    window_1 = sg.Window(" ", layout_1)
                    #creates each folder in a separate window, one at a time
                    while True:
                        event_1, values_1 = window_1.read()
                        if event_1 == "Exit" or event_1 == sg.WIN_CLOSED:
                            break
                        if event_1 == "OK":
                            if input_field_check(values_1["-IN_1-"]) == True:
                                pass
                            else:
                                try:
                                    if values_1["-IN_1-"] in os.listdir(folder):
                                        sg.popup("Name already in use, choose another")
                                    else:
                                        window_1.close()
                                        os.mkdir(folder + "/" + values_1["-IN_1-"])
                                except:
                                    sg.popup("An error has occurred")
            photo_renamer(file_list, folder)

if __name__ == "__main__":
    main()

##TO DO: need to add a way to seperate photos to new folders
#add a "Done" button to final window so that function can move on to upload
#possibly add a file conversion or resizer ability, if desired
#   ^ this would be good if file sizes need to be reduced to under x MB
