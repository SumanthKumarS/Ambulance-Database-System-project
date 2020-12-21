from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk
import requests
class Login :
    def __init__(self , root) :
        self.root2 = root
        self.root2.title("User home page")
        self.root2.geometry('1350x700+0+0')
        self.root2.config(bg='#08A3D2')
        self.root2.focus_force()
        self.image_dashbar = ImageTk.PhotoImage(file='images/amb2.png')
        frame10 = Frame(self.root2 , bd=10 , bg='light sea green' , relief=GROOVE).place(x=0 , y=0 , height=85 ,
                                                                                         width=1350)
        title = Label(frame10 , text='Welcome' , image=self.image_dashbar , compound=RIGHT ,
                      font=('times new roman' , 40 , 'bold') , bg='light sea green' , fg='blue')
        title.place(x=405 , y=15 , height=60 , width=600)

        frame12 = Frame(self.root2 , bd=4 , bg='deep sky blue')
        frame12.place(x=0 , y=85 , width=109 , height=640)

        self.home = ImageTk.PhotoImage(file='images/house.png')
        btn = Button(frame12 , image=self.home,command=self.home_page , bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=0 , width=92 , height=100)
        self.prof = ImageTk.PhotoImage(file='images/prof.png')
        btn1 = Button(frame12 , image=self.prof , command=self.profile_page , bg='light sea green' , bd=5 ,
                      relief=GROOVE , cursor='hand2').place(x=0 , y=104 , width=92 , height=100)
        self.update = ImageTk.PhotoImage(file='images/update.png')
        btn = Button(frame12 , image=self.update , bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=208 , width=92 , height=100)
        self.logout = ImageTk.PhotoImage(file='images/logout.png')
        btn = Button(frame12 , image=self.logout , bg='light sea green' , bd=5 ,
                     relief=GROOVE , cursor='hand2').place(x=0 , y=312 , width=92 , height=100)

        self.frame22 = Frame(self.root2 , bd=4 , bg='white')
        self.frame22.place(x=100 , y=85 , width=1250 , height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame22 , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 ,
                                                                                height=608)

    def home_page(self) :
        self.frame22 = Frame(self.root2 , bd=4 , bg='white')
        self.frame22.place(x=100 , y=85 , width=1250 , height=640)

        self.left = ImageTk.PhotoImage(file="images/reguserbck2.jpg")
        left = Label(self.frame22 , image=self.left , bg='deep sky blue').place(x=0 , y=0 , width=1242 , height=608)

        self.message = Label(self.frame22, font=('times new roman' , 50 , 'bold') , bg='deep sky blue' , fg='#d77337').place(x=200 ,y=200)

        r = requests.get('https://get.geojs.io/')

        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        ipAdd = ip_request.json()['ip']

        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        geo_request = requests.get(url)
        self.geo_data = geo_request.json()
        self.send_reqst = 'Requesting for Ambulance'

        btn_for_request = Button(self.frame22 , text='Request for Ambulance',command=self.send_request , font=('times new roman' , 20 , 'bold'),bd=5,relief=GROOVE).place(x=450 ,y=300)

    def profile_page(self):
        profile_frame = Frame(self.frame22 , bd=4 , bg='white')
        profile_frame.place(x=220 , y=100 , height=400 , width=800)
        profile_frame2 = Frame(profile_frame , bd=4 , bg='white')
        profile_frame2.place(x=10 , y=320 , height=70 , width=770)

        id = Label(profile_frame , text='ID' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        id.place(x=250 , y=60 , height=20 , width=70)
        self.id_txt = Entry(profile_frame, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        self.id_txt.place(x=350 , y=60 , height=20 , width=130)

        name = Label(profile_frame , text='Name' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        name.place(x=510 , y=60 , height=20 , width=70)
        self.name_txt = Entry(profile_frame, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        self.name_txt.place(x=610 , y=60 , height=20 , width=130)

        email = Label(profile_frame , text='Email ID' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        email.place(x=250 , y=100 , height=20 , width=70)
        self.email_txt = Entry(profile_frame, font=('times new roman' , 13 , 'bold') , bd=0 , state='readonly')
        self.email_txt.place(x=350 , y=100 , height=20 , width=130)

        gender = Label(profile_frame , text='Gender' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        gender.place(x=510 , y=100 , height=20 , width=70)
        self.cmb_quest = Entry(profile_frame, font=('times new roman' , 12) , bd=0 ,justify=CENTER , state='readonly')
        self.cmb_quest.place(x=610 , y=100 , height=20 , width=130)

        phone = Label(profile_frame , text='phone number' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        phone.place(x=300 , y=140 , height=20 , width=150)
        self.phone_txt = Entry(profile_frame, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        self.phone_txt.place(x=510 , y=140 , height=20 , width=150)

        dob = Label(profile_frame , text='D O B' , bg='white' , fg='black' , font=('times new roman' , 15 , 'bold'))
        dob.place(x=250 , y=180 , height=20 , width=70)
        self.dob_txt = Entry(profile_frame, font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        self.dob_txt.place(x=350 , y=180 , height=20 , width=130)

        address = Label(profile_frame , text='Address' , bg='white' , fg='black' ,font=('times new roman' , 15 , 'bold'))
        address.place(x=510 , y=180 , height=20 , width=70)
        self.address_txt = Entry(profile_frame,font=('times new roman' , 13 , 'bold') , bd=0 ,state='readonly')
        self.address_txt.place(x=610 , y=180 , height=20 , width=130)

        self.back_btn = ImageTk.PhotoImage(file='images/back.png')
        self.up_btn = Button(profile_frame , text="Update" , image=self.back_btn , command=self.home_page ,font=('times new roman' , 13 , 'bold') , bg='white' , bd=0)
        self.up_btn.place(x=700 , y=270 , height=40 , width=50)

    def send_request(self):
        if self.send_reqst == 'Requesting for Ambulance':
            print(self.send_reqst)

            print('Latitude coordinates' , self.geo_data['latitude'])
            print('Longitude coordinates' , self.geo_data['longitude'])

            print(self.geo_data['city'])
            print(self.geo_data['region'])
            print(self.geo_data['country'])



root = Tk()
obj = Login(root)
root.mainloop()