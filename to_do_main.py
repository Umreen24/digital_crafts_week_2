
from task_class import Task

user_input = ""
to_do = [] 

while user_input != "q":

    if user_input == "1":
        
        name = input("Enter task: ")
        priority = input("Enter high, medium, or low priority: ")

        tasks = Task(name, priority)
        to_do.append(tasks)
        
        with open("tasks.txt", "a") as file_object:
            file_object.write(f"{name} -- {priority} \n")
    
    elif user_input == "3":
        
        for index in range(0, len(to_do)):
            print(f"{index +1} - {to_do[index].name} - {to_do[index].priority}")

    elif user_input == "2":

        for index in range(0, len(to_do)):
            print(f"{index +1} - {to_do[index].name} - {to_do[index].priority}")
        
        delete_task = int(input("Enter the number of the task you would like to delete: "))

        def task_to_delete():
            del to_do[delete_task -1]
        
        task_to_delete()

    user_input = input("Press 1 to create a task, press 2 to delete a task, press 3 to view all tasks, or press q to quit! ")