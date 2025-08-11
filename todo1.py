#to do list app
with open("task.txt", "a") as file:
    pass
#a function to add task
def add_task(task):
    with open("task.txt", "a") as file:
        file.write(task + "\n")

# a function to view task
def view_tasks():
    with open("task.txt", "r") as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")

# a function to edit task
def edit_task(index, new_task):
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= index < len(tasks):
        tasks[index] = new_task + "\n"
        with open("task.txt", "w") as file:
            file.writelines(tasks)
            
 # a function to delete task
def delete_task(index):
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= index < len(tasks):
        tasks.pop(index)
        with open("task.txt", "w") as file:
            file.writelines(tasks)
            
#main function   
def main():
    while True:
        print("\n Todo List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to edit: ")) - 1
            new_task = input("Enter new task: ")
            edit_task(index, new_task)
        elif choice == "4":
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
main()

