import os
from colorama import Fore, Style, init # type: ignore

# Initialize colorama to enable colour formatting 
init(autoreset=True)

# A To Do List class to manage the tasks
class ToDoList:
    def __init__(self, file_name="tasks.txt"):
        self.tasks = []
        self.file_name = os.path.abspath("tasks.txt")
        self.load_tasks()

    # to load existing tasks from a file in memory
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    # to save tasks to a file
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    # to add a new task to the list and append it
    def add_task(self, task):
        if task.strip():
            self.tasks.append(task.strip())
            self.save_tasks()
            print(Fore.GREEN + f"Task '{task}' has been added successfully!")
        else:
            print(Fore.RED + "Task cannot be empty.")

    # to remove a task from the list by its index in the file
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(Fore.GREEN + f"Task '{removed_task}' has been removed successfully!")
        else:
            print(Fore.RED + "Invalid task number.")

    # to display all tasks in the list
    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks are currently available.")
        else:
            print(Fore.CYAN + "\nYour To-Do List is:")
            for i, task in enumerate(self.tasks, start=1):
                print(Fore.CYAN + f"{i}. {task}")

    # to clear all tasks from the list
    def clear_tasks(self):
        self.tasks.clear()
        self.save_tasks()
        print(Fore.GREEN + "All the tasks have been cleared!")

# a function to display the menu options available in to do list
def menu():
    print(Fore.MAGENTA + "\nTo-Do List Menu:")
    print(Fore.MAGENTA + "1. Add your task")
    print(Fore.MAGENTA + "2. Remove any task")
    print(Fore.MAGENTA + "3. View tasks")
    print(Fore.MAGENTA + "4. Clear All the tasks")
    print(Fore.MAGENTA + "5. Exit")

# main function to run the program
def main():
    to_do_list = ToDoList()

    while True:
        menu()  # Display menu options
        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))

            if choice == 1:
                # Add a new task
                task = input(Fore.BLUE + "Enter the task to add: ")
                to_do_list.add_task(task)
            elif choice == 2:
                # Remove a task by its number
                to_do_list.view_tasks()
                try:
                    index = int(input(Fore.BLUE + "Enter the task number to remove: ")) - 1
                    to_do_list.remove_task(index)
                except ValueError:
                    print(Fore.RED + "Please enter a valid choice.")
            elif choice == 3:
                # View all tasks
                to_do_list.view_tasks()
            elif choice == 4:
                # Clear all tasks
                to_do_list.clear_tasks()
            elif choice == 5:
                # Exit the program
                print(Fore.GREEN + "Exiting your To-Do List. Have a great day!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again !")

        except ValueError:
            print(Fore.RED + "Please enter a valid number !")

# Entry point of the program
if __name__ == "__main__":
    main()
