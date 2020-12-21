from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk

import pymysql


class Login :
    def __init__(self , root) :
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")
        # self.root.resizable(False, False)

        # images
        self.bg = ImageTk.PhotoImage(file="images/reguserbck1.jpg")
        self.bg_image = Label(self.root , image=self.bg).place(x=0 , y=0 , relwidth=1 , relheight=1)

        # frame
        login_frame = Frame(self.root , bg="white smoke")
        login_frame.place(x=700 , y=150 , width=520 , height=350)

        # title
        title1 = Label(login_frame , text='User Login Here' , font=('Impact' , 30 , 'bold') , bg='white smoke' ,
                       fg='#08A3D2').place(x=90 , y=30)
        title2 = Label(login_frame , text='User Account Login Area' , font=('Goudy old style' , 15 , 'bold') ,
                       bg='white smoke' , fg='#d77337').place(x=90 , y=80)

        # body of user login
        lemail = Label(login_frame , text='Email ID' , font=("Goudy old style" , 15 , 'bold') , bg='white smoke' ,
                       fg='#d77337').place(x=90 , y=130)
        self.txt_email = Entry(login_frame , font=("times new roman" , 15) , bg='light gray')
        self.txt_email.place(x=90 , y=170 , width=350 , height=30)

        lpass = Label(login_frame , text='Password' , font=("Goudy old style" , 15 , 'bold') , bg='white smoke' ,
                      fg='#d77337').place(x=90 , y=210)
        self.txt_pass = Entry(login_frame , font=("times new roman" , 15) , bg='light gray')
        self.txt_pass.place(x=90 , y=250 , width=350 , height=30)

        forpass = Button(login_frame , text='Forget Password?' , command=self.forget_password_window ,
                         bg='white smoke' , fg='#d77337' , font=('times new roman' , 12) , bd=0).place(x=90 , y=290)
        or_register = Button(login_frame , text='or  Registration New Account?' , command=self.Register_window ,
                             bg='white smoke' , fg='#d77337' , font=('times new roman' , 12) , bd=0).place(x=205 ,
                                                                                                           y=290)
        login_btn = Button(self.root , text='Login' , command=self.login_data , bg='#d77337' , fg='white' ,
                           font=('times new roman' , 20) , bd=0).place(x=880 , y=480 , width=180 , height=40)

    def Register_window(self) :
        self.root.destroy()
        import user_register

    def reset(self) :
        self.txt_phone.delete(0 , END)
        self.txt_newpassword.delete(0 , END)
        self.txt_email.delete(0 , END)
        self.txt_pass.delete(0 , END)

    def forget_password(self) :
        if self.txt_phone.get() == "" or self.txt_newpassword.get() == "" :
            messagebox.showerror("Error" , "All fields are Required!!!" , parent=self.root2)
        else :
            try :
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
                cur = con.cursor()
                # cur2 = con.cursor()
                cur.execute("select * from user where email=%s and phone=%s" ,
                            (self.txt_email.get() , self.txt_phone.get()))
                # cur2.execute('select * from workermanage where email=%s',(self.txt_email.get()))
                row1 = cur.fetchone()
                # row2 = cur2.fetchone()
                # row = row1 + row2
                print(row1)
                if row1 == None :
                    messagebox.showerror("Error" , "Please Enter correct phone number" , parent=self.root2)
                else :
                    cur.execute("update user set password=%s where email=%s" ,
                                (self.txt_newpassword.get() , self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success' , "your password has been reset, Please Login With the New Password" ,
                                        parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es :
                messagebox.showerror("Error" , f"Error due to: {str(es)}" , parent=self.root)

    def forget_password_window(self) :
        if self.txt_email.get() == "" :
            messagebox.showerror("Error" , "Please Enter the Email ID to reset your password" , parent=self.root)
        else :
            try :
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
                cur = con.cursor()
                # cur2 = con.cursor()
                cur.execute("select * from user where email=%s" , (self.txt_email.get()))
                # cur2.execute('select * from workermanage where email=%s',(self.txt_email.get()))
                row1 = cur.fetchone()
                # row2 = cur2.fetchone()
                # row = row1 + row2
                print(row1)
                if row1 == None :
                    messagebox.showerror("Error" , "Please Enter the Valid Email ID to reset your password" ,
                                         parent=self.root)
                else :
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title('Forget Password')
                    self.root2.geometry("350x400+500+150")
                    self.root2.config(bg='crimson')
                    p1 = PhotoImage(file='images/key.png')
                    self.root2.iconphoto(False , p1)
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.resizable(False , False)
                    self.root2.passwr = PhotoImage(file='images/password.png')
                    self.root2.log = PhotoImage(file='images/login.png')
                    t = Label(self.root2 , text='Forget Password' , image=self.root2.log , compound=LEFT ,
                              font=('times new roman' , 20 , 'bold') , bg='crimson' , fg='#08A3D2').place(x=0 , y=30 ,
                                                                                                          relwidth=1)

                    phone = Label(self.root2 , text='Phone Number' , font=("times new roman" , 15 , "bold") ,
                                  bg='crimson' , fg='#08A3D2').place(x=110 , y=100)
                    self.txt_phone = Entry(self.root2 , font=('times new roman' , 15) , bg='white smoke')
                    self.txt_phone.place(x=50 , y=130 , width=250)

                    newpassword = Label(self.root2 , text='New Password' , font=("times new roman" , 15 , "bold") ,
                                        bg='crimson' , fg='#08A3D2').place(x=110 , y=170)
                    self.txt_newpassword = Entry(self.root2 , font=('times new roman' , 15) , bg='white smoke')
                    self.txt_newpassword.place(x=50 , y=200 , width=250)
                    login_btn = Button(self.root2 , text='Set Password' , image=self.root2.passwr , compound=RIGHT ,
                                       command=self.forget_password , bg='#d77337' , fg='white' ,
                                       font=('times new roman' , 20) , bd=0).place(x=80 , y=270 , width=200 , height=40)



            except Exception as es :
                messagebox.showerror("Error" , f"Error due to: {str(es)}" , parent=self.root)

    def login_data(self) :
        if self.txt_email.get() == "" or self.txt_pass.get() == "" :
            messagebox.showerror("Error" , "All fields are required!!" , parent=self.root)
        else :
            try :
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
                cur = con.cursor()
                cur2 = con.cursor()
                cur.execute("select * from user where email=%s and password=%s" ,
                            (self.txt_email.get() , self.txt_pass.get()))
                # cur2.execute('select * from workermanage where email=%s',(self.txt_email.get()))
                row1 = cur.fetchone()
                # row2 = cur2.fetchone()
                # row = row1 + row2
                # print(row)
                if row1 != None :
                    messagebox.showinfo("Success" ,
                                        f"Welcome {self.txt_email.get()}\n your password: {self.txt_pass.get()}" ,
                                        parent=self.root)
                    self.root2 = Toplevel()
                    self.root2.title("User home page")
                    self.root2.geometry('1350x700+0+0')
                    self.root2.config(bg='#08A3D2')
                    self.root2.focus_force()
                    title = Label(self.root2 , text='Admin for user' , bd=10 , relief=GROOVE ,
                                  font=('times new roman' , 40 , 'bold') , bg='cyan' , fg='blue')
                    title.pack(side=TOP , fill=X)

                    frame12 = Frame(self.root2 , bd=4 , bg='crimson')
                    frame12.place(x=0 , y=85 , width=109 , height=640)

                    self.home = ImageTk.PhotoImage(file='images/house.png')
                    btn = Button(frame12 , image=self.home , bg='crimson' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=0 , width=92 , height=100)
                    self.prof = ImageTk.PhotoImage(file='images/prof.png')
                    btn1 = Button(frame12 , image=self.prof , bg='crimson' , bd=5 ,
                                  relief=GROOVE , cursor='hand2').place(x=0 , y=104 , width=92 , height=100)
                    self.update = ImageTk.PhotoImage(file='images/update.png')
                    btn = Button(frame12 , image=self.update, bg='crimson' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=208 , width=92 , height=100)
                    self.logout = ImageTk.PhotoImage(file='images/logout.png')
                    btn = Button(frame12 , image=self.logout, bg='crimson' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=312 , width=92 , height=100)

                    self.frame22 = Frame(self.root2 , bd=4 , bg='white')
                    self.frame22.place(x=100 , y=85 , width=1250 , height=640)

                    self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
                    left = Label(self.frame22 , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,
                                                                                            height=608)

                    self.message = Label(self.frame22 , text=f'Welcome\t{str(self.txt_email.get())}' ,
                                         font=('times new roman' , 50 , 'bold') , bg='deep sky blue' ,
                                         fg='#d77337').place(x=200 , y=200)

                else :
                    messagebox.showerror("Error" , " user dose not exist" , parent=self.root)
                con.close()

            except Exception as es :
                messagebox.showerror("Error" , f"Error due to: {str(es)}" , parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()