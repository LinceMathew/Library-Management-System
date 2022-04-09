from tkinter import *

def add_books(home,add_book):
        add_book.configure(background='black')
        Label(add_book,text='Book Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
        Text(add_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
        Label(add_book,text='Name',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
        Text(add_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
        Label(add_book,text='Author',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
        Text(add_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
        Label(add_book,text='Category',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
        Text(add_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
        Label(add_book,text='Count',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
        Text(add_book,height = 1,width = 30,font=('Courier',25)).pack()
        Button(add_book,text='Submit',bg='black', fg='white', font=('Courier',25)).pack(pady=12)
        add_book.pack(expand=1,fill = X)
        home.pack_forget()
