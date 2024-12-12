#from functions import get_todos, show_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip().capitalize() + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        functions.show_todos()

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            new_todo = input("Enter new ToDo: ")
            todos[number - 1] = new_todo.strip().capitalize() + "\n"
            functions.write_todos(todos)
            functions.show_todos()
        except ValueError:
            print("Please select a number of ToDo to edit.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            functions.write_todos(todos)
            print(f"ToDo '{todo_to_remove}' was removed from the list.")
            functions.show_todos()
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Please select a number of ToDo to complete.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")