from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk
import pymysql

def clear():
          emailEntry.delete(0,END)
          usernameEntry.delete(0,END)
          passwordEntry.delete(0,END)
          CpasswordEntry.delete(0,END)

def connect_database():
          if emailEntry.get()=='' or passwordEntry.get()=='' or usernameEntry.get()=='' or CpasswordEntry.get()=='':
                  messagebox.showerror('Error','All fields are required')
          elif emailEntry.get().isdigit():
                  messagebox.showerror('Error','Email should not have only numbers')
          elif emailEntry.get().isalpha():
                  messagebox.showerror('Error',"Email should not have only alphabets")
         #  elif  emailEntry.get()!='@':
                  # messagebox.showinfo('Error','Invalid Email Id')
          elif passwordEntry.get() != CpasswordEntry.get():
                   messagebox.showerror('Error','Password mismatched')
          elif check.get()==0:
                   messagebox.showerror('Error','Please accept Terms & Conditions')
          else:
                 try:
                    con=pymysql.connect(host='localhost',user='root',password='verkia@18komal')
                    mycursor=con.cursor()
                 except:
                    messagebox.showerror('Error','Database connectivity issue, Please try again later')
                    return
                 
                 try:
                    query='create database userdata'
                    mycursor.execute(query)
                    query='use userdata'
                    mycursor.execute(query)
                    query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
                    mycursor.execute(query)
                 except:  
                    mycursor.execute('use userdata')

                 query='select * from data where username=%s'
                 mycursor.execute(query,(usernameEntry.get()))

                 row=mycursor.fetchone()
                 if row !=None:
                    messagebox.showerror('Error','Username already exists')

                 else:
                    query='insert into data(email,username,password) values(%s,%s,%s)'
                    mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Registration is successful')
                    clear()
                    signup_window.destroy()
                    import signin

def login_page():
          signup_window.destroy()
          import signin

signup_window= tk.Tk()
signup_window.title("Signup Page")
signup_window.geometry("793x515+50+50")
signup_window.resizable(False,False)

img = ImageTk.PhotoImage(file ="background.jpg")
label_img = Label(signup_window,image=img, foreground= "white" )
label_img.grid()

frame=Frame(signup_window,bg='white') 
frame.place(x=456,y=45)

heading = Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light', 18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=7)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=26)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=26)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=26)

CpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
CpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
CpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
CpasswordEntry.grid(row=8,column=0,sticky='w',padx=26)

check=IntVar()
tc=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',8,'bold'),bg='white',activebackground='white',fg='firebrick1',activeforeground='firebrick1',variable=check)
tc.grid(row=9,column=0,sticky='w',padx=20,pady=10)

signupButton = Button(frame,text='Sign Up',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',bd=0,width=20,command=connect_database)
signupButton.grid(row=10,column=0,pady=10,padx=16)

ARHALabel=Label(frame,text='Already have an account??',font=('Open Sans',9),fg='black',bg='white')
ARHALabel.grid(row=11,column=0,sticky='w',padx=(12,0))

loginButton = Button(frame,text='Log in',font=('Open Sans',10,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='blue',cursor='hand2',bd=0,command=login_page)
loginButton.grid(row=11,column=0,padx=(75,0))

signup_window.mainloop()