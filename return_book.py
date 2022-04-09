from tkinter import *
def return_books(home,return_book):
    return_book.configure(background='black')
    Label(return_book,text='Return Book',bg='black', fg='white', font=('Courier',35)).pack(pady=15)
    Label(return_book,text='Book Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(return_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    Label(return_book,text='Student Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(return_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    return_book.pack(expand=1,fill = X)
    Button(return_book,text='Submit',command=lambda:returnbook(),bg='black', fg='white', font=('Courier',25)).pack(pady=12)
    home.pack_forget()
def returnbook():
    return None
