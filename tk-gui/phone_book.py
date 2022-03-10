import PySimpleGUI as sg
from sqlite_database_pb import sql_fetch, new


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
listdata = sql_fetch()

layout2 = [  [sg.Text('Contacts')],
            [sg.Text('Name', size=(9, 1)), sg.InputText(key='-txtName-')],
            [sg.Text('Phone', size=(9, 1)), sg.InputText(key='-txtPhone-')],
            [sg.Text('Home Phone', size=(9, 1)), sg.InputText(key='-txtHphone-')],
            [sg.Text('Address', size=(9, 1)), sg.InputText(key='-txtAdd-')],
            [sg.Push(), sg.Button('Ok', size=(3, 1)), sg.Button('Cancel', size=(6, 1)), sg.Push()],
            ]

new_button = [[sg.Push(), sg.Button('New', size=(3, 1)), sg.Button('Edit'), sg.Push()]]
headings = ['id', 'Name', 'Phone', 'Home Phone','Address']
# print(listdata)
layout = new_button + [[sg.Table(listdata, headings=headings, key='-table-', enable_events=True)]]

# Create the Window
window = sg.Window('Phone Book', 
                [[
                    sg.Column(layout, key='listview'),
                    sg.Column(layout2, key='editview', visible=False)
                ]], 
                font='Courier 12'
            )

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Ok':
        new(values[0], values[1], values[2], values[3])
        window['-table-'].update(values=sql_fetch())
        window.refresh()
        window['listview'].update(visible=True)
        window['editview'].update(visible=False)
    if event == 'Edit':
        try:
            selrow = values['-table-'][0]
            print(listdata[selrow][0])
            window['listview'].update(visible=False)
            window['editview'].update(visible=True)
            window['-txtName-'].update(value=listdata[selrow][1])
            window['-txtPhone-'].update(value=listdata[selrow][2])
            window['-txtHphone-'].update(value=listdata[selrow][3])
            window['-txtAdd-'].update(value=listdata[selrow][4])
        except IndexError:
            print('Invalid input, try again')
    if event == 'New':
        window['listview'].update(visible=False)
        window['editview'].update(visible=True)
    if event == 'Cancel':
        window['listview'].update(visible=True)
        window['editview'].update(visible=False)
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print('You entered ', values)
    print(event)

window.close()
# print(abc)