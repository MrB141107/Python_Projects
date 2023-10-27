# Create an empty list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def list_tasks():
    if tasks:
        print("Tasks in the to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the to-do list.")

def remove_task(task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def todo_list():
    print("Welcome to the To-Do List application!")

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_index = input("Enter the task number to remove: ")
            remove_task(task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    todo_list()
