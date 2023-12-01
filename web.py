import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todo(todos)


st.title("To Do App")

st.subheader("This is my To Do App")
st.write("This App helps to increase your Productivity")

todos = functions.get_todo()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter To Do", placeholder="Add new to do here...", on_change=add_todo, key="new_todo")


