import streamlit as st
from functions import *

todos = get_todos()


def add_todo():
    todo = st.session_state['add_input']
    todos.append(todo + '\n')
    write_todos(todos)


def remove_todo():
    keys = list(filter(st.session_state.get, st.session_state))
    todos.pop(int(keys[0].strip('chb')))
    write_todos(todos)


st.title('To Do App')
st.subheader('This is my To Do App')
st.write('An app to enhance productivity')

for i, t in enumerate(todos):
    st.checkbox(t.strip('\n'), key=f'chb{i}', on_change=remove_todo)

st.text_input('', placeholder='Add new todo...',
              on_change=add_todo, key='add_input')
