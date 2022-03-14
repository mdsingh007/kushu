import PySimpleGUI as sg
from dbops import select_all

sg.theme('DarkTeal2')   # Add a touch of color

btnSize = (6,1)
# # heading = 'Kchat'
friend_view = [ [sg.Text('Friends')], 
                [sg.Button('Kanha', size=btnSize)], 
                [sg.Button('Papa', size=btnSize)], 
                [sg.Button('Mama', size=btnSize)] ]
# message_view = [[sg.Text('Messages', size = (40, 1))]]

layout = [[sg.Output(size=(80, 20), key='-messages-')],
            [sg.Multiline(size=(70, 4), enter_submits=True, key='-text-'),
            sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
         ]]

window = sg.Window('Kchat', [[
        sg.Column(friend_view, key='-friend_view-'),
        sg.Column(layout, key='-message_view-')
        ]])


# while True:
#     event, values = window.read()
    # if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    #     break

# window.close()
buttons = ('Kanha', 'Papa', 'Mama')
    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
while True:
    event, values = window.read()

    if event == 'SEND':
        # print(values['-text-'])
        window['-text-'].update(value='')

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

    if event in buttons:
        for btn in buttons:
            window[btn].update(button_color=sg.theme_button_color())
        window[event].update(button_color='Grey')
        window['-messages-'].update(value='')

        for elem in buttons:
            if event == elem:
                allmsg = select_all()
                for msg in allmsg:
                    if msg[2] == elem and msg[3] == 'Kashvi':
                        print (f"{elem}: {msg[4]}")

        window.refresh()
    # print(event)
window.close()
