# To Do List

tasks = []
while True:
    print("\n--- ToDoList ---")
    print("1. Add Task")
    print("2. Show Task")
    print("3. Exit")

    choice = input("Choose one thing: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Tasked Added {task}")
    elif choice == "2":
        print("\nYour Tasks")
        if not tasks:
            print("No tasks yet")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}...")
    elif choice == "3":
        print("Exiting Goodbye")
        break
    else:
        print("Invalid choice")
