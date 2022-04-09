from tkinter import *
def delete_books(home,delete_book):
    delete_book.configure(background='black')
    Label(delete_book,text='Delete Book',bg='black', fg='white', font=('Courier',35)).pack(pady=15)
    Label(delete_book,text='Enter Book Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(delete_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    delete_book.pack(expand=1,fill = X)
    Button(delete_book,text='Submit',command=lambda:delete(),bg='black', fg='white', font=('Courier',25)).pack(pady=12)
    home.pack_forget()

def delete():
    return None

