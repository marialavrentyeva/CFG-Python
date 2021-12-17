new_item = input("What is there to do? ")

with open ('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open ('todo.txt', 'r') as todo_file:
        todo_file.write(todo)
