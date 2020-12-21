#worker
from tkinter import *
from tkinter import ttk, messagebox         # where ttk is used to scrolling in table or creating a table
from PIL import Image, ImageTk              # importing images
import pymysql                              # pymysql is used to connect to mysql database
import requests
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")
        self.root.focus_force()
        # images
        self.bg = ImageTk.PhotoImage(file="images/bck.jpg")
        self.user_icon = PhotoImage(file="images/login.png")
        self.password_icon = PhotoImage(file="images/key.png")
        self.login_icon = PhotoImage(file="images/user.png")

        # ----------background image--------
        bg_lb = Label(self.root , image=self.bg).pack()

        # -----------creating a frame----------
        login_frame = Frame(self.root, bg="white smoke")
        login_frame.place(x=400, y=130, width=600, height=400)
        logolb = Label(self.root , image=self.login_icon,bg='deep sky blue' , bd=0).place(x=350, y=50)
        title = Label(login_frame,text='Worker Login Here', font=('times new roman',30,'bold'),bg='white smoke',fg='#08A3D2').place(x=150,y=30)



        # -------------label and entry for email---------
        lemail = Label(login_frame, text='Email ID', image=self.user_icon,compound=LEFT,font=("times new roman", 20, 'bold'),bg='white').place(x=50, y=130)
        self.txt_email = Entry(login_frame,font=("times new roman", 15))
        self.txt_email.place(x=270, y=130, width=250)

        # -------------label and entry for password---------
        lpass = Label(login_frame, text='Password', image=self.password_icon,compound=LEFT,font=("times new roman", 20, 'bold'),bg='white').place(x=50, y=200)
        self.txt_pass = Entry(login_frame, font=("times new roman", 15), show='*')
        self.txt_pass.place(x=270, y=200, width=250)

        # ----------registration button---------
        btn_reg = Button(login_frame, text='Register new account?',cursor='hand2',command=self.Register_window,font=('times new roman', 12, 'bold'),bg='white smoke',bd=0, fg='#B00857').place(x=270, y=240)

        # ----------login button----------
        btn_log = Button(login_frame,text='Login', width=15, font=('times new roman', 14,'bold'),bg='#B00857',fg='white',cursor='hand2', command=self.login_data).place(x=270, y=300)

    # ---------opening register window
    def Register_window(self):
        # destroying the window
        self.root.destroy()
        # opening opening the registration window
        import register


    # -----------checking if login is success fill or not
    def login_data(self):
        # ------------if the email and password are blank
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        # ------------if the email and password are not blank
        else:
            try:
                # -------------connection to database-----------
                con = pymysql.connect(host='localhost', user='root', password='', database='ambu')
                cur = con.cursor()
                cur2 = con.cursor()
                # --------------select the values from two data base-----------
                cur.execute("select * from worker where email=%s and password=%s", (self.txt_email.get(), self.txt_pass.get()))
                cur2.execute('select * from workermanage where email=%s',(self.txt_email.get()))
                row1 = cur.fetchone()
                row2 = cur2.fetchone()
                # -----------concatinating the two values
                row = row1 + row2
                #print(row)
                # ---------if there is anything present in the row variable then it will execute the following command
                # else it will display user does not exist--------
                if row != None:
                    # messagebox is used to show error or work is completed or abort the execution or ask a question
                    messagebox.showinfo("Success" , "Log in is successful" , parent=self.root)
                    # if login is success full it will redirect it to home page
                    self.root2 = Toplevel()                     # creating a new window
                    self.root2.title("Worker Login page")       # title for the window
                    self.root2.geometry('1350x700+0+0')         # setting the size of window
                    self.root2.config(bg='#08A3D2')             # background color of window
                    self.root2.focus_force()                    # this is used to focus on current window that has opened

                    # ---- title bar ------ #
                    title = Label(self.root2 , text='Admin Details Report' , bd=10 , relief=GROOVE ,
                                  font=('times new roman' , 40 , 'bold') , bg='crimson' , fg='blue')
                    title.pack(side=TOP , fill=X)

                    # -----frame for buttons------
                    frame12 = Frame(self.root2 , bd=4 , bg='crimson')
                    frame12.place(x=0 , y=85 , width=109 , height=640)

                    self.home = ImageTk.PhotoImage(file='images/house.png')
                    btn = Button(frame12 , image=self.home , command=self.home_page , bg='crimson' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=0 , width=92 , height=100)
                    self.prof = ImageTk.PhotoImage(file='images/prof.png')
                    btn1 = Button(frame12 , image=self.prof , command=self.profile_page , bg='crimson' , bd=5 ,
                                  relief=GROOVE , cursor='hand2').place(x=0 , y=104 , width=92 , height=100)
                    self.update = ImageTk.PhotoImage(file='images/update.png')
                    btn = Button(frame12 , image=self.update , command=self.update_page , bg='crimson' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=208 , width=92 , height=100)
                    self.logout = ImageTk.PhotoImage(file='images/logout.png')
                    btn = Button(frame12 , image=self.logout , command=self.logout_fn , bg='crimson' , bd=5 ,
                                 relief=GROOVE , cursor='hand2').place(x=0 , y=312 , width=92 , height=100)



                    self.frame22 = Frame(self.root2 , bd=4 , bg='white')
                    self.frame22.place(x=100 , y=85 , width=1250 , height=640)

                    self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
                    left = Label(self.frame22 , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,height=608)

                    self.message = Label(self.frame22 , text=f'Welcome\t{str(self.txt_email.get())}' ,
                                         font=('times new roman' , 50 , 'bold'),bg='deep sky blue',fg='#d77337').place(x=200 , y=200)

                    con = pymysql.connect(host='localhost', user='root', password='', database='ambu')
                    cur = con.cursor()
                    cur.execute('select reqst_accept from request_accept ')
                    row = cur.fetchone()
                    if (row != None) and (row[0] == 'Requesting for Ambulance'):
                        check = messagebox.askyesno('Success', r'Request has been Accepted', parent=self.root2)
                        print(check)
                        if check == True :
                            self.update_page()
                    else:
                        pass

                else:
                    messagebox.showerror("Error", " user dose not exist" , parent=self.root)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"password does not exist|Error due to: {str(es)}", parent=self.root)

    def home_page(self):
        self.frame22 = Frame(self.root2, bd=4, bg='white')
        self.frame22.place(x=100, y=85, width=1250, height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame22, image=self.left, bg='deep sky blue').place(x=0 , y=0 , width=1242, height=608)

        self.message = Label(self.frame22,text=f'Welcome\t{str(self.txt_email.get())}',font=('times new roman',50,'bold'),bg='deep sky blue',fg='#d77337').place(x=200,y=200)
        self.send_reqst = 'Accepted'


    def profile_page(self) :
        profile_frame = Frame(self.frame22 , bd=4 , bg='white')
        profile_frame.place(x=220 , y=100 , height=400 , width=800)
        profile_frame2 = Frame(profile_frame, bd=4 , bg='white')
        profile_frame2.place(x=10, y=320, height=70, width=770)

        self.profile = ImageTk.PhotoImage(file='images/user.png')
        p_frm = Label(profile_frame, image=self.profile , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=40, y=60 , width=200 , height=250)

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()

        # --------------row 1 column 1------------#
        id = Label(profile_frame, text='ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        id.place(x=250,y=60,height=20,width=70)
        id_txt = Entry(profile_frame, textvariable=self.id_var , font=('times new roman' , 13 , 'bold') , bd=0,state='readonly')
        id_txt.place(x=350,y=60,height=20,width=130)

        # --------------row 1 column 2------------#
        name = Label(profile_frame, text='Name' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        name.place(x=510,y=60,height=20,width=70)
        name_txt = Entry(profile_frame, textvariable=self.name_var , font=('times new roman' , 13 , 'bold'),bd=0 ,state='readonly')
        name_txt.place(x=610,y=60,height=20,width=130)

        # --------------row 2 column 1------------#
        email = Label(profile_frame, text='Email ID' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        email.place(x=250 , y=100 , height=20 , width=70)
        email_txt = Entry(profile_frame, textvariable=self.email_var , font=('times new roman' , 13 , 'bold') , bd=0,state='readonly')
        email_txt.place(x=350 , y=100 , height=20 , width=130)

        # --------------row 2 column 2------------#
        gender = Label(profile_frame, text='Gender' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        gender.place(x=510 , y=100 , height=20 , width=70)
        cmb_quest = Entry(profile_frame, textvariable=self.gender_var , font=('times new roman' , 12), bd=0,
                          justify=CENTER,state='readonly')
        cmb_quest.place(x=610 , y=100 , height=20 , width=130)

        # --------------row 3 column 1------------#
        phone = Label(profile_frame, text='phone number' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        phone.place(x=300 , y=140 , height=20 , width=150)
        phone_txt = Entry(profile_frame, textvariable=self.phone_var , font=('times new roman' , 13 , 'bold') , bd=0,state='readonly' )
        phone_txt.place(x=510 , y=140 , height=20 , width=150)

        # --------------row 4 column 1------------#
        dob = Label(profile_frame, text='D O B' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        dob.place(x=250,y=180,height=20,width=70)
        dob_txt = Entry(profile_frame, textvariable=self.dob_var , font=('times new roman' , 13 , 'bold'),bd=0 ,state='readonly')
        dob_txt.place(x=350,y=180,height=20,width=130)

        # --------------row 4 column 2------------#
        address = Label(profile_frame, text='Address', bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        address.place(x=510,y=180,height=20,width=70)
        self.address_txt = Entry(profile_frame,textvariable=self.address_var, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        self.address_txt.place(x=610,y=180,height=20,width=130)

        self.back_btn = ImageTk.PhotoImage(file='images/back.png')
        self.up_btn = Button(profile_frame , text="Update" , image=self.back_btn , command=self.home_page ,
                             font=('times new roman' , 13 , 'bold') , bg='white' , bd=0)
        self.up_btn.place(x=700 , y=270 , height=40 , width=50)

        # ----------table for getting the information of the user ------ #
        self.worker_table = ttk.Treeview(profile_frame2, column=('ID' , 'name' , 'email' , 'gender' , 'phone' , 'dob' , 'address'))
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
        self.worker_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()
        cur.execute("select * from workermanage where email=%s",(self.txt_email.get()))
        row = cur.fetchone()
        print(row)
        if row != 0:
            self.worker_table.insert('' , END , values=row)
        con.commit()
        con.close()

    # --------------for selecting the values-----------#
    def get_cursor(self, ev):
        cursor_row = self.worker_table.focus()
        contents = self.worker_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.phone_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_var.set(row[6])


    def update_page(self):
        update_frame = Frame(self.frame22 , bd=4 , bg='white')
        update_frame.place(x=220 , y=100 , height=400 , width=800)
        update_frame2 = Frame(update_frame, bd=4 , bg='white')
        update_frame2.place(x=10 , y=320 , height=70 , width=770)

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()

        self.update_prf = ImageTk.PhotoImage(file="images/user.png")
        p_frm = Label(update_frame , image=self.update_prf , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=40 , y=60 , width=200 , height=250)

        # --------------row 1 column 1------------#
        id = Label(update_frame, text='ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        id.place(x=250 , y=60 , height=20 , width=70)
        id_txt = Entry(update_frame , textvariable=self.id_var , font=('times new roman' , 13 , 'bold') , bd=0 ,
                       state='readonly')
        id_txt.place(x=350 , y=60 , height=20 , width=130)

        # --------------row 1 column 1------------#
        name = Label(update_frame, text='Name' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        name.place(x=510 , y=60 , height=20 , width=70)
        name_txt = Entry(update_frame, textvariable=self.name_var , font=('times new roman' , 13 , 'bold') , bd=0)
        name_txt.place(x=610 , y=60 , height=20 , width=130)

        # --------------row 1 column 1------------#
        email = Label(update_frame , text='Email ID' , bg='white' , fg='black' ,
                      font=('times new roman' , 15 , 'bold'))
        email.place(x=250 , y=100 , height=20 , width=70)
        email_txt = Entry(update_frame , textvariable=self.email_var , font=('times new roman' , 13 , 'bold') , bd=0)
        email_txt.place(x=350 , y=100 , height=20 , width=130)

        # --------------row 1 column 1------------#
        gender = Label(update_frame , text='Gender' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        gender.place(x=510 , y=100 , height=20 , width=70)
        cmb_quest = Entry(update_frame , textvariable=self.gender_var , font=('times new roman' , 12),bd=0,
                          justify=CENTER)
        cmb_quest.place(x=610 , y=100 , height=20 , width=130)

        # --------------row 1 column 1------------#
        phone = Label(update_frame, text='phone number' , bg='white' , fg='black' ,
                      font=('times new roman' , 15 , 'bold'))
        phone.place(x=300 , y=140 , height=20 , width=150)
        phone_txt = Entry(update_frame, textvariable=self.phone_var , font=('times new roman' , 13 , 'bold') , bd=0 )
        phone_txt.place(x=510 , y=140 , height=20 , width=150)

        dob = Label(update_frame, text='D O B' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        dob.place(x=250 , y=180 , height=20 , width=70)
        dob_txt = Entry(update_frame , textvariable=self.dob_var , font=('times new roman' , 13 , 'bold') , bd=0)
        dob_txt.place(x=350 , y=180 , height=20 , width=130)

        address = Label(update_frame, text='Address' , bg='white' , fg='black' ,
                        font=('times new roman' , 15 , 'bold'))
        address.place(x=510 , y=180 , height=20 , width=70)
        self.address_txt = Entry(update_frame,textvariable=self.address_var, font=('times new roman' , 13 , 'bold') , bd=0)
        self.address_txt.place(x=610 , y=180 , height=20 , width=130)

        self.up_btn = Button(update_frame,text="Update",command=self.update_data,font=('times new roman' , 13 , 'bold'),bg='#B00857',bd=0)
        self.up_btn.place(x=610 , y=270, height=40 , width=70)

        # ---------- code for getting the location ---------- #
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

        self.send_reqst = 'Accepted'

        btn_for_request = Button(update_frame , text='Accepting the Request' , command=self.send_request ,
                                 font=('times new roman' , 10 , 'bold') , bd=5 , relief=GROOVE).place(x=350 , y=270)

        self.back_btn = ImageTk.PhotoImage(file='images/back.png')
        self.up_btn = Button(update_frame , text="Update",image=self.back_btn , command=self.home_page,
                             font=('times new roman' , 13 , 'bold') , bg='white' , bd=0)
        self.up_btn.place(x=700 , y=270 , height=40 , width=50)

        self.worker_table = ttk.Treeview(update_frame2 ,
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
                                                                               self.address_txt.get(),
                                                                               self.id_var.get()
                                                                               ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Success", "The Records are Updated successfully!!", parent=self.root2)

    def send_request(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()
        cur.execute('select reqst_accept from request_accept')
        row = cur.fetchone()
        print(row)
        if row != None and row[0]=='Requesting for Ambulance':
            x=cur.execute('update request_accept set name=%s,email=%s,latitude=%s,longitude=%s,city=%s,state=%s,reqst_accept=%s', (self.name_var.get(),
                                                                                                                                   self.email_var.get(),
                                                                                                                                   self.latitude ,
                                                                                                                                   self.longitude ,
                                                                                                                                   self.city ,
                                                                                                                                   self.state ,
                                                                                                                                   self.send_reqst))
            print(x)
            con.commit()
            messagebox.showinfo('Success', 'The Request has been Accepted', parent=self.root2)
        else:
            pass
        con.close()


    def logout_fn(self) :
        self.root2.destroy()
        self.clear()
        self.root.focus_force()


    def clear(self):
        self.txt_email.delete(0, END)
        self.txt_pass.delete(0, END)



root = Tk()
obj = Login(root)
root.mainloop()