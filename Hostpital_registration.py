from tkinter import *
from PIL import Image, ImageTk
# ImageTK is used to deals with jpg files
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import *

class HosRegister:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Window')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')
        self.root.focus_force()

        # image file
        self.bg = ImageTk.PhotoImage(file="images/bck.jpg")
        bg = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # left image file

        self.left = ImageTk.PhotoImage(file="images/hospital.png")
        left = Label(self.root, image=self.left, bg='steel blue').place(x=80, y=100, width=400, height=500)

        # register frame
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text='ADMIN REGISTER HERE', font=("times new roman", 20, "bold"), bg='white', fg='green').place(x=50,y=30)

        #---------------------------------Row1

        name = Label(frame1, text='Name', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=50, y=100)
        self.txt_name = Entry(frame1, font=('times new roman', 15), bg='white smoke')
        self.txt_name.place(x=50, y=130, width=250)

        phone = Label(frame1, text='Phone Number', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=370, y=100)
        self.txt_phone = Entry(frame1, font=('times new roman', 15), bg='white smoke')
        self.txt_phone.place(x=370, y=130, width=250)

        # ---------------------------------Row2
        email = Label(frame1, text='Email ID', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=50, y=170)
        self.txt_email = Entry(frame1, font=('times new roman', 15), bg='white smoke')
        self.txt_email.place(x=50, y=200, width=250)

        # ---------------------------------Row4
        password = Label(frame1, text='Password', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=50, y=240)
        self.txt_password = Entry(frame1, font=('times new roman', 15), bg='white smoke')
        self.txt_password.place(x=50, y=270, width=250)

        cpassword = Label(frame1, text='Confirm Password', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=370, y=240)
        self.txt_cpassword = Entry(frame1, font=('times new roman', 15), bg='white smoke')
        self.txt_cpassword.place(x=370, y=270, width=250)

        #-----------------------------------Terms
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions",variable=self.var_chk, onvalue=1, bg='white', font=('times new roman', 12)).place(x=50, y=320)

        # registration button
        btn_register = Button(frame1, text="Register",font=('times new roman', 15), bg='red', fg='SteelBlue1',bd=0, cursor='hand2', command=self.register_data).place(x=50, y=420, width=100)
        btn_login = Button(self.root, text="Sign In",font=('times new roman', 15), bg='SpringGreen3', fg='SteelBlue', bd=0, cursor='hand2', command=self.Login_window).place(x=220, y=480, width=130)


    def Login_window(self):
        self.root.destroy()
        #import worker

    def clear(self):
        self.txt_name.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0 , END)
        self.var_chk = 0

    def register_data(self):

        if self.txt_name.get()=="" or self.txt_phone.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","password and confirm password should be same",parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root',password='', database='ambulance')
                cur = con.cursor()
                cur2 = con.cursor()
                cur.execute("select * from admin where email=%s", self.txt_email.get())
                row = cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error", "User Already Exist, please try with another email", parent=self.root)
                    self.clear()
                else:
                        cur.execute("insert into admin (name,phone,email,password) values(%s,%s,%s,%s)",
                                    (
                                       self.txt_name.get(),
                                       self.txt_phone.get(),
                                       self.txt_email.get(),
                                       self.txt_password.get()
                                    ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Registration is successful", parent=self.root)
                        self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root = Tk()
obj = HosRegister(root)
root.mainloop()