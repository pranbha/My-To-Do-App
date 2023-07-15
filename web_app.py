import streamlit as st
import todos_functions

todos = todos_functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todos_functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("Hello")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        todos_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun

st.text_input(label = "", placeholder = "Add new to-do....", on_change = add_todo, key = "new_todo")