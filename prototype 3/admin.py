from tkinter import *
from tkinter import ttk, messagebox
import pymysql
class Admin:
    def __init__(self,root):
        self.root = root
        self.root.title("Admin Details Report")
        self.root.geometry('1350x700+0+0')
        title = Label(self.root,text='Admin Details Report',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='lime green',fg='red')
        title.pack(side=TOP, fill=X)

        #-----------variables
        self.ID_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.phone_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # worker management
        frame1 = Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        frame1.place(x=20,y=100,width=450,height=583)
        w_title = Label(frame1,text='Management of Workers', bg='crimson', fg='white',font=('times new roman',25,'bold'),justify=CENTER)
        w_title.grid(row=0,columnspan=2,pady=20)

        id = Label(frame1 , text='ID', bg='crimson' , fg='white', font=('times new roman' , 15 , 'bold'))
        id.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        id_txt = Entry(frame1, textvariable=self.ID_var, font=('times new roman' , 13, 'bold'), bd=5, relief=GROOVE)
        id_txt.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        name = Label(frame1 , text='Name' , bg='crimson' , fg='white' , font=('times new roman' ,15 , 'bold'))
        name.grid(row=2 , column=0 , pady=10 , padx=20 , sticky='w')
        name_txt = Entry(frame1, textvariable=self.name_var , font=('times new roman' , 13, 'bold') , bd=5 , relief=GROOVE)
        name_txt.grid(row=2, column=1 , pady=10 , padx=20 , sticky='w')

        email = Label(frame1 , text='Email ID' , bg='crimson' , fg='white' , font=('times new roman' , 15 , 'bold'))
        email.grid(row=3 , column=0 , pady=10 , padx=20 , sticky='w')
        email_txt = Entry(frame1 , textvariable=self.email_var , font=('times new roman' , 13 , 'bold') , bd=5 ,relief=GROOVE)
        email_txt.grid(row=3 , column=1 , pady=10 , padx=20 , sticky='w')

        gender = Label(frame1 , text='Gender' , bg='crimson' , fg='white' , font=('times new roman' , 15 , 'bold'))
        gender.grid(row=4 , column=0 , pady=10 , padx=20 , sticky='w')
        cmb_quest = ttk.Combobox(frame1 , textvariable=self.gender_var , font=('times new roman' , 12) ,
                                 state='readonly' , justify=CENTER)
        cmb_quest['values'] = ("SELECT" , "Male" , "Female" , "Others")
        cmb_quest.grid(row=4, column=1 , pady=10 , padx=20 , sticky='w')
        cmb_quest.current(0)

        phone = Label(frame1, text='phone number' , bg='crimson' , fg='white' , font=('times new roman' ,15 , 'bold'))
        phone.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        phone_txt = Entry(frame1, textvariable=self.phone_var , font=('times new roman' , 13, 'bold') , bd=5 , relief=GROOVE)
        phone_txt.grid(row=5, column=1 , pady=10, padx=20, sticky='w')

        dob = Label(frame1 , text='D O B' , bg='crimson' , fg='white' , font=('times new roman' , 15, 'bold'))
        dob.grid(row=6 , column=0 , pady=10 , padx=20 , sticky='w')
        dob_txt = Entry(frame1, textvariable=self.dob_var, font=('times new roman' , 13, 'bold') , bd=5 , relief=GROOVE)
        dob_txt.grid(row=6, column=1 , pady=10 , padx=20 , sticky='w')

        address = Label(frame1 , text='Address' , bg='crimson' , fg='white' , font=('times new roman' , 15, 'bold'))
        address.grid(row=7, column=0 , pady=10 , padx=20 , sticky='w')
        self.address_txt = Text(frame1, width=27, height=4, font=("", 10))
        self.address_txt.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        # ----btn frame
        btn_frame = Frame(frame1 , bd=4 , relief=RIDGE , bg='crimson')
        btn_frame.place(x=10 , y=500 , width=425)
        addbtn = Button(btn_frame , text="Add",command=self.add_Worker , width=10).grid(row=0 , column=0 , padx=10 , pady=10)
        updatebtn = Button(btn_frame , text="Update",command=self.update_data , width=10).grid(row=0 , column=1 , padx=10 , pady=10)
        deletebtn = Button(btn_frame , text="Delete", command=self.delete_data , width=10).grid(row=0 , column=2 , padx=10 , pady=10)
        clearbtn = Button(btn_frame , text="Clear", command=self.clear, width=10).grid(row=0 , column=3 , padx=10 , pady=10)

        frame2 = Frame(self.root , bd=4 , relief=RIDGE , bg='crimson')
        frame2.place(x=500 , y=100 , width=832 , height=583)

        search = Label(frame2 , text='Search by' , bg='crimson' , fg='white' , font=('times new roman' , 20 , 'bold'))
        search.grid(row=0 , column=0 , pady=10 , padx=20 , sticky='w')
        cmb_search = ttk.Combobox(frame2,textvariable=self.search_by, width=15, font=('times new roman' , 12) , state='readonly', justify=CENTER)
        cmb_search['values'] = ("ID", "name", "phone")
        cmb_search.grid(row=0, column=1 , pady=10 , padx=20 ,)

        search_txt = Entry(frame2,textvariable=self.search_txt, width=20, font=('times new roman' , 10 , 'bold') , bd=5, relief=GROOVE)
        search_txt.grid(row=0, column=2, pady=10, padx=20 , sticky='w')

        searchbtn = Button(frame2 , text="Search",command=self.search_data , width=10,pady=2).grid(row=0 , column=3, padx=10 , pady=10)
        showallbtn = Button(frame2 , text="Show All",command=self.fetch_data  , width=10,pady=2).grid(row=0 , column=4, padx=10 , pady=10)

        # -----------table frame
        table_frame = Frame(frame2, bd=4, relief=RIDGE, bg='crimson')
        table_frame.place(x=10, y=70,width=800, height=495)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame , orient=VERTICAL)
        self.worker_table = ttk.Treeview(table_frame,columns=('ID','name','email','gender','phone','dob','address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.worker_table.xview)
        scroll_y.config(command=self.worker_table.yview)
        self.worker_table.heading("ID", text='ID')
        self.worker_table.heading("name" , text='name')
        self.worker_table.heading("email" , text='email')
        self.worker_table.heading("gender" , text='gender')
        self.worker_table.heading("phone" , text='phone')
        self.worker_table.heading("dob" , text='dob')
        self.worker_table.heading("address" , text='address')
        self.worker_table['show'] = 'headings'
        self.worker_table.column('ID', width=100)
        self.worker_table.column('name', width=100)
        self.worker_table.column('email' , width=100)
        self.worker_table.column('phone' , width=100)
        self.worker_table.column('gender' , width=100)
        self.worker_table.column('dob' , width=100)
        self.worker_table.column('address' , width=170)
        self.worker_table.pack(fill=BOTH, expand=1)
        self.worker_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_Worker(self):
        if self.ID_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.phone_var.get()=="":
            messagebox.showerror('Error', 'All fields are Required!!!', parent=self.root)
        else:
            con = pymysql.connect(host='localhost', user='root', password='',database='ambu')
            cur = con.cursor()
            cur.execute('insert into workermanage values(%s,%s,%s,%s,%s,%s,%s)',(self.ID_var.get(),
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.phone_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.address_txt.get(1.0, END)
                                                                                ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "The details are added successfully!!", parent=self.root)

    def fetch_data(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur2 = con.cursor()
        r2 = 'select * from workermanage'
        cur2.execute(r2)
        row2 = cur2.fetchall()
        #print(r3)

        if len(row2) != 0:
            self.worker_table.delete(*self.worker_table.get_children())
            for row in (row2):
                self.worker_table.insert('',END,values=row)
            con.commit()

        con.close()

    def clear(self):
        self.ID_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.address_txt.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.worker_table.focus()
        contents = self.worker_table.item(cursor_row)
        row = contents['values']
        #print(row)
        self.ID_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.phone_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_txt.delete("1.0" , END)
        self.address_txt.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()
        cur.execute('update workermanage set name=%s,email=%s,phone=%s, gender=%s, dob=%s, address=%s where id=%s',
                                                                            (
                                                                               self.name_var.get() ,
                                                                               self.email_var.get() ,
                                                                               self.gender_var.get() ,
                                                                               self.phone_var.get() ,
                                                                               self.dob_var.get() ,
                                                                               self.address_txt.get(1.0 , END),
                                                                               self.ID_var.get()
                                                                               ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "The Records are Updated successfully!!", parent=self.root)

    def delete_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='ambu')
        cur = con.cursor()
        cur.execute('delete from workermanage where id=%s', self.ID_var.get())
        row = cur.fetchall()

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "The Records are Deleted successfully!!", parent=self.root)

    def search_data(self):
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='ambu')
        cur = con.cursor()

        cur.execute("select * from workermanage where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.worker_table.delete(*self.worker_table.get_children())
            for row in (rows):
                self.worker_table.insert('',END,values=row)
            con.commit()

        con.close()


root = Tk()
ob = Admin(root)
root.mainloop()