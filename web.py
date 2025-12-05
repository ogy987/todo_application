import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    # Clear the input box after adding
    st.session_state['new_todo'] = ""


st.title("Todo App")
st.subheader("This is todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# print("test")
# st.session_state
# streamlit run web.py --server.headless true