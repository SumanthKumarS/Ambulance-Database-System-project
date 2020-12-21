from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql
from tkinter.filedialog import askopenfilename


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Window')
        self.root.geometry('1350x700+0+0')

        profile_frame = Frame(self.root , bd=4 , bg='white')
        profile_frame.place(x=220 , y=100 , height=400 , width=800)

        self.update_prf = ImageTk.PhotoImage(file='images/default.png')
        p_frm = Label(profile_frame , image=self.update_prf , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=40 , y=60 , width=200 , height=250)
        p_frm = Button(profile_frame , text='select' , command=self.photo_get , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=105 , y=250 , width=70 , height=50)



    def photo_get(self):
        profile_frame = Frame(self.root , bd=4 , bg='white')
        profile_frame.place(x=220 , y=100 , height=400 , width=800)
        self.file = askopenfilename()
        print(self.file)
        self.image = ImageTk.PhotoImage(file=self.file)
        print(self.image)
        p_frm = Label(profile_frame , image=self.image , bd=5 , relief=RIDGE , bg="white")
        p_frm.place(x=40 , y=60 , width=200 , height=250)
        print(p_frm)
        con = pymysql.connect(host='localhost' , user='root' , password='' , database='pos')
        cur = con.cursor()
        cur.execute('insert into pitch(photo) values(%s)' , (self.file))
        con.commit()
        con.close()

root = Tk()
obj = Register(root)
root.mainloop()