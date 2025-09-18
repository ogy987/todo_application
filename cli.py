# from functions import get_todos, write_todos
import functions # module
import time # module

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos.append(todo + '\n')

        functions.write_todos(todos,"todos.txt")

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # Remove break line in console output
        new_todos = [item.strip('\n') for item in todos]

        # Remove break line in console output (another approach)
        # new_todos = []
        # for item in todos:
        #     item = item.strip('\n')
        #     new_todos.append(item)

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, "todos.txt")
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, "todos.txt")

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There isn't index with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Oops! You have entered the wrong command.")

print("Bye!")