
from tkinter import *

def update_books(home,update_book):
    update_book.configure(background='black')
    Label(update_book,text='Issue Book',bg='black', fg='white', font=('Courier',35)).pack(pady=15)
    Label(update_book,text='Enter Book Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(update_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    update_book.pack(expand=1,fill = X)
    Button(update_book,text='Submit',command=lambda:detailed_update(update_book),bg='black', fg='white', font=('Courier',25)).pack(pady=12)
    home.pack_forget()
def detailed_update(update_book):
    Label(update_book,text='Name',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(update_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    Label(update_book,text='Author',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(update_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    Label(update_book,text='Category',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(update_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    Label(update_book,text='Count',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(update_book,height = 1,width = 30,font=('Courier',25)).pack()
    Button(update_book,text='update',bg='black', fg='white', font=('Courier',25)).pack(pady=12)
