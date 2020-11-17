from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import pymysql

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")

        # images
        self.bg = ImageTk.PhotoImage(file="images/bck.jpg")
        self.user_icon = PhotoImage(file="images/login.png")
        self.password_icon = PhotoImage(file="images/key.png")
        self.login_icon = PhotoImage(file="images/user.png")

        self.uname=StringVar()
        self.upass=StringVar()
        bg_lb = Label(self.root , image=self.bg).pack()

        login_frame = Frame(self.root, bg="white smoke")
        login_frame.place(x=400, y=130, width=600, height=400)
        logolb = Label(self.root , image=self.login_icon,bg='deep sky blue' , bd=0).place(x=350, y=50)
        title = Label(login_frame,text='Login Here', font=('times new roman',30,'bold'),bg='white',fg='#08A3D2').place(x=200,y=30)




        lemail = Label(login_frame, text='Email ID', image=self.user_icon,compound=LEFT,font=("times new roman", 20, 'bold'),bg='white').place(x=50, y=130)
        self.txt_email = Entry(login_frame,font=("times new roman",15))
        self.txt_email.place(x=270, y=130, width=250)

        lpass = Label(login_frame, text='Password', image=self.password_icon,compound=LEFT,font=("times new roman", 20, 'bold'),bg='white').place(x=50, y=200)
        self.txt_pass = Entry(login_frame,font=("times new roman",15))
        self.txt_pass.place(x=270, y=200, width=250)

        btn_reg = Button(login_frame, text='Register new account?',cursor='hand2',command=self.Register_window,font=('times new roman', 12, 'bold'),bg='white smoke',bd=0, fg='#B00857').place(x=270, y=240)

        btn_log = Button(login_frame,text='Login', width=15, font=('times new roman', 14,'bold'),bg='#B00857',fg='white',cursor='hand2', command=self.login_data).place(x=270, y=300)

    def Register_window(self):
        self.root.destroy()
        import register

    def login_data(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ambu')
                cur = con.cursor()
                cur.execute("select * from worker where email=%s and password=%s", (self.txt_email.get(), self.txt_pass.get()))
                row = cur.fetchone()
                print(row)
                if row != None:
                    messagebox.showinfo("Success" , "Log in is successful" , parent=self.root)

                else:
                    messagebox.showerror("Error" , " user dose not exist" , parent=self.root)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()