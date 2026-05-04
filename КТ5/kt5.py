from tkinter import *
from datetime import datetime

class ToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo")
        self.root.geometry('650x450')
        self.root.configure(bg='black')

        title_label = Label(
            self.root, 
            text="Мои текущие задачи", 
            font=("Times New Roman", 28, "bold"), 
            fg="yellow", 
            bg="black"
        )
        title_label.pack(pady=20)
        self.display_tasks()

    def display_tasks(self):
        tasks = []
        today = datetime.now().date()
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                        continue
                    
                date_str, task_name = line.split('/')
                    
                task_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                tasks.append((task_date, task_name))

        tasks.sort(key=lambda x: x[0])

        for task_date, task_name in tasks:
            avg = (task_date - today).days

            if avg < 0:
                text = f"Прошло {abs(avg)} от {task_name}"
                color = "#ff3333"
            elif avg == 0:
                text = f"Сейчас происходит {task_name}"
                color = "#ffcc00"
            else:
                text = f"Осталось {avg} до {task_name}"
                color = "#add8e6"

            lbl = Label(
                self.root, 
                text=text, 
                font=("Times New Roman", 14), 
                fg=color, 
                bg="black", 
                justify="left"
            )
            lbl.pack(anchor="w", padx=80, pady=2)

if __name__ == "__main__":
    main_window = Tk()
    app = ToDo(main_window)
    main_window.mainloop()