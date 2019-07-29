"""
A program that stores book information

Title, Author, Year, ISBN

User can: 
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *
from backend import Database #on import, calls the functions!

database = Database("books.db")
def get_selected_row(event):
    try:
        global selected_tuple
        index = bookDisplay.curselection()[0]
        selected_tuple = bookDisplay.get(index)

        titleInput.delete(0, END)
        titleInput.insert(END, selected_tuple[1])
        authInput.delete(0, END)
        authInput.insert(END, selected_tuple[2])
        yearInput.delete(0, END)
        yearInput.insert(END, selected_tuple[3])
        isbnInput.delete(0, END)
        isbnInput.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    bookDisplay.delete(0,END)
    for row in database.view():
        bookDisplay.insert(END, row)

def search_command():
    bookDisplay.delete(0,END)
    for row in database.search(title_text.get(), auth_text.get(), year_text.get(), isbn_text.get()):
        bookDisplay.insert(END, row)

def insert_command():
    bookDisplay.delete(0,END)
    database.insert(title_text.get(), auth_text.get(), year_text.get(), isbn_text.get())
    for row in database.view():
        bookDisplay.insert(END, row)

def update_command():
    database.update(selected_tuple[0], title_text.get(), auth_text.get(), year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    database.delete(selected_tuple[0]) #passes id, first value in list
    view_command()

def close_command():
    window.destroy()

window = Tk()

window.wm_title("Book Store")

title = Label(window, text="Title")
title.grid(row=0, column=0)

title_text=StringVar()
titleInput = Entry(window, textvariable=title_text)
titleInput.grid(row=0, column=1)


auth = Label(window, text="Author")
auth.grid(row=0, column=2)

auth_text=StringVar()
authInput = Entry(window, textvariable = auth_text)
authInput.grid(row=0, column=3)

year = Label(window, text="Year")
year.grid(row=1, column=0)

year_text=StringVar()
yearInput = Entry(window, textvariable=year_text)
yearInput.grid(row=1, column=1)

isbn= Label(window, text="ISBN")
isbn.grid(row=1, column=2)
isbn_text = StringVar()
isbnInput = Entry(window, textvariable=isbn_text)
isbnInput.grid(row=1,column=3)

bookDisplay = Listbox(window, height=6, width=35)
bookDisplay.grid(row=2, column=0, rowspan=6, columnspan=2)

bookDisplayScroll = Scrollbar(window)
bookDisplayScroll.grid(row=2, column=2, rowspan=6)
bookDisplay.configure(yscrollcommand=bookDisplayScroll.set)
bookDisplayScroll.configure(command=bookDisplay.yview)

bookDisplay.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(window, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=3)
b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=close_command)
b6.grid(row=7, column=3)


window.mainloop()
