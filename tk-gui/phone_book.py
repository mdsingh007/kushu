import PySimpleGUI as sg
from sqlite_database_pb import sql_fetch, new


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout2 = [  [sg.Text('Contacts')],
            [sg.Text('Name', size=(9, 1)), sg.InputText()],
            [sg.Text('Phone', size=(9, 1)), sg.InputText()],
            [sg.Text('Home Phone', size=(9, 1)), sg.InputText()],
            [sg.Text('Address', size=(9, 1)), sg.InputText()],
            [sg.Push(), sg.Button('Ok', size=(3, 1)), sg.Button('Cancel', size=(6, 1)), sg.Push()],
            ]

headings = ['Name', 'Phone', 'Home Phone','Address']
new_button = [[sg.Push(), sg.Button('New', size=(3, 1)), sg.Push()]]
header =  [[sg.Text(h, size=(14,1), text_color='red') for h in headings]]
# input_rows = [[[for elem in range(4): sg.Input(size=(15,1), pad=(0,0)), sg.Button('Edit', size=(5, 1))] for col in range(4)] for row in range(10)]
def create_view_layout():
    input_rows = []
    table = sql_fetch()
    for ct in table:
        row = []
        for col in range(4):
            row.append(sg.Text(ct[col+1], size=(15,1), pad=(0,0)))
        row.append(sg.Button('Edit'))

        input_rows.append(row)
    
    return input_rows

layout = new_button + header + create_view_layout()
# layout = create_view_layout(new_button, header)
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
        create_view_layout()
        window['listview'].update(visible=True)
        window['editview'].update(visible=False)
        # print('You entered ', values)    
        # pass
    if event == 'New':
        window['listview'].update(visible=False)
        window['editview'].update(visible=True)
    if event == 'Cancel':
        window['listview'].update(visible=True)
        window['editview'].update(visible=False)
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    # print('You entered ', values)
    # print(event)

window.close()
# print(abc)