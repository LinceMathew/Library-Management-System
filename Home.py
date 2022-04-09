
from tkinter import *
from add_book import add_books





def home():
    main=Tk()
    main.title("Library")
    main.geometry("600x500")  
    main.configure(background='black')
    head= Label(main,text="Library Management System", bg='black', fg='white', font=('Courier',25))
    def goback():
        for widget in add_book.winfo_children():
            widget.destroy()
        home.pack(expand=1,fill=X)  
        add_book.pack_forget()
    Button(main,text='back',bg='black', fg='white', font=('Courier',25),command=goback).pack(pady=12,side=TOP, anchor=NW)
    head.pack(pady=20)
    home =Frame(main)
    add_book=Frame(main)
    def landing():
        home.configure(background='black')
        Text(home,height = 1,width = 30,font=('Courier',25)).pack(pady=18)
        Button(home,text='search',bg='black', fg='white', font=('Courier',25)).pack(pady=18)
        Button(home,text ="add book",command=lambda:add_books(home,add_book),bg='black', fg='white', font=('Courier',25)).pack(pady=18)
        Button(home,text='update book',bg='black', fg='white', font=('Courier',25)).pack(pady=18)
        Button(home,text='delete book',bg='black', fg='white', font=('Courier',25)).pack(pady=18)   
        Button(home,text='issue book',bg='black', fg='white', font=('Courier',25)).pack(pady=18)
        Button(home,text='return book',bg='black', fg='white', font=('Courier',25)).pack(pady=18)
        home.pack(expand=1,fill=X)
    
    
    
  

    landing()
    main.mainloop()  
home()


