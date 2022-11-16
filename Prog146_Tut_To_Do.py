def Open_window2():

    mycon = sqltor.connect(host='localhost', user='root', passwd='thuli@4132', database='TUT')
    if mycon.is_connected == False:
        print("Error connecting ")
    cursor = mycon.cursor()
    task_list=[]
    def newTask():
        task = my_entry.get()
        dat =''

        if task != "":
            lb.insert(END, task)
            task_list.append(my_entry)
            my_entry.delete(0, "end")
            for i in range(len(task_list)):
                dat = dat + " " + task_list(i)
            data = (ent,dat)
            insert_stmt = ("INSERT INTO TODO (EMAIL,TODOLIST) "
                           "VALUES(%s,%s)")
            cursor.execute(insert_stmt, data)

        else:
            messagebox.showwarning("Warning", "Please enter some task!")

    def deleteTask():
        a = lb.delete(ANCHOR)
        dlt_stmt = ("UPDATE TODO"
                    "SET TODOLIST = a"
                    "WHERE EMAIL = ent")
        cursor.execute(dlt_stmt)

    ws = Tk()
    ws.geometry('500x450+500+200')
    ws.title('ToDo List')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)

    frame = Frame(ws)
    frame.pack(pady=10)

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

    cursor.execute("CREATE TABLE IF NOT EXISTS TODO"
                   "(EMAIL varchar(20)"
                   "TODOLIST varchar(1000)")
    label_1 = Label(ws, text="Email", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    global ent
    ent = StringVar()
    Entry(ws, textvariable=ent).place(x=240, y=130)

    ws.mainloop()


def Open_window2():

    def newTask():
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter some task.")

    def deleteTask():
        lb.delete(ANCHOR)

    ws = Tk()
    ws.geometry('500x450+500+200')
    ws.title('ToDo List')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)

    frame = Frame(ws)
    frame.pack(pady=10)

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

    task_list = ["Homework", "Study for Exam"]

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
    motivate1()
    ws.mainloop()