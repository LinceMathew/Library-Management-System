
from tkinter import *

from black import out
from connect_db import connect
from tkinter import messagebox
import pymysql
def update_books(home,update_book):
    update_book.configure(background='black')
    Label(update_book,text='Update Book',bg='black', fg='white', font=('Courier',35)).pack(pady=15)
    Label(update_book,text='Enter Book Id',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    id=Text(update_book,height = 1,width = 30,font=('Courier',25))
    id.pack(pady=5)
    update_book.pack(expand=1,fill = X)
    Button(update_book,text='Submit',command=lambda:queryby_id(id,update_book),bg='black', fg='white', font=('Courier',25)).pack(pady=12)
    home.pack_forget()
def detailed_update(update_book,output):
    Label(update_book,text='Name',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    name=Text(update_book,height = 1,width = 30,font=('Courier',25))
    name.pack(pady=5)
    Label(update_book,text='Author',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    author=Text(update_book,height = 1,width = 30,font=('Courier',25))
    author.pack(pady=5)
    Label(update_book,text='Category',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    category=Text(update_book,height = 1,width = 30,font=('Courier',25))
    category.pack(pady=5)
    Label(update_book,text='Total Count',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    t_count=Text(update_book,height = 1,width = 30,font=('Courier',25))
    t_count.pack()
    Label(update_book,text='Available Count',bg='black', fg='white', font=('Courier',25)).pack(pady=5)
    a_count=Text(update_book,height = 1,width = 30,font=('Courier',25))
    a_count.pack()
    display_details(name,author,category,t_count,a_count,output)
    Button(update_book,text='update',bg='black', fg='white', font=('Courier',25)).pack(pady=12)
    
def queryby_id(id,update_book):
    book_id=id.get(1.0, "end-1c")
    query="select * from Books where book_id="+book_id
    try:
        result=connect(query)
        output=fetch_detail(result)
        messagebox.showinfo("Success","enter new book details")
        detailed_update(update_book,output)
    except(pymysql.Error, pymysql.Warning) as e:
        err=str(e)
        messagebox.showinfo("Error","Can't add data into Database "+err)

def display_details(name,author,category,t_count,a_count,output):
    name.insert(INSERT,output[0])
    author.insert(INSERT,output[1])
    category.insert(INSERT,output[2])
    t_count.insert(INSERT,output[3])
    a_count.insert(INSERT,output[4])

def fetch_detail(result):
    for row in result:
        name=row[1]
        author=row[2]
        cat_id=row[3]
        t_count=row[4]
        avail_count=row[5]
    return [name,author,cat_id,t_count,avail_count]


