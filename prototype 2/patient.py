from tkinter import*
root=Tk()
root.title("patient details")
root.geometry("800x400+200+50")
root.config(bg="yellow")
root.resizable(True,True)
title=Label(root,text="PATIENT DETAILS",font=("impact",40),bg="black",fg="red").place(x=0,y=0,relwidth=1)
lbl_patientname=Label(root,text="PATIENTNAME",font=("times new roman",30),bg="yellow").place(x=30,y=180)
lbl_address=Label(root,text="ADRESS",font=("times new roman",30),bg="yellow").place(x=30,y=240)
lbl_email=Label(root,text="EMAIL",font=("times new roman",30),bg="yellow").place(x=30,y=300)
lbl_gender=Label(root,text="GENDER",font=("times new roman",30),bg="yellow").place(x=30,y=360)




txt_patientname=Entry(root,font=("times new roman",15)).place(x=350,y=200,width=500,height=40)
txt_address=Entry(root,font=("times new roman",15)).place(x=350,y=250,width=500,height=40)
txt_email=Entry(root,font=("times new roman",15)).place(x=350,y=300,width=500,height=40)
male=Radiobutton(root,text="Male",value="male",font=("times new roman",25),bg="yellow").place(x=350,y=350)
female=Radiobutton(root,text="Female",value="female",font=("times new roman",25),bg="yellow").place(x=490,y=350)

check_=Checkbutton(root,text="Accept out terms and Condition",font=("times new roman",12),bg="yellow").place(x=350,y=430)

btn=Button(root,text="Show Data",font=("times new roman",20,"bold"),bg="red",fg="green").place(x=350,y=500,width=150,height=50)


root.mainloop()
