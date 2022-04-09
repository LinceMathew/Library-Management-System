from tkinter import *
def issue_books(home,issue_book):
   
    issue_book.configure(background='black')
    Label(issue_book,text='Issue Book',bg='black', fg='white', font=('Courier',35)).pack(pady=15)
    Label(issue_book,text='Book Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(issue_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    Label(issue_book,text='Student Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(issue_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    Label(issue_book,text='return date',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    Text(issue_book,height = 1,width = 30,font=('Courier',25)).pack(pady=5)
    issue_book.pack(expand=1,fill = X)
    Button(issue_book,text='Submit',command=lambda:issue(),bg='black', fg='white', font=('Courier',25)).pack(pady=12)
    home.pack_forget()
def issue():
    return None