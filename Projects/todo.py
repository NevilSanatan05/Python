# Simple To-Do List App

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task['done'] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")

def mark_done():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]['done'] = True
        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\n--- To-Do Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
