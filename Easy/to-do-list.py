FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append("[] " + task)
    save_tasks(tasks)
    print("Task added!")



def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1 )
            save_tasks(tasks)
            print(f"your task '{removed}' have been succefully removed King")
        else:
            print("There is no task in that number ")
    
    except ValueError:
            print("king enter a valid number")


def tasks_marker():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter task to mark as done King:-"))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1].startswith("[✔]"):
                print("Task have been marked King, Keep grinding")
            else:
                tasks[task_num - 1 ] = tasks[task_num - 1].replace("[]" ,"[✔]", 1)
                save_tasks(tasks)
        else:
            print("invalid Task number King")

    except ValueError:
        print("Yo King enter a valid number")

def main():
    while True:
        print("///WELCOME TO KINGS TO DO LIST///")
        print("1.Add Tasks")
        print("2.View Tasks")
        print("3.Mark Tasks As Done")
        print("4.Remove")
        print("5.Exit")

        choice = input("Enter your choice King: ")
         


        if choice =="1":        
            add_task()

        elif choice =="2":
            view_tasks()

        elif choice =="3":
            tasks_marker()
        
        elif choice == "4":
            remove_task()

        elif choice == "5":
             print("Your exting the To Do List King, Stay Sharp")
             break
        else:
            print("That's an invalid option King, Hit the gym")


if __name__ == "__main__":
    main()