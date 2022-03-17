from socket import timeout
import PySimpleGUI as sg
from dbops import select_all, new

sg.theme('DarkTeal2')   # Add a touch of color

Users = ('Kashvi', 'Papa', 'Mama', 'Kanha', 'Stranger')
user = input('User name? ')
buttons = [x for x in Users if x != user]

btnSize = (6,1)
# # heading = 'Kchat'
# friend_view = [ [sg.Text('Friends')], 
#                 [sg.Button('Kanha', size=btnSize)], 
#                 [sg.Button('Papa', size=btnSize)], 
#                 [sg.Button('Mama', size=btnSize)] ]
# message_view = [[sg.Text('Messages', size = (40, 1))]]

friend_view = [[sg.Text('Friends')]]
for friend in buttons:
    friend_view.append([sg.Button(friend, size=btnSize)])

layout = [[sg.Output(size=(80, 20), key='-messages-')],
            [sg.Multiline(size=(70, 4), enter_submits=True, key='-text-'),
            sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
         ]]

window = sg.Window(f'Kchat: {user}', [[
        sg.Column(friend_view, key='-friend_view-'),
        sg.Column(layout, key='-message_view-')
        ]])


# while True:
#     event, values = window.read()
    # if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
    #     break

# window.close()

def update_chat_window(sender, receiver, window, force_update=False):
    global max_id
    if sender != None and receiver != None:
        allmsg = select_all()
        max_id2 = allmsg[-1][0]
        if max_id2 > max_id or force_update:

            window['-messages-'].update(value='')
            for id, dtime, s, r, msg in allmsg:
                if s == sender and r == receiver:
                    print (f"{sender}: {msg}")
                if s == receiver and r == sender:
                    print (f"{receiver}: {msg}")
                if r == user and s != sender and id > max_id:
                    window[f'{s}'].update(button_color='Yellow')
            max_id = max_id2

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
sender = None
receiver = None
max_id = 0

while True:
    event, values = window.read(timeout=1000)

    # let's refresh view
    update_chat_window(sender, receiver, window)

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

    if event in buttons:
        sel_btn = event
        for btn in buttons:
            window[btn].update(button_color=sg.theme_button_color())
        window[event].update(button_color='Grey')

        for elem in buttons:
            if event == elem:
                sender = elem
                receiver = user
                update_chat_window(sender, receiver, window, force_update=True)

    if event == 'SEND':
        new(user, sel_btn, values['-text-']) 
        print(f'{user}: {values["-text-"]}')
        window['-text-'].update(value='')


        window.refresh()
    # print(event)
window.close()
