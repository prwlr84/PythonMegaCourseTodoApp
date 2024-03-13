from functions import *
import PySimpleGUI as pysg

label = pysg.Text('Type in a to do')
input_field = pysg.InputText(key='todo', tooltip='Enter to do')
add_button = pysg.Button('Add')
edit_button = pysg.Button('Edit')
display = pysg.Listbox(values=[t.strip('\n') for t in get_todos()], key='list',
                       enable_events=True, size=(45, 10))

layout = [[label],
          [input_field, add_button],
          [display, edit_button]]

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
            print(todos)
        case 'Edit':
            todos = get_todos()
            todos[todos.index(value['list'][0] + '\n')] = value['todo'] + '\n'
            write_todos(todos)
            window['list'].update(values=[t.strip('\n') for t in todos])
        case 'list':
            window['todo'].update(value=value['list'][0])
        case pysg.WINDOW_CLOSED:
            break


window.close()
