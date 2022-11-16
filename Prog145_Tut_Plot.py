import math
from matplotlib import pyplot as plt
import numpy as np

cars = eval(input("enter yourlist"))

data = eval(input("enter your score"))

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)

plt.show()

l1 = Label(win, text="Student Name", font=("verdana", 12, "bold"), borderwidth=5).grid(row=0, column=0, padx=20,
                                                                                           pady=100)
    t1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    t1.grid(row=0, column=1, padx=20, pady=100)

    l2 = Label(win, text="Student Class", font=("verdana", 12, "bold"), borderwidth=5).grid(row=1, column=0, padx=20,
                                                                                            pady=50)
    t2 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    t2.grid(row=1, column=1, padx=20, pady=50)

for student in my_conn:
    if student[1] == log2.get():
        for j in range(len(student)):
            e = Label(my_w, width=20, text=student[j], borderwidth=2, relief='ridge', anchor="w", fg='blue')
            e.grid(row=i, column=j)
    i = i + 1

#Success is the sum of small efforts, repeated day-in and day-out
    global task_list
    task_list = ''
    def newTask():
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            task_list + task
            my_entry.delete(0, "end")
            upd()

        else:
            messagebox.showwarning("Warning", "Please enter some task.")

    def deleteTask():
        lb.delete(ANCHOR)
        upd()

    def upd():
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        sql_select_Query = "SELECT * FROM STUDMARK"
        cursor = connection.cursor()
        val = log1.get()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print(records)
        for rows in records:
            if (rows[0] == val):
                task_list = list(rows[2])
            else:
                continue

        v = log1.get()
        sql_select_Query = "UPDATE STUDMARK SET TODO =%s WHERE EMAIL =%s"

        val = (task_list, v)
        cursor.execute(sql_select_Query, val)
        connection.commit()

    ws = Tk()
    ws.geometry('500x450+500+200')
    ws.title('ToDo List')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)
    frame = Frame(ws)
    frame.pack(pady=10)

    connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
    sql_select_Query = "SELECT * FROM STUDMARK"
    cursor = connection.cursor()
    val = log1.get()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for rows in records:
        if (rows[0] == val):
            task_list = rows[2]
            print(task_list)
        else:
            continue

    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none")
    lb.pack(side=LEFT, fill=BOTH)

    # task_list = ["Homework", "Study for Exam"]

    for item in task_list:
        lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    my_entry = Entry(ws, font=('times', 24))
    my_entry.pack(pady=20)

    button_frame = Frame(ws)
    button_frame.pack(pady=20)

    addTask_btn = Button(button_frame, text='Add Task', font=('times 14'),
                         bg='#c5f776', padx=20, pady=10, command=newTask
                         )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(button_frame, text='Delete Task', font=('times 14'),
                         bg='#ff8b61', padx=20, pady=10, command=deleteTask)
    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    exitTask_btn = Button(button_frame, text='Commit', font=('times 14'),
                          bg='#c4f413', padx=20, pady=10, command=upd)
    exitTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


    motivate1()
    ws.mainloop()
