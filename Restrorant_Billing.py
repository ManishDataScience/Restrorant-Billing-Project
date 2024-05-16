from tkinter import*

root=Tk()
root.geometry("1000x550")
root.title("Billing Management of Cube Stop")
root.resizable(False,False)

def Reset():
        entry_dosa.delete(0,END)
        entry_cookies.delete(0,END)
        entry_tea.delete(0,END)
        entry_coffee.delete(0,END)
        entry_Juice.delete(0,END)
        entry_samosa.delete(0,END)
        entry_eggs.delete(0,END)

def Total():
        
        try:a1=int(Dosa.get())
        except:a1=0

        try:a2=int(Cookies.get())
        except:a2=0

        try:a3=int(Tea.get())
        except:a3=0

        try:a4=int(Coffee.get())
        except:a4=0

        try:a5=int(Juice.get())
        except:a5=0

        try:a6=int(samosa.get())
        except:a6=0

        try:a7=int(Eggs.get())
        except:a7=0

        #define cost of each item per quantity
        

        c1=50*a1
        c2=30*a2
        c3=10*a3
        c4=100*a4
        c5=50*a5
        c6=50*a6
        c7=8*a7

        lbl_total=Label(f2,font=('aria',20,'bold',),text="Total",width=16,fg="lightyellow",bg="black")
        lbl_total.place(x=0,y=50)


        entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
        entry_total.place(x=20,y=100)

        totalcost=c1+c2+c3+c4+c5+c6+c7
        String_bill="Rs",str('%.2f' %totalcost)
        Total_bill.set(String_bill)


        
Label(text="Bill Mangament Anand  Food Restorant",bg="blue",fg="yellow",font=("calibri",33),width="300",height="2").pack()

#MENU CARD

f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)


Label(f,text="Menu",font=("Gabfiola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa...........Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cookies........Rs.30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Tea............Rs.10/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coffee.........Rs.100/cup",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Juice..........Rs.50/glass",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Samosa.........Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Eggs...........Rs.8/egg",fg="black",bg="lightgreen").place(x=10,y=260)

#BiLL
f2=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)


Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)


#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()


Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
samosa=StringVar()
Eggs=StringVar()
Total_bill=StringVar()




#Lable
lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue4")
lbl_Tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")
lbl_Coffee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="blue4")
lbl_Juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")
lbl_samosa=Label(f1,font=("aria",20,'bold'),text="Samosa",width=12,fg="blue4")
lbl_Eggs=Label(f1,font=("aria",20,'bold'),text="Eggs",width=12,fg="blue4")

lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_Coffee.grid(row=4,column=0)
lbl_Juice.grid(row=5,column=0)
lbl_samosa.grid(row=6,column=0)
lbl_Eggs.grid(row=7,column=0)


#Entry
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="lightpink")
entry_cookies=Entry(f1,font=("aria",20,'bold'),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_coffee=Entry(f1,font=("aria",20,'bold'),textvariable=Coffee,bd=6,width=8,bg="lightpink")
entry_Juice=Entry(f1,font=("aria",20,'bold'),textvariable=Juice,bd=6,width=8,bg="lightpink")
entry_samosa=Entry(f1,font=("aria",20,'bold'),textvariable=samosa,bd=6,width=8,bg="lightpink")
entry_eggs=Entry(f1,font=("aria",20,'bold'),textvariable=Eggs,bd=6,width=8,bg="lightpink")


entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_tea.grid(row=3,column=1)
entry_coffee.grid(row=4,column=1)
entry_Juice.grid(row=5,column=1)
entry_samosa.grid(row=6,column=1)
entry_eggs.grid(row=7,column=1)


#Buttona

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_Total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_Total.grid(row=8,column=1)


root.mainloop()