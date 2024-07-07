tasks = []

print("You are entered into the ToDoList Application!")
print("Your Available commands: add, update, delete, complete, view, quit")

while True:
    command = input("Enter a command: ").strip().lower()

    if command == "add":
        task = input("Enter the task: ").strip()
        if task:
            tasks.append({"task": task, "completed": False})
            print(f"Task '{task}' added.")
        else:
            print("You must enter a task.")
    
    elif command == "update":
        try:
            index = int(input("Enter the task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter the new task description: ").strip()
                if new_task:
                    tasks[index]["task"] = new_task
                    print(f"Task {index + 1} updated to '{new_task}'.")
                else:
                    print("You must enter a new task description.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("You must enter a valid number.")

    elif command == "delete":
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(task):
                deleted_task = tasks.pop(index)
                print(f"Task '{deleted_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("You must enter a valid number.")
    
    elif command == "complete":
        try:
            index = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print(f"Task {index + 1} marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("You must enter a valid number.")

    elif command == "view":
        if tasks:
            for i, task in enumerate(tasks):
                status = "✓" if task["completed"] else "✗"
                print(f"{i + 1}. {task['task']} [{status}]")
        else:
            print("No tasks found.")
    
    elif command == "quit":
        print("Exiting the To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid command. Available commands: add, update, delete, complete, view, quit")
