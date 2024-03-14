from functions import *
import PySimpleGUI as pysg

pysg.theme('DarkPurple4')

label = pysg.Text('Type in a to do')
input_field = pysg.InputText(key='todo', tooltip='Enter to do')
add_button = pysg.Button(image_source='add.png', button_color='purple',
                         mouseover_colors='red', tooltip='button')
edit_button = pysg.Button('Edit')
complete_button = pysg.Button('Complete')
exit_button = pysg.Button('Exit')
display = pysg.Listbox(values=[t.strip('\n') for t in get_todos()], key='list',
                       enable_events=True, size=(45, 10))
message = pysg.Text(key='message')

layout = [[label],
          [input_field, add_button],
          [display, edit_button, complete_button],
          [exit_button, message]]

window = pysg.Window('ToDoApp',
                     layout=layout,
                     font=('Helvetice', 20))

while True:
    event, value = window.read()
    print(value)
    match event:
        case 'Add':
            todos = get_todos()
            if value['todo']:
                todos.append(value['todo'] + '\n')
                write_todos(todos)
            window['list'].update(values=[t.strip('\n') for t in todos])
        case 'Edit':
            try:
                todos = get_todos()
                todos[todos.index(value['list'][0] + '\n')] = value['todo'] + '\n'
                write_todos(todos)
                window['list'].update(values=[t.strip('\n') for t in todos])
            except IndexError:
                window['message'].update(value='Select an item first', text_color='red')
                continue
        case 'Complete':
            try:
                todos = get_todos()
                todos.pop(todos.index(value['list'][0] + '\n'))
                write_todos(todos)
                window['list'].update(values=[t.strip('\n') for t in todos])
                window['todo'].update(value='')
            except IndexError:
                pysg.Popup('Select an item first', font=('Helvetica', 20))
        case 'list':
            window['todo'].update(value=value['list'][0])
            window['message'].update(value='')
        case 'Exit':
            break
        case pysg.WINDOW_CLOSED:
            break


window.close()
