#user
from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
import requests
import pymysql

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")
        #self.root.resizable(False, False)

        # images
        self.bg = ImageTk.PhotoImage(file="images/reguserbck1.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #frame
        login_frame = Frame(self.root, bg="white smoke")
        login_frame.place(x=700, y=150, width=520, height=350)

        #title
        title1 = Label(login_frame, text='User Login Here', font=('Impact', 30, 'bold'), bg='white smoke', fg='#08A3D2').place(x=90, y=30)
        title2 = Label(login_frame, text='User Account Login Area', font=('Goudy old style', 15, 'bold'), bg='white smoke', fg='#d77337').place(x=90, y=80)

        # body of user login
        lemail = Label(login_frame, text='Email ID', font=("Goudy old style", 15, 'bold'), bg='white smoke',fg='#d77337').place(x=90, y=130)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg='light gray')
        self.txt_email.place(x=90, y=170 , width=350, height=30)

        lpass = Label(login_frame, text='Password', font=("Goudy old style" , 15 , 'bold') , bg='white smoke',fg='#d77337').place(x=90, y=210)
        self.txt_pass = Entry(login_frame , font=("times new roman" , 15), bg='light gray', show='*')
        self.txt_pass.place(x=90, y=250, width=350, height=30)

        forpass = Button(login_frame, text='Forget Password?', command=self.forget_password_window, bg='white smoke', fg='#d77337',font=('times new roman', 12), bd=0).place(x=90, y=290)
        or_register = Button(login_frame, text='or  Registration New Account?', command=self.Register_window, bg='white smoke', fg='#d77337',font=('times new roman', 12), bd=0).place(x=205, y=290)
        login_btn = Button(self.root, text='Login', command=self.login_data, bg='#d77337', fg='white', font=('times new roman', 20), bd=0).place(x=880, y=480, width=180,height=40)



    def Register_window(self):
        self.root.destroy()
        import user_register

    def reset(self):
        self.txt_phone.delete(0,END)
        self.txt_newpassword.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pass.delete(0,END)

    def forget_password(self):
        if self.txt_phone.get() == "" or self.txt_newpassword.get() == "":
            messagebox.showerror("Error", "All fields are Required!!!", parent=self.root2)
        else:
            try:
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
                cur = con.cursor()
                # cur2 = con.cursor()
                cur.execute("select * from user where email=%s and phone=%s" , (self.txt_email.get(), self.txt_phone.get()))
                # cur2.execute('select * from workermanage where email=%s',(self.txt_email.get()))
                row1 = cur.fetchone()
                # row2 = cur2.fetchone()
                # row = row1 + row2
                print(row1)
                if row1 == None :
                    messagebox.showerror("Error" , "Please Enter correct phone number" ,parent=self.root2)
                else:
                    cur.execute("update user set password=%s where email=%s", (self.txt_newpassword.get() , self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success',"your password has been reset, Please Login With the New Password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error" , f"Error due to: {str(es)}" , parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Please Enter the Email ID to reset your password", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ambu')
                cur = con.cursor()
                cur.execute("select * from user where email=%s", (self.txt_email.get()))
                row1 = cur.fetchone()
                print(row1)
                if row1 == None:
                    messagebox.showerror("Error" , "Please Enter the Valid Email ID to reset your password" ,parent=self.root)
                else:
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

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)




    def login_data(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ambu')
                cur = con.cursor()
                cur2 = con.cursor()
                cur.execute("select * from user where email=%s and password=%s", (self.txt_email.get(), self.txt_pass.get()))
                row1 = cur.fetchone()
                if row1 != None:
                    messagebox.showinfo("Success" , f"Welcome {self.txt_email.get()}\n your password: {self.txt_pass.get()}" , parent=self.root)
                    self.root3 = Toplevel()
                    self.root3.title("User Home Page")
                    self.root3.geometry('1350x700+0+0')
                    self.root3.config(bg='#08A3D2')
                    self.root3.focus_force()
                    self.image_dashbar = ImageTk.PhotoImage(file='images/amb2.png')
                    self.title_frame = Frame(self.root3, bd=10 , relief=GROOVE, bg='light sea green').place(x=0,y=0,height=85,width=1350)
                    title = Label(self.root3, text='Admin Details Report',image=self.image_dashbar,compound=RIGHT,
                                font=('times new roman' ,20, 'bold'), bg='light sea green' , fg='blue').place(x=600,y=10,height=60,width=500)
                    #title = Label(self.root3, text='Admin Details Report' , bd=10 , relief=GROOVE ,
                     #             font=('times new roman' , 40 , 'bold')  , bg='light sea green' , fg='blue')
                    #title.pack(side=TOP , fill=X)

                    frame12 = Frame(self.root3 , bd=4 , bg='deep sky blue')
                    frame12.place(x=0 , y=85 , width=109 , height=640)

                    self.home = ImageTk.PhotoImage(file='images/house.png')
                    btn = Button(frame12 , image=self.home , command=self.home_page , bg='light sea green' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=0 , width=92 , height=100)
                    self.prof = ImageTk.PhotoImage(file='images/prof.png')
                    btn1 = Button(frame12 , image=self.prof , command=self.profile_page , bg='light sea green' , bd=5 ,
                                  relief=GROOVE , cursor='hand2').place(x=0 , y=104 , width=92 , height=100)
                    self.update = ImageTk.PhotoImage(file='images/update.png')
                    btn = Button(frame12 , image=self.update, command=self.update_page, bg='light sea green' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=208 , width=92 , height=100)
                    self.request = ImageTk.PhotoImage(file='images/call.png')
                    btn = Button(frame12 , image=self.request, command=self.request_details , bg='light sea green' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=312 , width=92 , height=100)
                    self.logout = ImageTk.PhotoImage(file='images/logout.png')
                    btn = Button(frame12 , image=self.logout, command=self.logout_fn, bg='light sea green' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=416 , width=92 , height=100)

                    self.frame22 = Frame(self.root3, bd=4 , bg='white')
                    self.frame22.place(x=100 , y=85 , width=1250 , height=640)

                    self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
                    left = Label(self.frame22 , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,
                                                                                            height=608)

                else:
                    messagebox.showerror("Error", " user dose not exist", parent=self.root)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Password is invalid | Error due to: {str(es)}", parent=self.root)

    def home_page(self) :
        self.frame22 = Frame(self.root3 , bd=4 , bg='white')
        self.frame22.place(x=100 , y=85 , width=1250 , height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame22 , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 , height=608)

        self.message = Label(self.frame22,text=f'Welcome\t{str(self.txt_email.get())}', font=('times new roman' , 50 , 'bold') , bg='deep sky blue' , fg='#d77337').place(x=200 ,y=200)
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()
        print(cur.execute('select reqst_accept from request_accept '))
        row = cur.fetchone()
        if (row != None) and (row[0] == 'Accepted'):
            check = messagebox.askyesno('Success', r'Request has been Accepted', parent=self.root3)
            print(check)
            if check == True :
                self.request_details()
        else:
            pass



    def profile_page(self):
        profile_frame = Frame(self.frame22 , bd=4 , bg='white')
        profile_frame.place(x=220 , y=100 , height=400 , width=800)
        profile_frame2 = Frame(profile_frame , bd=4 , bg='white')
        profile_frame2.place(x=10 , y=320 , height=70 , width=770)

        self.profile = ImageTk.PhotoImage(file='images/user.png')
        p_frm = Label(profile_frame , image=self.profile , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=40 , y=60 , width=200 , height=250)

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()

        id = Label(profile_frame , text='ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        id.place(x=250 , y=60 , height=20 , width=70)
        id_txt = Entry(profile_frame, textvariable=self.id_var, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        id_txt.place(x=350 , y=60 , height=20 , width=130)

        name = Label(profile_frame , text='Name' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        name.place(x=510 , y=60 , height=20 , width=70)
        name_txt = Entry(profile_frame, textvariable=self.name_var, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        name_txt.place(x=610 , y=60 , height=20 , width=130)

        phone = Label(profile_frame , text='Phone Number' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        phone.place(x=300 , y=100 , height=20 , width=150)
        phone_txt = Entry(profile_frame, textvariable=self.email_var, font=('times new roman' , 13 , 'bold') , bd=0 , state='readonly')
        phone_txt.place(x=510 , y=100 , height=20 , width=150)

        email = Label(profile_frame , text='Email ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        email.place(x=250 , y=140 , height=20 , width=70)
        email_txt = Entry(profile_frame, textvariable=self.gender_var, font=('times new roman' , 12) , bd=0 ,justify=CENTER , state='readonly')
        email_txt.place(x=350, y=140 , height=20 , width=130)

        dob = Label(profile_frame , text='D O B' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        dob.place(x=510 , y=140 , height=20 , width=70)
        dob_txt = Entry(profile_frame, textvariable=self.phone_var, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        dob_txt.place(x=610 , y=140 , height=20 , width=130)

        gender = Label(profile_frame , text='Gender' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        gender.place(x=250 , y=180 , height=20 , width=70)
        gender_txt = Entry(profile_frame, textvariable=self.dob_var, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        gender_txt.place(x=350 , y=180 , height=20 , width=130)

        address = Label(profile_frame , text='Address' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        address.place(x=510 , y=180 , height=20 , width=70)
        address_txt = Entry(profile_frame, textvariable=self.address_var,font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        address_txt.place(x=610 , y=180 , height=20 , width=130)

        self.back_btn = ImageTk.PhotoImage(file='images/back.png')
        self.up_btn = Button(profile_frame , text="Update" , image=self.back_btn , command=self.home_page ,font=('times new roman' , 13 , 'bold') , bg='white' , bd=0)
        self.up_btn.place(x=700 , y=270 , height=40 , width=50)
        self.worker_table = ttk.Treeview(profile_frame2 ,
                                         column=('ID' , 'name' , 'email' , 'gender' , 'phone' , 'dob' , 'address'))
        self.worker_table.heading("ID" , text='ID')
        self.worker_table.heading("name" , text='name')
        self.worker_table.heading("email" , text='email')
        self.worker_table.heading("gender" , text='gender')
        self.worker_table.heading("phone" , text='phone')
        self.worker_table.heading("dob" , text='dob')
        self.worker_table.heading("address" , text='address')
        self.worker_table['show'] = 'headings'
        self.worker_table.column('ID' , width=100)
        self.worker_table.column('name' , width=100)
        self.worker_table.column('email' , width=100)
        self.worker_table.column('gender' , width=100)
        self.worker_table.column('phone' , width=100)
        self.worker_table.column('dob' , width=100)
        self.worker_table.column('address' , width=170)
        self.worker_table.pack(fill=BOTH , expand=1)
        self.worker_table.bind("<ButtonRelease-1>" , self.get_cursor)
        self.fetch_data()

    def update_page(self):
        update_frame = Frame(self.frame22 , bd=4 , bg='white')
        update_frame.place(x=220 , y=100 , height=400 , width=800)
        update_frame2 = Frame(update_frame , bd=4 , bg='white')
        update_frame2.place(x=10 , y=320 , height=70 , width=770)

        self.update_prf = ImageTk.PhotoImage(file="images/user.png")
        p_frm = Label(update_frame , image=self.update_prf , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=40 , y=60 , width=200 , height=250)

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()

        id = Label(update_frame , text='ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        id.place(x=250 , y=60 , height=20 , width=70)
        id_txt = Entry(update_frame, textvariable=self.id_var, font=('times new roman' , 13 , 'bold') , bd=0,justify=CENTER)
        id_txt.place(x=350 , y=60 , height=20 , width=130)

        name = Label(update_frame , text='Name' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        name.place(x=510 , y=60 , height=20 , width=70)
        self.name_txt = Entry(update_frame, textvariable=self.name_var, font=('times new roman' , 13 , 'bold') , bd=0,justify=CENTER)
        self.name_txt.place(x=610 , y=60 , height=20 , width=130)

        phone = Label(update_frame , text='Phone Number' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        phone.place(x=300 , y=100 , height=20 , width=150)
        phone_txt = Entry(update_frame, textvariable=self.email_var, font=('times new roman' , 13 , 'bold') , bd=0)
        phone_txt.place(x=510 , y=100 , height=20 , width=150)

        email = Label(update_frame , text='Email ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        email.place(x=250 , y=140 , height=20 , width=70)
        self.email_txt = Entry(update_frame, textvariable=self.gender_var, font=('times new roman' , 12) , bd=0 ,justify=CENTER)
        self.email_txt.place(x=350, y=140 , height=20 , width=130)

        dob = Label(update_frame , text='D O B' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        dob.place(x=510 , y=140 , height=20 , width=70)
        dob_txt = Entry(update_frame, textvariable=self.phone_var, font=('times new roman' , 13 , 'bold') , bd=0,justify=CENTER)
        dob_txt.place(x=610 , y=140 , height=20 , width=130)

        gender = Label(update_frame , text='Gender' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        gender.place(x=250 , y=180 , height=20 , width=70)
        gender_txt = Entry(update_frame, textvariable=self.dob_var, font=('times new roman' , 13 , 'bold') , bd=0 ,justify=CENTER)
        gender_txt.place(x=350 , y=180 , height=20 , width=130)

        address = Label(update_frame , text='Address' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        address.place(x=510 , y=180 , height=20 , width=70)
        address_txt = Entry(update_frame, textvariable=self.address_var,font=('times new roman' , 13 , 'bold') , bd=0 ,justify=CENTER)
        address_txt.place(x=610 , y=180 , height=20 , width=130)

        self.up_btn = Button(update_frame , text="Update" , command=self.update_data ,font=('times new roman' , 13 , 'bold') , bg='#B00857' , bd=0)
        self.up_btn.place(x=610 , y=270 , height=40 , width=70)

        r = requests.get('https://get.geojs.io/')

        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        ipAdd = ip_request.json()['ip']

        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        geo_request = requests.get(url)
        geo_data = geo_request.json()

        self.latitude = geo_data['latitude']
        self.longitude = geo_data['longitude']
        self.city = geo_data['city']
        self.state = geo_data['region']
        self.send_reqst = 'Requesting for Ambulance'

        btn_for_request = Button(update_frame, text='Request for Ambulance' , command=self.send_request,
                                 font=('times new roman',10, 'bold') , bd=5 , relief=GROOVE).place(x=350 , y=270)

        self.back_btn = ImageTk.PhotoImage(file='images/back.png')
        self.up_btn = Button(update_frame , text="Update" , image=self.back_btn, command=self.home_page ,font=('times new roman', 13, 'bold'), bg='white', bd=0)
        self.up_btn.place(x=700, y=270, height=40, width=50)
        self.worker_table = ttk.Treeview(update_frame2, column=('ID', 'name', 'email', 'gender', 'phone', 'dob', 'address'))
        self.worker_table.heading("ID" , text='ID')
        self.worker_table.heading("name" , text='name')
        self.worker_table.heading("email" , text='email')
        self.worker_table.heading("gender" , text='gender')
        self.worker_table.heading("phone" , text='phone')
        self.worker_table.heading("dob" , text='dob')
        self.worker_table.heading("address" , text='address')
        self.worker_table['show'] = 'headings'
        self.worker_table.column('ID' , width=100)
        self.worker_table.column('name' , width=100)
        self.worker_table.column('email' , width=100)
        self.worker_table.column('gender' , width=100)
        self.worker_table.column('phone' , width=100)
        self.worker_table.column('dob' , width=100)
        self.worker_table.column('address' , width=170)
        self.worker_table.pack(fill=BOTH , expand=1)
        self.worker_table.bind("<ButtonRelease-1>" , self.get_cursor)
        self.fetch_data()

    def update_data(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()
        cur.execute('update workermanage set name=%s,email=%s, gender=%s, phone=%s, dob=%s, address=%s where id=%s',
                                                                            (
                                                                               self.name_var.get() ,
                                                                               self.email_var.get() ,
                                                                               self.gender_var.get() ,
                                                                               self.phone_var.get() ,
                                                                               self.dob_var.get() ,
                                                                               self.address_var.get(),
                                                                               self.id_var.get()
                                                                               ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Success", "The Records are Updated successfully!!", parent=self.root3)

    def fetch_data(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()
        cur.execute("select * from user_info where email=%s",
                    (self.txt_email.get()))
        row = cur.fetchone()
        if row != 0 :
            self.worker_table.insert('' , END , values=row)
        con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.worker_table.focus()
        contents = self.worker_table.item(cursor_row)
        row = contents['values']
        #print(row)
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.phone_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_var.set(row[6])

    def send_request(self):
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
                cur = con.cursor()
                cur.execute("insert into request_accept (name,email,latitude,longitude,city,state,reqst_accept) values(%s,%s,%s,%s,%s,%s,%s)" ,
                            (self.name_txt.get(),
                             self.email_txt.get(),
                             self.latitude,
                             self.longitude,
                             self.city,
                             self.state,
                             self.send_reqst)
                            )
                con.commit()
                con.close()
                messagebox.showinfo("Success" , "Request Sent successful" , parent=self.root3)

    def request_details(self):
        self.requestf = Frame(self.root3 , bd=4 , bg='white')
        self.requestf.place(x=100 , y=85 , width=1250 , height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.requestf, image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,
                                                                                height=608)
        btn_delete = Button(self.requestf, text='patient admitted to hospital', command=self.delete_request,bg='crimson', font=('times new roman', 30, 'bold')).place(x=300,y=200)

    def delete_request(self):
        con = pymysql.connect(host='localhost', user='root', password='' , database='ambu')
        cur = con.cursor()
        print(cur.execute('delete from request_accept where email=%s', self.txt_email.get()))
        row = cur.fetchone()
        print(row)
        con.commit()
        con.close()
        messagebox.showinfo("Success", "The Patient admitted successfully!!", parent=self.root3)

    def clear(self):
        self.txt_email.delete(0, END)
        self.txt_pass.delete(0, END)

    def logout_fn(self) :
        self.root3.destroy()
        self.clear()
        self.root.focus_force()


root = Tk()
obj = Login(root)
root.mainloop()