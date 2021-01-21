from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
class Home:
    def __init__(self, root):
        
        self.root = root
        self.root.title('Home window')
        self.root.geometry("1350x700+0+0")
        #self.root.focus_force()

        self.bg = ImageTk.PhotoImage(file="images/amb.jpg")
        ttk.bg_bg = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.register_page()


    def register_page(self):

        self.fetch = 1
        self.frame12 = Frame(self.root, bd=4,relief=GROOVE, bg='light sea green').place(x=200,y=100,width=400,height=500)
        register = Label(self.frame12,text="Registration form", font=("times new roman" , 20 , "bold"),bg="light sea green", bd=5).place(x=290,y=200)
        ttk.btn = Button(self.frame12 , text="Register" , command=self.register_page ,
                     font=("times new roman" , 10 , "bold") , bd=5 , relief=GROOVE , state='active').place(
            x=250 , y=110 , width=150)
        ttk.btn = Button(self.frame12, text="Login" , command=self.login_page , font=("times new roman" , 10 , "bold") ,
                     bd=5 , relief=GROOVE).place(
            x=400 , y=110 , width=150)
        self.cmb_Box = ttk.Combobox(self.frame12 , font=('times new roman' , 15) , state='readonly' , justify=CENTER)
        self.cmb_Box['values'] = ("SELECT" , "Worker Registration" , "User Registration" , "Admin Registration")
        self.cmb_Box.place(x=275, y=270 , width=250)
        self.cmb_Box.current(0)

        ttk.btn_select = Button(self.frame12, text="Select" , command=self.select, font=("times new roman" , 10 , "bold") ,
                     bd=5 , relief=GROOVE).place(
            x=320 , y=400 , width=150)

    def login_page(self):

        self.fetch = 2
        self.frame22 = Frame(self.root, bd=4,relief=GROOVE, bg='light sea green').place(x=200,y=100,width=400,height=500)
        login = Label(self.frame22,text="Login form", font=("times new roman" , 20 , "bold"),bg="light sea green", bd=5).place(x=320,y=200)
        btn = Button(self.frame22, text="Register" , command=self.register_page ,
                     font=("times new roman" , 10 , "bold") , bd=5 , relief=GROOVE , state='active').place(
            x=250 , y=110 , width=150)
        btn = Button(self.frame22 , text="Login" , command=self.login_page , font=("times new roman" , 10 , "bold") ,
                     bd=5 , relief=GROOVE).place(
            x=400 , y=110 , width=150)
        self.cmb_Box = ttk.Combobox(self.frame22, font=('times new roman' , 15) , state='readonly' , justify=CENTER)
        self.cmb_Box['values'] = ("SELECT" , "Worker Login" , "User Login" , "Admin Login")
        self.cmb_Box.place(x=275, y=270 , width=250)
        self.cmb_Box.current(0)

        btn_select = Button(self.frame22 , text="Select" , command=self.select ,
                            font=("times new roman" , 10 , "bold") ,
                            bd=5 , relief=GROOVE).place(
            x=320 , y=400 , width=150)

    def select(self):
        if self.fetch == 1:
            #print(self.cmb_Box.get())
            if self.cmb_Box.get()=="Worker Registration":
                self.root.destroy()
                import worker_register

            elif self.cmb_Box.get()=="User Registration":
                self.root.destroy()
                import user_register
            else:
                self.root.destroy()
                import Hostpital_registration

        elif self.fetch == 2:
            if self.cmb_Box.get() == "Worker Login" :
                self.root.destroy()
                import worker_login

            elif self.cmb_Box.get() == "User Login" :
                self.root.destroy()
                import user_login
            else:
                self.root.destroy()
                import hospital_login





root = Tk()
obj = Home(root)
root.mainloop()