import tkinter as tk
from PIL import ImageTk
# from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql

#functionality
# def clear():
#     usernameEntry.delete(0,END)
#     passwordEntry.delete(0,END)

def forget_password():
        def change_password():
            if user_entry.get()=='' or Npassword_entry.get=='' or Confirmpassword_entry.get=='':
                messagebox.showerror('Error','All fields are required',parent=window)
            elif Npassword_entry.get()!=Confirmpassword_entry.get():
                messagebox.showerror('Error','Password and Confirm password are not same!!',parent=window)
            else:
                con=pymysql.connect(host='localhost',user='root',password='verkia@18komal',database='userdata')
                mycursor=con.cursor()
                query='select * from data where username=%s'
                mycursor.execute(query,(user_entry.get()))
                row=mycursor.fetchone()
                if row==None:
                      messagebox.showerror('Error','Incorrect username',parent=window)
                else:
                      query='update data set password =%s where username =%s'
                      n_pass=Npassword_entry.get()
                      username=user_entry.get()
                      mycursor.execute(query,(n_pass,username))
                      con.commit()
                      con.close()
                      messagebox.showinfo('Success','Password is reset, please login woth new password',parent=window)
                      window.destroy()
        

        window = Toplevel()
        window.title('Change Password')

        bgPic = ImageTk.PhotoImage(file='background.jpg')
        bglabel = Label(window,image=bgPic)
        bglabel.grid()

        heading_label = Label(window,text='RESET PASSWORD',font=('arial', 19,'bold'),bg='white',fg='magenta2')
        heading_label.place(x=480,y=60)

        user_label = Label(window,text='Username',font=('arial', 13,'bold'),bg='white',fg='orchid1')
        user_label.place(x=470,y=108)
        
        user_entry = Entry(window,width=25,font=('arial',10),bd=0,fg='magenta2')
        user_entry.place(x=475,y=130)
        
        Frame(window,width=260,height=2,bg='orchid1').place(x=475,y=149)

        Npassword_label = Label(window,text='New Password',font=('arial', 13,'bold'),bg='white',fg='orchid1')
        Npassword_label.place(x=470,y=178)

        Npassword_entry = Entry(window,width=25,font=('arial',10),border=0,fg='magenta2')
        Npassword_entry.place(x=475,y=200)

        Frame(window,width=260,height=2,bg='orchid1').place(x=475,y=219)

        Confirmpassword_label = Label(window,text='Confirm Password',font=('arial', 13,'bold'),bg='white',fg='orchid1')
        Confirmpassword_label.place(x=470,y=248)
        
        Confirmpassword_entry = Entry(window,width=25,font=('arial',10),border=0,fg='magenta2') 
        Confirmpassword_entry.place(x=475,y=270)
        
        Frame(window,width=260,height=2,bg='orchid1').place(x=475,y=289)

        RPButton = Button(window,text='Change Password',font=('Open Sans',16,'bold'),fg='white',bg='magenta2',activebackground='magenta2',activeforeground='white',cursor='hand2',bd=0,width=20,command=change_password)
        RPButton.place(x=472,y=340)

        window.mainloop()

file ="home.html"
def login_user():
        if usernameEntry.get()=='' or passwordEntry=='':
             messagebox.showerror('Error','All fields are required')
        
        else:
             try:
                con=pymysql.connect(host='localhost',user='root',password='verkia@18komal')
                mycursor=con.cursor()
             except:
                messagebox.showerror('Error','Connection is not established')
                return
             
             query='use userdata'
             mycursor.execute(query)
             query='select * from data where username=%s and password=%s'
        #      username=usernameEntry.get()
        #      password=passwordEntry.get()
        #      mycursor.execute(query,(username,password))
             mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
             row=mycursor.fetchone()
             if row==None:
                messagebox.showerror('Error','Invalid username or password')
             else:
                messagebox.showinfo('Welcome','Login is successful')
                # return(file)
def signup_page():
        login_window.destroy()
        import signup1

def user_enter(HI):
        if usernameEntry.get()=='Username':
                usernameEntry.delete(0,END)

def password_enter(JI):
        if passwordEntry.get()=='Password':
                passwordEntry.delete(0,END)

def hide():
        openeye.config(file='closeye.png')
        passwordEntry.config(show='*')
        eyeButton.config(command=show)

def show():
        openeye.config(file='openeye.png')
        passwordEntry.config(show='')
        eyeButton.config(command=hide)


# login_window = Toplevel()
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("793x515+50+50")
login_window.resizable(False,False)

#forimage
img = ImageTk.PhotoImage(file ="background.jpg")
label_img = Label(login_window,image=img, foreground= "white" )
label_img.place(x=0,y=0 )

#heading
heading = Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light', 20,'bold'),bg='white',fg='firebrick1')
heading.place(x=520,y=60)

#username
usernameEntry = Entry(login_window,width=19,font=('Microsoft Yahei UI Light', 15,'bold'),border=0,fg='firebrick1')
usernameEntry.insert(0,'Username')
usernameEntry.place(x=480,y=120)

usernameEntry.bind('<FocusIn>',user_enter)
Frame(login_window,width=250,height=2,bg='firebrick1' ).place(x=480,y=148)

#password
passwordEntry = Entry(login_window,width=19,font=('Microsoft Yahei UI Light', 15,'bold'),border=0,fg='firebrick1')
passwordEntry.insert(0,'Password')
passwordEntry.place(x=480,y=190)
passwordEntry.bind('<FocusIn>',password_enter)
Frame(login_window,width=250,height=2,bg='firebrick1' ).place(x=480,y=218)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window,image=openeye,border=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=700,y=189 )

forgetButton = Button(login_window,text="Forgot Password??",border=0,bg='white',font=('Microsoft Yahei UI Light', 7,'bold'),fg='firebrick1',activeforeground='firebrick1',activebackground='white',cursor='hand2',command=forget_password)
forgetButton.place(x=632,y=220 )

loginButton = Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',bd=0,width=20,command=login_user)
loginButton.place(x=472,y=264)

orLabel=Label(login_window,text='------------------OR------------------',font=('Open Sans',16,'bold'),fg='firebrick1',bg='white')
orLabel.place(x=460,y=332)

facebook_logo=PhotoImage(file='facebook.png')
flogo=Button(login_window,image=facebook_logo,border=0,bg='white',activebackground='white',cursor='hand2')
flogo.place(x=545,y=385)

google_logo=PhotoImage(file='google.png')
glogo=Button(login_window,image=google_logo,border=0,bg='white',activebackground='white',cursor='hand2')
glogo.place(x=591,y=385)

twitter_logo=PhotoImage(file='twitter.png')
tlogo=Button(login_window,image=twitter_logo,border=0,bg='white',activebackground='white',cursor='hand2')
tlogo.place(x=634,y=385)

dhaLabel=Label(login_window,text="Don't have an account??",font=('Open Sans', 9,'bold'),fg='firebrick1',bg='white')
dhaLabel.place(x=468,y=440)

newAButton = Button(login_window,text='Create New account',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='blue',cursor='hand2',bd=0,command=signup_page)
newAButton.place(x=614,y=440)


login_window.mainloop()
