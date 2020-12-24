from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
class Reg:
    def __init__(self,root):
        self.root=root
        self.root.title("cool")
        self.root.geometry('1350x700+0+0')
        title=Label(root,text="PATIENT DETAILS",font=("impact",40),bg="green",fg="red").place(x=0,y=0,relwidth=1)
       
        
        f_name=Label(root,text="first name",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=30,y=180)
        self.txt_fname=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_fname.place(x=30,y=230,width=550)  

        l_name=Label(root,text="last name",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=730,y=180)
        self.txt_lname=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_lname.place(x=730,y=230,width=550)  

        contact=Label(root,text="contact no",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=30,y=280)
        self.txt_contact=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_contact.place(x=30,y=330,width=550) 

        email=Label(root,text="email",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=730,y=280)
        self.txt_email=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_email.place(x=730,y=330,width=550) 


        address=Label(root,text="address",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=30,y=380)
        self.txt_address=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_address.place(x=30,y=430,width=550) 

        passd=Label(root,text="password",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=730,y=380)
        self.txt_passd=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_passd.place(x=730,y=430,width=550)



        date=Label(root,text="date of birth",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=30,y=480)
        self.txt_date=Entry(root,font=("times new roman",25),bg="lightgrey")
        self.txt_date.place(x=30,y=530,width=550)


        gender=Label(root,text="Gender",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=730,y=480)
        self.com=ttk.Combobox(root,font=("times new roman",25),state='readonly',justify=CENTER)
        self.com['values']=('select','male','female','others')
        self.com.place(x=730,y=530,width=550)
        self.com.current(0)
        




        self.var_chk= IntVar()
        check_=Checkbutton(root,text="Accept out terms and Condition",font=("times new roman",12),bg="white",onvalue=1,offvalue=0,variable=self.var_chk).place(x=30,y=580)
        btn=Button(root,text="submit",font=("times new roman",20,"bold"),bg="yellow",fg="green",command=self.register_data).place(x=450,y=650,width=150,height=50)  

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_address.delete(0,END)
        self.txt_passd.delete(0,END)
        self.txt_date.delete(0,END)
        self.com.current(0)


    def register_data(self):
         if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_address.get()=="" or self.txt_passd.get()=="" or self.txt_date.get()=="":
             messagebox.showerror('Error',"All fields are required",parent=self.root)
         elif self.var_chk.get()==0:
             messagebox.showerror('Error',"Agree terms ",parent=self.root)
         else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="patient2")
                    cur=con.cursor()
                    cur.execute("select * from shrivatsa where email=%s",self.txt_email.get())
                    row=cur.fetchone()
                    print(row)
                    if row!=None:
                        messagebox.showerror("Error","user already exist,please try another",parent=self.root) 
                    else:
                        cur.execute("insert into shrivatsa(fname,lname,contactno,email,address,password,date,gender)values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.txt_address.get(),
                        self.txt_passd.get(),self.txt_date.get(),
                        self.com.get()

                    ) )

                        con.commit()
                        con.close()
                    #print(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.txt_address.get(),self.txt_passd.get())
                        messagebox.showinfo('success',"Register done",parent=self.root)
                        self.clear()
            

                except Exception as es:
                    messagebox.showerror("Error",f"error due to:{str(es)}",parent=self.root)     
                    print("error")   
root=Tk()
obj=Reg(root)
root.mainloop()
