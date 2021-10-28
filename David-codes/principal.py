import PySimpleGUI as sg

"""
    Demo Combo File Chooser - with clearable history
    
    This is a design pattern that is very useful for programs that you run often that requires
    a filename be entered.  You've got 4 options to use to get your filename with this pattern:
    1. Copy and paste a filename into the combo element
    2. Use the last used item which will be visible when you create the window
    3. Choose an item from the list of previously used items
    4. Browse for a new name
    
    To clear the list of previous entries, click the "Clear History" button.
    
    The history is stored in a json file using the PySimpleGUI User Settings APIs
    
    The code is as sparse as possible to enable easy integration into your code.

    Copyright 2021 PySimpleGUI
"""
dicionario = {"portugues":1,
                "matemática":0}
dicionario["zoo"] = 4
listad = sorted(dicionario.keys())
print(dicionario.keys)
layout = [[sg.Combo(listad, 
          default_value=listad[0], 
          size=(50, 1), key='-FILENAME-')],
          [sg.Button('Ok'),  sg.Button('Cancel')]]

window = sg.Window('Filename Chooser With History', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Ok':

        sg.popup(dicionario.get(values['-FILENAME-']))
    elif event == 'Clear History':
        window['-FILENAME-'].update(values=[], value='')

window.close()