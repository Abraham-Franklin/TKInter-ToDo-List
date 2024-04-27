from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("750x600+750+250")

        self.todo_label = Label(self.root, text="Todo List", bg="red", fg="white", font="ariel, 25 bold")
        self.todo_label.pack(side=TOP, fill=BOTH)

        self.list_entry = Entry(self.root, width=38, font=("Ariel", 16))
        self.list_entry.place(x=55, y=75)

        def onadditem():
            item = self.list_entry.get()
            with open("datas.txt", 'a') as file:
                file.write(item)
                file.seek(0)
                file.close()
            self.event_lists.insert(END, item)
            self.list_entry.delete(0, END)

        self.addbtn = Button(self.root, text="Add Task", bg="red", fg="white", activeforeground="red", activebackground="white", command=onadditem)
        self.addbtn.place(x=600, y=75)

        self.event_lists = Listbox(self.root, width=49, height=13, font=("Ariel", 15))
        self.event_lists.place(x=55, y=120)

        def displayitems():
            with open("datas.txt", 'r') as fs:
                events = fs.readlines()
                for event in events:
                    self.event_lists.insert(END, event)
                    fs.close()
        displayitems()

        def ondeleteitem():
            item_selection = self.event_lists.curselection()
            if item_selection:
                index = item_selection[0]
                item_to_delete = self.event_lists.get(index)
                with open("datas.txt", 'r') as file:
                    datas_read = file.readlines()
                with open("datas.txt", 'w') as file:
                    for line in datas_read:
                        if line.strip() != item_to_delete:
                            file.write(line)
                self.event_lists.delete(index)


        self.deletebtn = Button(self.root, text="Delete Item", width=68, bg="red", fg="white", activeforeground="red", activebackground="white", command=ondeleteitem)
        self.deletebtn.place(x=54, y=490)
                    


def main():
    root = Tk()
    TodoInstance = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()