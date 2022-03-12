import PySimpleGUI as sg

layout = [[sg.Text('Welcome to Kchat!')]]

window = sg.Window('Kchat', 
    [[
        sg.Column(layout, key='listview')
    ]]
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

window.close()