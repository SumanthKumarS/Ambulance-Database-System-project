#worker
from tkinter import *
from tkinter import ttk, messagebox         # where ttk is used to scrolling in table or creating a table
from PIL import Image, ImageTk              # importing images
import pymysql                              # pymysql is used to connect to mysql database
import requests


class Login:
    def __init__(self, root):
        self.root = root  # creating a new window
        self.root.title("Worker Login page")  # title for the window
        self.root.geometry('1350x700+0+0')  # setting the size of window
        self.root.config(bg='#08A3D2')  # background color of window
        self.root.focus_force()  # this is used to focus on current window that has opened


        # ---- title bar ------ #
        title = Label(self.root , text='Admin Details Report' , bd=10 , relief=GROOVE ,
                      font=('times new roman' , 40 , 'bold') , bg='light sea green' , fg='blue')
        title.pack(side=TOP , fill=X)

        # -----frame for buttons------
        frame12 = Frame(self.root , bd=4 , bg='light sea green')
        frame12.place(x=0 , y=85, width=109 , height=640)

        self.home = ImageTk.PhotoImage(file='images/house.png')
        btn = Button(frame12 , image=self.home,command=self.home_page, bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=0 , width=92 , height=100)
        self.user = ImageTk.PhotoImage(file='images/user-paitent.png')
        btn1 = Button(frame12 , image=self.user,command=self.user_patient, bg='light sea green' , bd=5 ,
                      relief=GROOVE , cursor='hand2').place(x=0 , y=104 , width=92 , height=100)
        self.worker = ImageTk.PhotoImage(file='images/worker.png')
        btn = Button(frame12 , image=self.worker,command=self.worker_page, bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=208 , width=92 , height=100)
        self.patient = ImageTk.PhotoImage(file='images/patient.png')
        btn = Button(frame12 , image=self.patient, command=self.patient_worker_page, bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=312 , width=92 , height=100)
        self.patient_details = ImageTk.PhotoImage(file='images/patient_details.png')
        btn = Button(frame12 , image=self.patient_details  , command=self.patient_detail_page , bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=416 , width=92 , height=100)
        self.home_page()

    def user_patient(self):
        self.fetch_p = 1
        self.frame = Frame(self.root , bd=4 , bg='white')
        self.frame.place(x=100 , y=85 , width=1350 , height=640)

        self.ID_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # worker management
        frame1 = Frame(self.frame , bd=4 , relief=RIDGE , bg='light sea green')
        frame1.place(x=10 , y=10 , width=450 , height=583)
        w_title = Label(frame1 , text='Management of Users' , bg='light sea green' , fg='white' ,
                        font=('times new roman' , 25 , 'bold') , justify=CENTER)
        w_title.grid(row=0 , columnspan=3 , pady=20)

        id = Label(frame1 , text='ID' , bg='light sea green' , fg='white' , font=('times new roman' , 15 , 'bold'))
        id.grid(row=1 , column=0 , pady=10 , padx=20 , sticky='w')
        id_txt = Entry(frame1 , textvariable=self.ID_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                       relief=GROOVE)
        id_txt.grid(row=1 , column=1 , pady=10 , padx=20 , sticky='w')

        name = Label(frame1 , text='Name' , bg='light sea green' , fg='white' , font=('times new roman' , 15 , 'bold'))
        name.grid(row=2 , column=0 , pady=10 , padx=20 , sticky='w')
        name_txt = Entry(frame1 , textvariable=self.name_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                         relief=GROOVE)
        name_txt.grid(row=2 , column=1 , pady=10 , padx=20 , sticky='w')

        email = Label(frame1 , text='Email ID' , bg='light sea green' , fg='white' ,
                      font=('times new roman' , 15 , 'bold'))
        email.grid(row=3 , column=0 , pady=10 , padx=20 , sticky='w')
        email_txt = Entry(frame1 , textvariable=self.email_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                          relief=GROOVE)
        email_txt.grid(row=3 , column=1 , pady=10 , padx=20 , sticky='w')

        gender = Label(frame1 , text='Gender' , bg='light sea green' , fg='white' ,
                       font=('times new roman' , 15 , 'bold'))
        gender.grid(row=4 , column=0 , pady=10 , padx=20 , sticky='w')
        cmb_quest = ttk.Combobox(frame1 , textvariable=self.gender_var , font=('times new roman' , 12) ,
                                 state='readonly' , justify=CENTER)
        cmb_quest['values'] = ("SELECT" , "Male" , "Female" , "Others")
        cmb_quest.grid(row=4 , column=1 , pady=10 , padx=20 , sticky='w')
        cmb_quest.current(0)

        phone = Label(frame1 , text='phone number' , bg='light sea green' , fg='white' ,
                      font=('times new roman' , 15 , 'bold'))
        phone.grid(row=5 , column=0 , pady=10 , padx=20 , sticky='w')
        phone_txt = Entry(frame1 , textvariable=self.phone_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                          relief=GROOVE)
        phone_txt.grid(row=5 , column=1 , pady=10 , padx=20 , sticky='w')

        dob = Label(frame1 , text='D O B' , bg='light sea green' , fg='white' , font=('times new roman' , 15 , 'bold'))
        dob.grid(row=6 , column=0 , pady=10 , padx=20 , sticky='w')
        dob_txt = Entry(frame1 , textvariable=self.dob_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                        relief=GROOVE)
        dob_txt.grid(row=6 , column=1 , pady=10 , padx=20 , sticky='w')
        date = self.dob_var.get()
        if (date) :
            Month = ['' , 'JAN' , 'FEB' , 'MAR' , 'APR' , 'MAY' , 'JUN' , 'JUL' , 'AUG' , 'SEP' , 'OCT' , 'NOV' , 'DEC']
            date = self.dob_var.get()
            date = date.split('/')
            print(date)
            mon = int(date[1])
            print(mon)
            self.dbdate = '20' + date[2] + '-' + date[1] + '-' + date[0]
            print(self.dbdate)

        address = Label(frame1 , text='Address' , bg='light sea green' , fg='white' ,
                        font=('times new roman' , 15 , 'bold'))
        address.grid(row=7 , column=0 , pady=10 , padx=20 , sticky='w')
        self.address_txt = Text(frame1 , width=27 , height=4 , font=("" , 10))
        self.address_txt.grid(row=7 , column=1 , pady=10 , padx=20 , sticky='w')

        # ----btn frame
        btn_frame = Frame(frame1 , bd=4 , relief=RIDGE , bg='light sea green')
        btn_frame.place(x=10 , y=500 , width=420)

        addbtn = Button(btn_frame , text="Add",command=self.add_data , width=10).grid(row=0 , column=0 , padx=10 ,pady=10)
        updatebtn = Button(btn_frame , text="Update",command=self.update_data, width=10).grid(row=0 , column=1 ,padx=10 , pady=10)
        deletebtn = Button(btn_frame , text="Delete",command=self.delete_data , width=10).grid(row=0 , column=2 , padx=10 , pady=10)
        clearbtn = Button(btn_frame , text="Clear",command=self.clear, width=10).grid(row=0 , column=3 , padx=10 , pady=10)

        frame2 = Frame(self.frame, bd=4 , relief=RIDGE , bg='light sea green')
        frame2.place(x=480, y=10 , width=750 , height=583)

        search = Label(frame2 , text='Search by' , bg='light sea green' , fg='white' ,
                       font=('times new roman' , 20 , 'bold'))
        search.grid(row=0 , column=0 , pady=10 , padx=20 , sticky='w')
        cmb_search = ttk.Combobox(frame2 , textvariable=self.search_by , width=15 , font=('times new roman' , 12) ,
                                  state='readonly' , justify=CENTER)
        cmb_search['values'] = ("select","user_id" , "name" , "phone")
        cmb_search.grid(row=0 , column=1 , pady=10 , padx=20 )
        cmb_search.current(0)

        search_txt = Entry(frame2 , textvariable=self.search_txt , width=20 , font=('times new roman' , 10 , 'bold') ,
                           bd=5 , relief=GROOVE)
        search_txt.grid(row=0 , column=2 , pady=10 , padx=20 , sticky='w')

        searchbtn = Button(frame2 , text="Search",command=self.search_data , width=10 , pady=2).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(frame2 , text="Show All",command=self.fetch_data , width=10 , pady=2).grid(row=0, column=4, padx=10, pady=10)

        # -----------table frame
        table_frame = Frame(frame2 , bd=4 , relief=RIDGE , bg='light sea green')
        table_frame.place(x=10 , y=70 , width=720 , height=460)

        bck_btn = Button(frame2,text="Back",command=self.home_page,font=('times new roman',15,'bold')).place(x=370,y=532)

        scroll_x = Scrollbar(table_frame , orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame , orient=VERTICAL)
        self.user_table = ttk.Treeview(table_frame ,column=('ID' , 'name' , 'phone' , 'email' , 'dob' , 'gender' , 'address') ,
                                       xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)
        self.user_table.heading("ID" , text='ID')
        self.user_table.heading("name" , text='name')
        self.user_table.heading("phone" , text='phone')
        self.user_table.heading("email" , text='email')
        self.user_table.heading("dob" , text='dob')
        self.user_table.heading("gender" , text='gender')
        self.user_table.heading("address" , text='address')
        self.user_table['show'] = 'headings'
        self.user_table.column('ID' , width=100)
        self.user_table.column('name' , width=100)
        self.user_table.column('phone' , width=100)
        self.user_table.column('email' , width=100)
        self.user_table.column('dob' , width=100)
        self.user_table.column('gender' , width=100)
        self.user_table.column('address' , width=170)
        self.user_table.pack(fill=BOTH , expand=1)
        self.user_table.bind("<ButtonRelease-1>" , self.get_cursor)
        self.fetch_data()

    def home_page(self) :
        self.frame = Frame(self.root , bd=4 , bg='white')
        self.frame.place(x=100 , y=85 , width=1350 , height=640)
        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,
                                                                              height=608)

    def worker_page(self):
        self.fetch_p = 2
        self.frame = Frame(self.root , bd=4 , bg='white')
        self.frame.place(x=100 , y=85 , width=1350 , height=640)

        self.ID_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # worker management
        frame1 = Frame(self.frame , bd=4 , relief=RIDGE , bg='light sea green')
        frame1.place(x=10 , y=10 , width=450 , height=583)
        w_title = Label(frame1 , text='Management of Worker' , bg='light sea green' , fg='white' ,
                        font=('times new roman' , 25 , 'bold') , justify=CENTER)
        w_title.grid(row=0 , columnspan=3 , pady=20)

        id = Label(frame1 , text='ID' , bg='light sea green' , fg='white' , font=('times new roman' , 15 , 'bold'))
        id.grid(row=1 , column=0 , pady=10 , padx=20 , sticky='w')
        id_txt = Entry(frame1 , textvariable=self.ID_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                       relief=GROOVE)
        id_txt.grid(row=1 , column=1 , pady=10 , padx=20 , sticky='w')

        name = Label(frame1 , text='Name' , bg='light sea green' , fg='white' , font=('times new roman' , 15 , 'bold'))
        name.grid(row=2 , column=0 , pady=10 , padx=20 , sticky='w')
        name_txt = Entry(frame1 , textvariable=self.name_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                         relief=GROOVE)
        name_txt.grid(row=2 , column=1 , pady=10 , padx=20 , sticky='w')

        email = Label(frame1 , text='Email ID' , bg='light sea green' , fg='white' ,
                      font=('times new roman' , 15 , 'bold'))
        email.grid(row=3 , column=0 , pady=10 , padx=20 , sticky='w')
        email_txt = Entry(frame1 , textvariable=self.email_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                          relief=GROOVE)
        email_txt.grid(row=3 , column=1 , pady=10 , padx=20 , sticky='w')

        gender = Label(frame1 , text='Gender' , bg='light sea green' , fg='white' ,
                       font=('times new roman' , 15 , 'bold'))
        gender.grid(row=4 , column=0 , pady=10 , padx=20 , sticky='w')
        cmb_quest = ttk.Combobox(frame1 , textvariable=self.gender_var , font=('times new roman' , 12) ,
                                 state='readonly' , justify=CENTER)
        cmb_quest['values'] = ("SELECT" , "Male" , "Female" , "Others")
        cmb_quest.grid(row=4 , column=1 , pady=10 , padx=20 , sticky='w')
        cmb_quest.current(0)

        phone = Label(frame1 , text='phone number' , bg='light sea green' , fg='white' ,
                      font=('times new roman' , 15 , 'bold'))
        phone.grid(row=5 , column=0 , pady=10 , padx=20 , sticky='w')
        phone_txt = Entry(frame1 , textvariable=self.phone_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                          relief=GROOVE)
        phone_txt.grid(row=5 , column=1 , pady=10 , padx=20 , sticky='w')

        dob = Label(frame1 , text='D O B' , bg='light sea green' , fg='white' , font=('times new roman' , 15 , 'bold'))
        dob.grid(row=6 , column=0 , pady=10 , padx=20 , sticky='w')
        dob_txt = Entry(frame1 , textvariable=self.dob_var , font=('times new roman' , 13 , 'bold') , bd=5 ,
                        relief=GROOVE)
        dob_txt.grid(row=6 , column=1 , pady=10 , padx=20 , sticky='w')
        date = self.dob_var.get()
        if (date) :
            Month = ['' , 'JAN' , 'FEB' , 'MAR' , 'APR' , 'MAY' , 'JUN' , 'JUL' , 'AUG' , 'SEP' , 'OCT' , 'NOV' , 'DEC']
            date = self.dob_var.get()
            date = date.split('/')
            print(date)
            mon = int(date[1])
            print(mon)
            self.dbdate = '20' + date[2] + '-' + date[1] + '-' + date[0]
            print(self.dbdate)

        address = Label(frame1 , text='Address' , bg='light sea green' , fg='white' ,
                        font=('times new roman' , 15 , 'bold'))
        address.grid(row=7 , column=0 , pady=10 , padx=20 , sticky='w')
        self.address_txt = Text(frame1 , width=27 , height=4 , font=("" , 10))
        self.address_txt.grid(row=7 , column=1 , pady=10 , padx=20 , sticky='w')

        # ----btn frame
        btn_frame = Frame(frame1 , bd=4 , relief=RIDGE , bg='light sea green')
        btn_frame.place(x=10 , y=500 , width=420)

        addbtn = Button(btn_frame , text="Add" ,command=self.add_data, width=10).grid(row=0 , column=0 , padx=10 , pady=10)
        updatebtn = Button(btn_frame , text="Update" ,command=self.update_data, width=10).grid(row=0 , column=1 , padx=10 , pady=10)
        deletebtn = Button(btn_frame , text="Delete",command=self.delete_data , width=10).grid(row=0 , column=2 , padx=10 , pady=10)
        clearbtn = Button(btn_frame , text="Clear",command=self.clear , width=10).grid(row=0 , column=3 , padx=10 , pady=10)

        frame2 = Frame(self.frame , bd=4 , relief=RIDGE , bg='light sea green')
        frame2.place(x=480 , y=10 , width=750 , height=583)

        search = Label(frame2 , text='Search by' , bg='light sea green' , fg='white' ,
                       font=('times new roman' , 20 , 'bold'))
        search.grid(row=0 , column=0 , pady=10 , padx=20 , sticky='w')
        cmb_search = ttk.Combobox(frame2 , textvariable=self.search_by , width=15 , font=('times new roman' , 12) ,
                                  state='readonly' , justify=CENTER)
        cmb_search['values'] = ("select","worker_id" , "name" , "phone")
        cmb_search.grid(row=0 , column=1 , pady=10 , padx=20  )
        cmb_search.current(0)

        search_txt = Entry(frame2 , textvariable=self.search_txt , width=20 , font=('times new roman' , 10 , 'bold') ,
                           bd=5 , relief=GROOVE)
        search_txt.grid(row=0 , column=2 , pady=10 , padx=20 , sticky='w')

        searchbtn = Button(frame2 , text="Search",command=self.search_data , width=10 , pady=2).grid(row=0 , column=3 , padx=10 , pady=10)
        showallbtn = Button(frame2 , text="Show All",command=self.fetch_data , width=10 , pady=2).grid(row=0 , column=4 , padx=10 , pady=10)

        # -----------table frame
        table_frame = Frame(frame2 , bd=4 , relief=RIDGE , bg='light sea green')
        table_frame.place(x=10 , y=70 , width=720 , height=460)

        bck_btn = Button(frame2 , text="Back" , command=self.home_page , font=('times new roman' , 15 , 'bold')).place(
            x=370 , y=532)

        scroll_x = Scrollbar(table_frame , orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame , orient=VERTICAL)
        self.worker_table = ttk.Treeview(table_frame , column=('ID' , 'name' , 'phone' , 'email' , 'dob' , 'gender' , 'address') ,
                                       xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.worker_table.xview)
        scroll_y.config(command=self.worker_table.yview)
        self.worker_table.heading("ID" , text='ID')
        self.worker_table.heading("name" , text='name')
        self.worker_table.heading("phone" , text='phone')
        self.worker_table.heading("email" , text='email')
        self.worker_table.heading("dob" , text='dob')
        self.worker_table.heading("gender" , text='dob')
        self.worker_table.heading("address" , text='address')
        self.worker_table['show'] = 'headings'
        self.worker_table.column('ID' , width=100)
        self.worker_table.column('name' , width=100)
        self.worker_table.column('phone' , width=100)
        self.worker_table.column('email' , width=100)
        self.worker_table.column('dob' , width=100)
        self.worker_table.column('gender' , width=100)
        self.worker_table.column('address' , width=170)
        self.worker_table.pack(fill=BOTH , expand=1)
        self.worker_table.bind("<ButtonRelease-1>" , self.get_cursor)
        self.fetch_data()

    def patient_worker_page(self):
        self.fetch_p = 3
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.frame = Frame(self.root , bd=4 , bg='white')
        self.frame.place(x=100 , y=85 , width=1350 , height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,height=608)

        search = Label(self.frame , text='Search by',
                       font=('times new roman' , 20 , 'bold'))
        search.place(x=50, y=10,width=170,height=30)
        cmb_search = ttk.Combobox(self.frame,textvariable=self.search_by, width=15 , font=('times new roman' , 12) ,
                                  state='readonly' , justify=CENTER)
        cmb_search['values'] = ("select","id" , "name" , "phone","date")
        cmb_search.place(x=300, y=10,width=200,height=30)
        cmb_search.current(0)

        search_txt = Entry(self.frame,textvariable=self.search_txt, width=20 , font=('times new roman' , 10 , 'bold') ,
                           bd=5 , relief=GROOVE)
        search_txt.place(x=600, y=10,width=200,height=30)

        searchbtn = Button(self.frame , text="Search" , command=self.search_data , width=10 , pady=2).place(x=980, y=10,width=100,height=30)

        showallbtn = Button(self.frame , text="Show All" , command=self.fetch_data , width=10 , pady=2).place(x=1080, y=10,width=100,height=30)

        # -----------table frame
        table_frame = Frame(self.frame, bd=4 , relief=RIDGE , bg='light sea green')
        table_frame.place(x=50 , y=50 , width=1130 , height=460)

        bck_btn = Button(self.frame, text="Back" , command=self.home_page , font=('times new roman' , 15 , 'bold')).place(
            x=600 , y=532)

        scroll_x = Scrollbar(table_frame , orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame , orient=VERTICAL)
        self.patient_table = ttk.Treeview(table_frame ,
                                         column=('ID' , 'name' , 'email' , 'latitude' , 'longitude' , 'city' , 'state','request|accept','date','time') ,
                                         xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('Treeview' , background='white')
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.patient_table.xview)
        scroll_y.config(command=self.patient_table.yview)
        self.patient_table.heading("ID" , text='ID')
        self.patient_table.heading("name" , text='name')
        self.patient_table.heading("email" , text='email')
        self.patient_table.heading("latitude" , text='latitude')
        self.patient_table.heading("longitude" , text='longitude')
        self.patient_table.heading("city" , text='dob')
        self.patient_table.heading("state" , text='state')
        self.patient_table.heading("date" , text='date')
        self.patient_table.heading("time" , text='time')
        self.patient_table.heading("request|accept" , text='request|accept')
        self.patient_table['show'] = 'headings'
        self.patient_table.column('ID' , width=100)
        self.patient_table.column('name' , width=100)
        self.patient_table.column('email' , width=100)
        self.patient_table.column('latitude' , width=100)
        self.patient_table.column('longitude' , width=100)
        self.patient_table.column('city' , width=100)
        self.patient_table.column('state' , width=100)
        self.patient_table.column('request|accept' , width=170)
        self.patient_table.column("date" , width=100)
        self.patient_table.column("time" , width=100)
        self.patient_table.pack(fill=BOTH , expand=1)
        self.fetch_data()

    def fetch_data(self):
        if self.fetch_p == 2:
            con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
            cur2 = con.cursor()
            r2 = 'select * from worker_manage'
            cur2.execute(r2)
            row2 = cur2.fetchall()

            if len(row2) != 0:
                self.worker_table.delete(*self.worker_table.get_children())
                for row in (row2):
                    self.worker_table.insert('',END,values=row)
                con.commit()

            con.close()
        elif self.fetch_p == 1:
            con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
            cur2 = con.cursor()
            r2 = 'select * from user_info'
            cur2.execute(r2)
            row2 = cur2.fetchall()
            # print(r3)

            if len(row2) != 0 :
                self.user_table.delete(*self.user_table.get_children())
                for row in (row2) :
                    self.user_table.insert('' , END , values=row)
                con.commit()
            con.close()
        elif self.fetch_p == 3:
            con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
            cur2 = con.cursor()
            r2 = 'select * from request_details'
            cur2.execute(r2)
            row2 = cur2.fetchall()
            #print(row2)

            if len(row2) != 0:
                self.patient_table.delete(*self.patient_table.get_children())
                for row in row2:
                    if row[7] == "Requesting for Ambulance":
                        self.patient_table.insert('', END,
                                              values=(row),
                                              tags='Requestingforambulance')
                    elif row[7] == "Reject":
                        self.patient_table.insert('', END,
                                              values=(row),
                                              tags='Reject')
                    else:
                        self.patient_table.insert('', END,
                                                  values=(row),
                                                  tags='Accepting')

                self.patient_table.tag_configure("Accepting" , foreground='white' , background="green")
                self.patient_table.tag_configure("Reject", foreground='white', background="red")
                self.patient_table.tag_configure("RequestingforAmbulance" , foreground='blue' , background="black")

                con.commit()

            con.close()
        else:
            con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
            cur2 = con.cursor()
            r2 = 'select * from patient_details'
            cur2.execute(r2)
            row2 = cur2.fetchall()

            if len(row2) != 0 :
                self.patient_data_table.delete(*self.patient_data_table.get_children())
                for row in (row2) :
                    self.patient_data_table.insert('' , END , values=row)
                con.commit()

            con.close()

    def get_cursor(self, ev):
        if self.fetch_p == 1:
            cursor_row = self.user_table.focus()
            contents = self.user_table.item(cursor_row)
            row = contents['values']
            self.ID_var.set(row[0])
            self.name_var.set(row[1])
            self.phone_var.set(row[2])
            self.email_var.set(row[3])
            self.dbdate.set(row[4])
            self.gender_var.set(row[5])
            self.address_txt.delete("1.0" , END)
            self.address_txt.insert(END,row[6])
        elif self.fetch_p == 2 :
            cursor_row = self.worker_table.focus()
            contents = self.worker_table.item(cursor_row)
            row = contents['values']
            self.ID_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.phone_var.set(row[4])
            self.dbdate.set(row[5])
            self.address_txt.delete("1.0" , END)
            self.address_txt.insert(END , row[6])

    def add_data(self) :
        if self.fetch_p == 1:
            if self.ID_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.phone_var.get() == "" :
                messagebox.showerror('Error' , 'All fields are Required!!!' , parent=self.root)
            else:
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
                cur = con.cursor()
                cur.execute('select email from user where email=%s',self.email_var.get())
                row = cur.fetchone()
                print(row)
                if row == None or self.email_var.get() != row[0]:
                    print(self.email_var.get())
                    cur.execute('insert into user (f_name, phone, email, dob, gender) values(%s,%s,%s,%s,%s)', (
                                                                                    self.name_var.get(),
                                                                                    self.phone_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.dbdate.get(),
                                                                                    self.gender_var.get()
                                                                                    ))
                    cur.execute('insert into user_info (name, phone, email, dob, gender,address) values(%s,%s,%s,%s,%s,%s)', (
                        self.name_var.get() ,
                        self.phone_var.get() ,
                        self.email_var.get() ,
                        self.dbdate.get() ,
                        self.gender_var.get(),
                        self.address_txt.get(1.0, END)
                    ))
                    messagebox.showinfo("Success" , "The details are added successfully!!" , parent=self.root)
                else:
                    messagebox.showinfo('Success', 'The user already exist', parent=self.root)

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
        elif self.fetch_p == 2:
            if self.ID_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.phone_var.get() == "" :
                messagebox.showerror('Error' , 'All fields are Required!!!' , parent=self.root)
            else:
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
                cur = con.cursor()
                cur.execute('select email from worker where email=%s',self.email_var.get())
                row = cur.fetchone()
                print(row)
                if row == None or row[0] != self.email_var.get():
                    cur.execute('insert into worker (f_name, phone, email) values(%s,%s,%s)', (
                                                                                    self.name_var.get(),
                                                                                    self.phone_var.get(),
                                                                                    self.email_var.get()
                                                                                    ))
                    cur.execute('insert into worker_manage (name, phone, email, dob, gender,address) values(%s,%s,%s,%s,%s,%s)', (
                        self.name_var.get(),
                        self.phone_var.get(),
                        self.email_var.get(),
                        self.dbdate.get() ,
                        self.gender_var.get(),
                        self.address_txt.get(1.0, END)
                    ))
                    messagebox.showinfo("Success" , "The details are added successfully!!" , parent=self.root)
                else:
                    messagebox.showinfo('Success', 'The user already exist', parent=self.root)
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()

    def update_data(self):
        if self.fetch_p == 1:
            con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
            cur = con.cursor()
            cur.execute('select email from user where email=%s' , self.email_var.get())
            row = cur.fetchone()
            print(row)
            print(row[0])
            if row[0] == self.email_var.get():
                cur.execute('update user set f_name=%s,email=%s,phone=%s, gender=%s, dob=%s where id=%s',
                                                                                    (
                                                                                       self.name_var.get() ,
                                                                                       self.email_var.get() ,
                                                                                       self.gender_var.get() ,
                                                                                       self.phone_var.get() ,
                                                                                       self.dob_var.get() ,
                                                                                       self.ID_var.get()
                                                                                       ))
                cur.execute('update user_info set name=%s,phone=%s,email=%s, dob=%s, gender=%s, address=%s where id=%s' ,
                            (
                                self.name_var.get() ,
                                self.phone_var.get() ,
                                self.email_var.get() ,
                                self.dob_var.get() ,
                                self.gender_var.get() ,
                                self.address_txt.get(1.0 , END) ,
                                self.ID_var.get()
                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "The Records are Updated successfully!!", parent=self.root)
        elif self.fetch_p == 2:
            con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
            cur = con.cursor()
            cur.execute('select email from worker where email=%s' , self.email_var.get())
            row = cur.fetchone()
            print(row)
            print(row[0])
            if row[0] == self.email_var.get():
                cur.execute('update worker set f_name=%s,email=%s,phone=%s where id=%s',
                                                                                    (
                                                                                       self.name_var.get() ,
                                                                                       self.email_var.get() ,
                                                                                       self.phone_var.get() ,
                                                                                       self.ID_var.get()
                                                                                       ))
                cur.execute('update worker_manage set name=%s,phone=%s,email=%s, dob=%s, gender=%s, address=%s where id=%s' ,
                            (
                                self.name_var.get() ,
                                self.phone_var.get() ,
                                self.email_var.get() ,
                                self.dob_var.get() ,
                                self.gender_var.get() ,
                                self.address_txt.get(1.0 , END) ,
                                self.ID_var.get()
                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "The Records are Updated successfully!!", parent=self.root)

    def delete_data(self):
        if self.fetch_p == 1:
            con = pymysql.connect(host='localhost', user='root', password='', database='ambulance')
            cur1 = con.cursor()
            cur2 = con.cursor()
            cur1.execute('select email from user where email=%s' , self.email_var.get())
            row = cur1.fetchone()
            if row[0] == self.email_var.get() :
                cur1.execute('delete from user where email=%s', self.email_var.get())
                cur2.execute('delete from user_info where email=%s', self.email_var.get())
                row1 = cur1.fetchall()
                row2 = cur2.fetchall()
                con.commit()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success" , "The Records are Deleted successfully!!" , parent=self.root)
            con.close()

        elif self.fetch_p == 2:
            con = pymysql.connect(host='localhost', user='root', password='', database='ambulance')
            cur = con.cursor()
            cur.execute('select email from worker where email=%s', self.email_var.get())
            row = cur.fetchone()
            print(row)
            print(row[0])
            if row[0] == self.email_var.get() :
                cur.execute('delete from worker where email=%s',self.email_var.get())
                cur.execute('delete from worker_manage where email=%s',self.email_var.get())
                row = cur.fetchall()
                con.commit()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success" , "The Records are Deleted successfully!!" , parent=self.root)
            con.close()


    def clear(self):
        if self.fetch_p == 1:
            self.ID_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.phone_var.set("")
            self.gender_var.set("")
            self.dob_var.set(0)
            self.address_txt.delete("1.0", END)
        elif self.fetch_p == 2:
            self.ID_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.phone_var.set("")
            self.gender_var.set("SELECT")
            self.dob_var.set("")
            self.address_txt.delete("1.0" , END)

    def search_data(self):
        if self.fetch_p ==1:
            print(self.search_by.get())
            if self.search_by.get()!="" and self.search_txt.get()!="":
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
                cur = con.cursor()

                cur.execute("select * from user_info where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.user_table.delete(*self.user_table.get_children())
                    for row in (rows):
                        self.user_table.insert('', END, values=row)
                    con.commit()
                con.close()
            else:
                messagebox.showerror("Error", "Please Select the content for searching", parent=self.root)
        elif self.fetch_p == 2:
            if self.search_by.get() != "" and self.search_txt.get() != "" :
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
                cur = con.cursor()

                cur.execute("select * from worker_manage where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows = cur.fetchall()

                if len(rows) != 0 :
                    self.worker_table.delete(*self.worker_table.get_children())
                    for row in (rows) :
                        self.worker_table.insert('' , END , values=row)
                    con.commit()

                con.close()
            else:
                messagebox.showerror("Error", "Please Select the content for searching", parent=self.root)
        elif self.fetch_p == 3 :
            print(self.fetch_p)
            if self.search_by.get()!="" and self.search_txt.get()!="":
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
                cur = con.cursor()

                cur.execute("select * from request_details where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows = cur.fetchall()
                if len(rows) != 0 :
                    self.patient_table.delete(*self.patient_table.get_children())
                    for row in rows :
                        # print(row[7])
                        # print(row)

                        if row[7] == "Requesting for Ambulance" :
                            self.patient_table.insert('' , END ,
                                                      values=(row) ,
                                                      tags='Requestingforambulance')


                        elif row[7] == "Reject" :
                            self.patient_table.insert('' , END ,
                                                      values=(row) ,
                                                      tags='Reject')

                        else :
                            self.patient_table.insert('' , END ,
                                                      values=(row) ,
                                                      tags='Accepting')

                    self.patient_table.tag_configure("Accepting" , foreground='white' , background="green")
                    self.patient_table.tag_configure("Reject" , foreground='white' , background="red")
                    self.patient_table.tag_configure("RequestingforAmbulance" , foreground='blue' , background="black")

                    con.commit()
                con.close()
            else:
                messagebox.showerror("Error", "Please Select the content for searching", parent=self.root)
        elif self.fetch_p == 4:
            if self.search_by.get() != "" and self.search_txt.get() != "" :
                con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambulance')
                cur = con.cursor()

                cur.execute("select * from patient_details where " + str(self.search_by.get()) + " LIKE '%" + str(
                    self.search_txt.get()) + "%'")
                rows = cur.fetchall()

                if len(rows) != 0 :
                    self.patient_data_table.delete(*self.patient_data_table.get_children())
                    for row in (rows) :
                        self.patient_data_table.insert('' , END , values=row)
                    con.commit()

                con.close()
            else :
                messagebox.showerror("Error" , "Please Select the content for searching" , parent=self.root)
        else:
            pass

    def patient_detail_page(self):
        self.fetch_p = 4
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.frame = Frame(self.root , bd=4 , bg='white')
        self.frame.place(x=100 , y=85 , width=1350 , height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 , height=608)

        search = Label(self.frame , text='Search by' ,
                       font=('times new roman' , 20 , 'bold'))
        search.place(x=50 , y=10 , width=170 , height=30)
        cmb_search = ttk.Combobox(self.frame , textvariable=self.search_by , width=15 , font=('times new roman' , 12) ,
                                  state='readonly' , justify=CENTER)
        cmb_search['values'] = ("select" , "PNO" , "name" , "phone" , "date")
        cmb_search.place(x=300 , y=10 , width=200 , height=30)
        cmb_search.current(0)

        search_txt = Entry(self.frame , textvariable=self.search_txt , width=20 ,
                           font=('times new roman' , 10 , 'bold') ,
                           bd=5 , relief=GROOVE)
        search_txt.place(x=600 , y=10 , width=200 , height=30)

        searchbtn = Button(self.frame , text="Search" , command=self.search_data , width=10 , pady=2).place(x=980 ,
                                                                                                            y=10 ,
                                                                                                            width=100 ,
                                                                                                            height=30)

        showallbtn = Button(self.frame , text="Show All" , command=self.fetch_data , width=10 , pady=2).place(x=1080 ,
                                                                                                              y=10 ,
                                                                                                              width=100 ,
                                                                                                              height=30)

        # -----------table frame
        table_frame = Frame(self.frame , bd=4 , relief=RIDGE , bg='light sea green')
        table_frame.place(x=50 , y=50 , width=1130 , height=460)

        bck_btn = Button(self.frame , text="Back" , command=self.home_page ,
                         font=('times new roman' , 15 , 'bold')).place(
            x=600 , y=532)

        scroll_x = Scrollbar(table_frame , orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame , orient=VERTICAL)
        self.patient_data_table = ttk.Treeview(table_frame ,
                                          column=(
                                          'ID' , 'name' , 'email' , 'phone' , 'address' , 'place' , 'date|time') ,
                                          xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('Treeview' , background='white')
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.patient_data_table.xview)
        scroll_y.config(command=self.patient_data_table.yview)
        self.patient_data_table.heading("ID" , text='ID')
        self.patient_data_table.heading("name" , text='name')
        self.patient_data_table.heading("email" , text='email')
        self.patient_data_table.heading("phone" , text='phone')
        self.patient_data_table.heading("address" , text='address')
        self.patient_data_table.heading("place" , text='place')
        self.patient_data_table.heading("date|time" , text='date|time')
        self.patient_data_table['show'] = 'headings'
        self.patient_data_table.column('ID' , width=100)
        self.patient_data_table.column('name' , width=100)
        self.patient_data_table.column('email' , width=100)
        self.patient_data_table.column('phone' , width=100)
        self.patient_data_table.column('address' , width=100)
        self.patient_data_table.column('place' , width=100)
        self.patient_data_table.column("date|time" , width=100)
        self.patient_data_table.pack(fill=BOTH , expand=1)
        self.fetch_data()




root = Tk()
obj = Login(root)
root.mainloop()