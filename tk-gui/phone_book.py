from multiprocessing.sharedctypes import Value
import PySimpleGUI as sg
from sqlite_database_pb import sql_fetch, new, edit, delete


# sg.theme('Default')   # Add a touch of color
# All the stuff inside your window.
# listdata = sql_fetch()

layout2 = [  [sg.Text('Contacts')],
            [sg.Text('Name', size=(9, 1)), sg.InputText(key='-txtName-')],
            [sg.Text('Phone', size=(9, 1)), sg.InputText(key='-txtPhone-')],
            [sg.Text('Home Phone', size=(9, 1)), sg.InputText(key='-txtHphone-')],
            [sg.Text('Address', size=(9, 1)), sg.InputText(key='-txtAdd-')],
            [sg.Push(), sg.Button('Ok', size=(3, 1)), sg.Button('Cancel', size=(6, 1)), sg.Push()],
            ]

new_button = [[sg.Button('New', size=(3, 1)), sg.Button('Edit'), sg.Button('Delete'), sg.Push(), sg.Button('Filter'), sg.InputText(key='-Search-', size=(10, 1))]]
headings = ['ID', 'Name', 'Phone', 'Home Phone','Address']
layout = new_button + [[sg.Table(sql_fetch(), headings=headings,
                                key='-table-', 
                                enable_events=True, 
                                # display_row_numbers = True,
                                visible_column_map=[False, True, True, True, True])]]

# Create the Window
window = sg.Window('Phone Book', 
                [[
                    sg.Column(layout, key='listview'),
                    sg.Column(layout2, key='editview', visible=False)
                ]], 
            )

# Event Loop to process "events" and get the "values" of the inputs
is_edit = False
while True:
    event, values = window.read()
    window['-Search-'].update(value = '')
    if event == 'Ok':
        if is_edit:
            selrow = values['-table-'][0]
            id = window['-table-'].Values[selrow][0]
            edit(id, values['-txtName-'], values['-txtPhone-'], values['-txtHphone-'], values['-txtAdd-'])
        else:
            new(values['-txtName-'], values['-txtPhone-'], values['-txtHphone-'], values['-txtAdd-'])
        window['-table-'].update(values=sql_fetch())
        window.refresh()
        window['listview'].update(visible=True)
        window['editview'].update(visible=False)
    if event == 'Edit':
        is_edit = True
        try:
            selrow = values['-table-'][0]
            record = window['-table-'].Values[selrow]

            window['listview'].update(visible=False)
            window['editview'].update(visible=True)
            window['-txtName-'].update(value=record[1])
            window['-txtPhone-'].update(value=record[2])
            window['-txtHphone-'].update(value=record[3])
            window['-txtAdd-'].update(value=record[4])
        except IndexError:
            print('Invalid input, try again')
    if event == 'New':
        is_edit = False
        window['-txtName-'].update(value='')
        window['-txtPhone-'].update(value='')
        window['-txtHphone-'].update(value='')
        window['-txtAdd-'].update(value='')
        window['listview'].update(visible=False)
        window['editview'].update(visible=True)
    if event == 'Cancel':
        window['listview'].update(visible=True)
        window['editview'].update(visible=False)
    if event == 'Delete':
        try:
            selrow = values['-table-'][0]
            id = window['-table-'].Values[selrow][0]
            delete(id)
            window['-table-'].update(values=sql_fetch())
            window.refresh()
        except IndexError:
            print('Invalid input, try again')
    if event == 'Filter':
        window['-table-'].update(values=sql_fetch(values['-Search-']))
        window.refresh()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print(f'Event -> {event}, \nvalues -> {values}')

window.close()