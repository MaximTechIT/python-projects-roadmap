



todos = [
    {
        "id": 1,
        "task": "Learn Python ",
        "completed": False
    },

    {
        "id": 2,
        "task": "Learn JavaScript",
        "completed": False
    }
]




def add_task():


    todos.append()

    


def show_tasks():
    
    for i in todos:

        print(i["task"])

        print("_________")


while True:

    print(" 1. Показать задачи\n 2. Добавить задачу \n 3. Удалить задачу \n 4. Выполнить задачу \n 5. Выйти")

    choice = int(input("Введите ваш выбор: "))

    if choice == 1:

        show_tasks()
        

    elif choice == 2:
        
        pass
        
    
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        pass



