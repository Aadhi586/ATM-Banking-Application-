import mysql.connector as m
from tkinter import *
from tkinter import ttk
import datetime as d
d5=0
d14=0
def atm(x=0):
    global l
    global x1,y1,l
    x1=m.connect(host="localhost",user="root",passwd="2453",database="proj")
    y1=x1.cursor()
    y1.execute("select * from atm")
    l=y1.fetchall()
    if x==4:
        w4.destroy()
    elif x==18:
        w18.destroy()
    elif x==16:
        w16.destroy()
    elif x==12:
        w12.destroy()
    global w1
    w1=Tk()
    p=PhotoImage(file="pig.png")
    icon=PhotoImage(file='2354424-200.png')
    w1.iconphoto(True,icon)
    w1.title("Piggy Bank")
    w1.geometry("720x800")
    w1.config(background="#f8d8e7")
    f1=Frame(w1,bg="#f8d8e7")
    f1.pack()
    Label(f1,text="Welcome \nTo Piggy bank",
          font=("Perpetua",40),
          fg="#e985b4",
          bg="#f8d8e7",
          pady=30,
          image=p,
          compound="bottom").grid(row=0,column=0)
    Button(f1,text="Continue",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=Pass,bd=3).grid(row=2,column=0)
    w1.mainloop()
def Pass():
    w1.destroy()
    global w2
    global en2
    w2=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w2.iconphoto(True,icon)
    w2.title("Piggy Bank")
    w2.geometry("520x400")
    w2.config(background="#f8d8e7")
    f2=Frame(w2,bg="#f8d8e7")
    f2.pack()
    Label(f2,text="Enter your password ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7",pady=40).grid(row=0,column=0)
    en2=Entry(f2,font=("Perpetua",20),show="*")
    en2.grid(row=1,column=0,pady=20)
    Button(f2,text="Submit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=pin).grid(row=3,column=0)
def pin():
    a=en2.get()
    w2.destroy()
    for i in range(len(l)):
        if str(l[i][1])==str(a):
            pin2(list(l[i]))
            break
    else:
        global w4
        w4=Tk()
        icon=PhotoImage(file='2354424-200.png')
        w4.iconphoto(True,icon)
        w4.title("Piggy Bank")
        w4.geometry("520x400")
        w4.config(background="#f8d8e7")
        f4=Frame(w4,bg="#f8d8e7")
        f4.pack()
        Label(f4,text="Account not found !",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7",pady=10).grid(row=0,column=0)            
        Label(f4,text="Try again!",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0) 
        Button(f4,text="Ok",
               font=("Perpetua",20),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:atm(4)).grid(row=2,column=0,pady=50) 
def pin2(l):
    global w3
    global en3
    w3=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w3.iconphoto(True,icon)
    w3.title("Piggy Bank")
    w3.geometry("520x400")
    w3.config(background="#f8d8e7")
    f3=Frame(w3,bg="#f8d8e7")
    f3.pack()
    Label(f3,text="Enter your pin ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=30)
    en3=Entry(f3,font=("Perpetua",20),show="*")
    en3.grid(row=1,column=0)
    Button(f3,text="Submit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:pin1(l)).grid(row=3,column=0,pady=30)       
def pin1(l):
    global d5
    global w5
    global en5
    global w18
    if d5==0:
        b=en3.get()
        w3.destroy()
    elif d5==2 and str(l[0])!=str(en5.get()):
        b='End'
        w5.destroy()
        w18=Tk()
        icon=PhotoImage(file='2354424-200.png')
        w18.iconphoto(True,icon)
        w18.title("Piggy Bank")
        w18.geometry("520x400")
        w18.config(background="#f8d8e7")
        f18=Frame(w18,bg="#f8d8e7")
        f18.pack()
        d5=0
        Label(f18,text="You have Reached maximum tries!",font=("Perpetua",28),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)           
        Label(f18,text="Account locked",font=("Perpetua",28),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
        Button(f18,text="Ok",
               font=("Perpetua",20),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:atm(18)).grid(row=2,column=0,pady=20)
    else:
        b=en5.get()
        w5.destroy()
    if str(l[0])==str(b):
        menu(l)
    elif b=='End':
        pass
    else:
        if d5<2:
            d5+=1
            w5=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w5.iconphoto(True,icon)
            w5.title("Piggy Bank")
            w5.geometry("520x400")
            w5.config(background="#f8d8e7")
            f5=Frame(w5,bg="#f8d8e7")
            f5.pack()
            Label(f5,text="Wrong pin!",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0)
            Label(f5,text="Enter your pin again! ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            en5=Entry(f5,font=("Perpetua",20),show="*")
            en5.grid(row=2,column=0,pady=30)
            Button(f5,text="Submit",
                   font=("Perpetua",18),
                   fg="#e985b4",bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:pin1(l)).grid(row=3,column=0)
        else:
            d5+=1
def menu(l,g=0):
    if g==10:
        w10.destroy()
    elif g==20:
        w20.destroy()
    elif g==7:
        w7.destroy()
    elif g==11:
        w11.destroy()
    elif g==17:
        w17.destroy()
    else:
        pass
    global w6
    w6=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w6.iconphoto(True,icon)
    w6.title("Piggy Bank")
    w6.geometry("520x400")
    w6.config(background="#f8d8e7")
    f6=Frame(w6,bg="#f8d8e7")
    f6.pack()
    Label(f6,text="Welcome "+str(l[2]),font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=1,columnspan=2)
    Label(f6,text="Choose option:",font=("Perpetua",22),fg="#e985b4",bg="#f8d8e7",padx=5,pady=20).grid(row=1,column=1,columnspan=2)
    Button(f6,text="Cash Withdrawal",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:withd(l)).grid(row=2,column=2,pady=2,padx=20)
    Button(f6,text="Cash Deposit",
           font=("Perpetua",18),
           fg="#e985b4",bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:dep(l),
           padx=18).grid(row=3,column=2,pady=10)
    Button(f6,text="Balance enquiry",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:enq(l)).grid(row=2,column=1,padx=50)
    Button(f6,text="Change Pin",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:changepin(l),
           padx=21).grid(row=3,column=1)
    Button(f6,text="Transanction details",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:Trans(l),
           padx=21).grid(row=4,column=1)
    Button(f6,text="Exit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:Exit(l,6),
           padx=58).grid(row=4,column=2,pady=2)
def withd(l):
    w6.destroy()
    global w7
    w7=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w7.iconphoto(True,icon)
    w7.title("Piggy Bank")
    w7.geometry("520x400")
    w7.config(background="#f8d8e7")
    f7=Frame(w7,bg="#f8d8e7")
    f7.pack()
    Label(f7,text="Choose option:",font=("Perpetua",25),fg="#e985b4",bg="#f8d8e7",pady=20).grid(row=0,column=1)
    Button(f7,text="Current A/C",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:withd1(l,2)).grid(row=1,column=2,pady=25)
    Button(f7,text="Savings A/C",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:withd1(l,1)).grid(row=1,column=0)
    Button(f7,text="Back",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:menu(l,7)).grid(row=2,column=2)
def withd1(l,x,z=7):
    if z==7:
        w7.destroy()
    elif z==9:
        w9.destroy()
    global w8
    global en8
    w8=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w8.iconphoto(True,icon)
    w8.title("Piggy Bank")
    w8.geometry("520x400")
    w8.config(background="#f8d8e7")
    f8=Frame(w8,bg="#f8d8e7")
    f8.pack()
    Label(f8,text="Enter amount to withdraw: ",font=("Perpetua",38),fg="#e985b4",bg="#f8d8e7",pady=38).grid(row=0,column=0)
    en8=Entry(f8,font=("Perpetua",20))
    en8.grid(row=1,column=0,pady=20)
    Button(f8,text="Submit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:withd2(l,x,1)).grid(row=2,column=0)
def withd2(l,x,r):
    global w9
    if r==1:
        global w9
        global w10
        s=int(en8.get())
        w8.destroy()
    if x==1:
        if s>100000:
            w9=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w9.iconphoto(True,icon)
            w9.title("Piggy Bank")
            w9.geometry("520x200")
            w9.config(background="#f8d8e7")
            f9=Frame(w9,bg="#f8d8e7")
            f9.pack()
            Label(f9,text="Amount above ₹1,00,000 cannot be withdrawn in one go!",
                  font=("Perpetua",16),
                  fg="#e985b4",
                  bg="#f8d8e7").grid(row=0,column=0,pady=20)            
            Label(f9,text="Try again!",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            Button(f9,text="Ok",
                   font=("Perpetua",20),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:withd1(l,x,9)).grid(row=2,column=0,pady=20)
        elif s>l[4]-1000:
            w9=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w9.iconphoto(True,icon)
            w9.title("Piggy Bank")
            w9.geometry("520x400")
            w9.config(background="#f8d8e7")
            f9=Frame(w9,bg="#f8d8e7")
            f9.pack()
            Label(f9,text="Insuficient balance!",font=("Perpetua",16),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)            
            Label(f9,text="Try again!",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            Button(f9,text="Ok",
                   font=("Perpetua",20),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:withd1(l,x,9)).grid(row=2,column=0,pady=20)   
        else:
            y1.execute("update atm set savings={} where acc={}".format(l[4]-s,l[3]))
            x1.commit()
            y1.execute('select * from {}'.format("a_"+str(l[3])))
            s2=y1.fetchall()
            c=d.datetime.now()
            f=c.strftime('%H:%M:%S')
            y1.execute("insert into {} values({},'savings','withdraw',{},'{}','{}')".format("a_"+str(l[3]),len(s2)+1,s,str(d.date.today()),str(f)))
            l[4]=l[4]-s
            w10=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w10.iconphoto(True,icon)
            w10.title("Piggy Bank")
            w10.geometry("520x400")
            w10.config(background="#f8d8e7")
            f10=Frame(w10,bg="#f8d8e7")
            f10.pack()
            Label(f10,text="Transaction succesfull",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=1,columnspan=2)
            Label(f10,text="Do you want to continue?",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=1,columnspan=2)
            Button(f10,text="Yes",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:menu(l,10)).grid(row=2,column=1,pady=50)
            Button(f10,text="No",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:Exit(l,10)).grid(row=2,column=2)
    else:
        if s>100000:
            w9=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w9.iconphoto(True,icon)
            w9.title("Piggy Bank")
            w9.geometry("520x200")
            w9.config(background="#f8d8e7")
            f9=Frame(w9,bg="#f8d8e7")
            f9.pack()
            Label(f9,text="Amount above ₹1,00,000 cannot be withdrawn in one go!",
                  font=("Perpetua",16),
                  fg="#e985b4",
                  bg="#f8d8e7").grid(row=0,column=0,pady=20)            
            Label(f9,text="Try again!",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            Button(f9,text="Ok",
                   font=("Perpetua",20),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:withd1(l,x,9)).grid(row=2,column=0,pady=20)
        elif s>l[5]-1000:
            w9=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w9.iconphoto(True,icon)
            w9.title("Piggy Bank")
            w9.geometry("520x400")
            w9.config(background="#f8d8e7")
            f9=Frame(w9,bg="#f8d8e7")
            f9.pack()
            Label(f9,text="Insuficient balance!",font=("Perpetua",16),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)            
            Label(f9,text="Try again!",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            Button(f9,text="Ok",
                   font=("Perpetua",20),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:withd1(l,x,9)).grid(row=2,column=0,pady=20)   
        else:
            y1.execute("update atm set current={} where acc={}".format(l[5]-s,l[3]))
            x1.commit()
            y1.execute('select * from {}'.format("a_"+str(l[3])))
            s2=y1.fetchall()
            c=d.datetime.now()
            f=c.strftime('%H:%M:%S')
            y1.execute("insert into {} values({},'current','withdraw',{},'{}','{}')".format("a_"+str(l[3]),len(s2)+1,s,str(d.date.today()),str(f)))
            x1.commit()
            l[5]=l[5]-s
            w10=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w10.iconphoto(True,icon)
            w10.title("Piggy Bank")
            w10.geometry("520x400")
            w10.config(background="#f8d8e7")
            f10=Frame(w10,bg="#f8d8e7")
            f10.pack()
            Label(f10,text="Transaction succesfull",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=1,columnspan=2)
            Label(f10,text="Do you want to continue?",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=1,columnspan=2)
            Button(f10,text="Yes",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:menu(l,10)).grid(row=2,column=1,pady=50)
            Button(f10,text="No",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:Exit(l,10)).grid(row=2,column=2)
def dep(l):
    w6.destroy()
    global w7
    w7=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w7.iconphoto(True,icon)
    w7.title("Piggy Bank")
    w7.geometry("520x400")
    w7.config(background="#f8d8e7")
    f7=Frame(w7,bg="#f8d8e7")
    f7.pack()
    Label(f7,text="Choose option:",font=("Perpetua",25),fg="#e985b4",bg="#f8d8e7",pady=20).grid(row=0,column=1)
    Button(f7,text="Current A/C",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:dep1(l,2)).grid(row=1,column=2,pady=25)
    Button(f7,text="Savings A/C",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:dep1(l,1)).grid(row=1,column=0)
    Button(f7,text="Back",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:menu(l,7)).grid(row=2,column=2)
def dep1(l,x,z=7):
    if z==9:
        w9.destroy()
    elif z==7:
        w7.destroy()
    global w8
    global en8
    w8=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w8.iconphoto(True,icon)
    w8.title("Piggy Bank")
    w8.geometry("520x400")
    w8.config(background="#f8d8e7")
    f8=Frame(w8,bg="#f8d8e7")
    f8.pack()
    Label(f8,text="Enter amount to deposit: ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7",pady=40).grid(row=0,column=0)
    en8=Entry(f8,font=("Perpetua",20))
    en8.grid(row=1,column=0,pady=20)
    Button(f8,text="Submit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:dep2(l,x,1)).grid(row=2,column=0)
def dep2(l,x,r):
    if r==1:
        global w9
        global w10
        s=int(en8.get())
        w8.destroy()
    if x==1:
        if s>1000000:
            w9=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w9.iconphoto(True,icon)
            w9.title("Piggy Bank")
            w9.geometry("520x200")
            w9.config(background="#f8d8e7")
            f9=Frame(w9,bg="#f8d8e7")
            f9.pack()
            Label(f9,text="Amount above ₹10,00,000 cannot be deposited in one go!",
                  font=("Perpetua",16),
                  fg="#e985b4",
                  bg="#f8d8e7").grid(row=0,column=0,pady=20)            
            Label(f9,text="Try again!",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            Button(f9,text="Ok",
                   font=("Perpetua",20),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:dep1(l,x,9)).grid(row=2,column=0,pady=20)
        else:
            y1.execute("update atm set savings={} where acc={}".format(l[4]+s,l[3]))
            x1.commit()
            y1.execute('select * from {}'.format("a_"+str(l[3])))
            s2=y1.fetchall()
            c=d.datetime.now()
            f=c.strftime('%H:%M:%S')
            y1.execute("insert into {} values({},'savings','deposit',{},'{}','{}')".format("a_"+str(l[3]),len(s2)+1,s,str(d.date.today()),str(f)))
            x1.commit()
            l[4]=l[4]+s
            w10=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w10.iconphoto(True,icon)
            w10.title("Piggy Bank")
            w10.geometry("520x400")
            w10.config(background="#f8d8e7")
            f10=Frame(w10,bg="#f8d8e7")
            f10.pack()
            Label(f10,text="Transaction succesfull",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=1,columnspan=2)
            Label(f10,text="Do you want to continue?",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=1,columnspan=2)
            Button(f10,text="Yes",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:menu(l,10)).grid(row=2,column=1,pady=50)
            Button(f10,text="No",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:Exit(l,10)).grid(row=2,column=2)
    else:
        if s>1000000:
            w9=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w9.iconphoto(True,icon)
            w9.title("Piggy Bank")
            w9.geometry("520x200")
            w9.config(background="#f8d8e7")
            f9=Frame(w9,bg="#f8d8e7")
            f9.pack()
            Label(f9,text="Amount above ₹10,00,000 cannot be deposited in one go!",
                  font=("Perpetua",16),
                  fg="#e985b4",
                  bg="#f8d8e7").grid(row=0,column=0,pady=20)            
            Label(f9,text="Try again!",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            Button(f9,text="Ok",
                   font=("Perpetua",20),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:dep1(l,x,9)).grid(row=2,column=0,pady=20)
        else:
            y1.execute("update atm set current={} where acc={}".format(l[5]+s,l[3]))
            x1.commit()
            y1.execute('select * from {}'.format("a_"+str(l[3])))
            s2=y1.fetchall()
            c=d.datetime.now()
            f=c.strftime('%H:%M:%S')
            y1.execute("insert into {} values({},'current','deposit',{},'{}','{}')".format("a_"+str(l[3]),len(s2)+1,s,str(d.date.today()),str(f)))
            x1.commit()
            l[5]=l[5]+s
            w10=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w10.iconphoto(True,icon)
            w10.title("Piggy Bank")
            w10.geometry("520x400")
            w10.config(background="#f8d8e7")
            f10=Frame(w10,bg="#f8d8e7")
            f10.pack()
            Label(f10,text="Transaction succesfull",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=1,columnspan=2)
            Label(f10,text="Do you want to continue?",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=1,columnspan=2)
            Button(f10,text="Yes",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:menu(l,10)).grid(row=2,column=1,pady=50)
            Button(f10,text="No",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:Exit(l,10)).grid(row=2,column=2)
def enq(l):
    w6.destroy()
    global w11
    w11=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w11.iconphoto(True,icon)
    w11.title("Piggy Bank")
    w11.geometry("520x400")
    w11.config(background="#f8d8e7")
    f11=Frame(w11,bg="#f8d8e7")
    f11.pack()
    Label(f11,text="Your Savings A\C balance is ₹"+str(l[4]),
          font=("Perpetua",20),
          fg="#e985b4",
          bg="#f8d8e7").grid(row=0,column=1,columnspan=2,pady=20)
    Label(f11,text="Your Current A\C balance is ₹"+str(l[5]),
          font=("Perpetua",20),
          fg="#e985b4",
          bg="#f8d8e7").grid(row=1,column=1,columnspan=2,pady=20)
    Label(f11,text="Do you want to continue?",
          font=("Perpetua",20),
          fg="#e985b4",
          bg="#f8d8e7").grid(row=2,column=1,columnspan=2)
    Button(f11,text="Yes",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:menu(l,11)).grid(row=3,column=1,pady=50)
    Button(f11,text="No",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:Exit(l,11)).grid(row=3,column=2)
def Exit(l,i=0):
    if i==6:
        w6.destroy()
    elif i==10:
        w10.destroy()
    elif i==11:
        w11.destroy()
    elif i==17:
        w17.destroy()
    else:
        pass
    global w12
    w12=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w12.iconphoto(True,icon)
    w12.title("Piggy Bank")
    w12.config(background="#f8d8e7")
    w12.geometry("520x400")
    f12=Frame(w12,bg="#f8d8e7")
    f12.pack()
    Label(f12,text="Thank you "+str(l[2]),font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7",pady=10).grid(row=0,column=0,pady=20)
    Label(f12,text="Please visit again!",font=("Perpetua",28),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
    Button(f12,text="Ok",
           font=("Perpetua",20),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:atm(12)).grid(row=2,column=0,pady=20)
def changepin(l):
    w6.destroy()
    global w13
    global en13
    w13=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w13.iconphoto(True,icon)
    w13.title("Piggy Bank")
    w13.geometry("520x400")
    w13.config(background="#f8d8e7")
    f13=Frame(w13,bg="#f8d8e7")
    f13.pack()
    Label(f13,text="Enter your current pin: ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7",pady=40).grid(row=0,column=0)
    en13=Entry(f13,font=("Perpetua",20),show="*")
    en13.grid(row=1,column=0,pady=20)
    Button(f13,text="Submit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:change_pin(l)).grid(row=3,column=0)
def change_pin(l):
    global d14
    global w14
    global en14
    global w16
    if d14==0:
        b=en13.get()
        w13.destroy()
    elif d14==2:
        b='End'
        w14.destroy()
        w16=Tk()
        icon=PhotoImage(file='2354424-200.png')
        w16.iconphoto(True,icon)
        w16.title("Piggy Bank")
        w16.geometry("520x400")
        w16.config(background="#f8d8e7")
        f16=Frame(w16,bg="#f8d8e7")
        f16.pack()
        d14=0
        Label(f16,text="You have Reached maximum tries!",font=("Perpetua",28),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)           
        Label(f16,text="Account locked",font=("Perpetua",28),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
        Button(f16,text="Ok",
               font=("Perpetua",20),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:atm(16)).grid(row=2,column=0,pady=20)
        w16.mainloop()
    else:
        b=en14.get()
        w14.destroy()
    if str(l[0])==str(b):
        newpin(l,d14,14)
    elif b=='End':
        pass
    else:
        if d14<2:
            d14+=1
            w14=Tk()
            icon=PhotoImage(file='2354424-200.png')
            w14.iconphoto(True,icon)
            w14.title("Piggy Bank")
            w14.geometry("520x400")
            w14.config(background="#f8d8e7")
            f14=Frame(w14,bg="#f8d8e7")
            f14.pack()
            Label(f14,text="Wrong pin!",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0)
            Label(f14,text="Enter your pin again! ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
            en14=Entry(f14,font=("Perpetua",20),show="*")
            en14.grid(row=2,column=0,pady=30)
            Button(f14,text="Submit",
                   font=("Perpetua",18),
                   fg="#e985b4",
                   bg="#f8d8e7",
                   activeforeground="#e985b4",
                   activebackground="#f8d8e7",
                   command=lambda:change_pin(l)).grid(row=3,column=0)
        else:
            d14+=1
def newpin(l,d14=0,x=0):
    if x==1:
        w17.destroy()
    elif x==50:
        w50.destroy()
    global w15
    global en15
    global en151
    w15=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w15.iconphoto(True,icon)
    w15.title("Piggy Bank")
    w15.geometry("520x400")
    w15.config(background="#f8d8e7")
    f15=Frame(w15,bg="#f8d8e7")
    f15.pack()
    Label(f15,text="Enter new pin: ",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)
    en15=Entry(f15,font=("Perpetua",20),show='*')
    en15.grid(row=1,column=0,pady=20)
    Label(f15,text="Confirm new pin: ",font=("Perpetua",20),fg="#e985b4",bg="#f8d8e7").grid(row=2,column=0,pady=20)
    en151=Entry(f15,font=("Perpetua",20),show="*")
    en151.grid(row=3,column=0,pady=20)
    Button(f15,text="Submit",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:newpin1(l)).grid(row=4,column=0)
def newpin1(l):
    global w17
    global w50
    c=en15.get()
    d=en151.get()
    w15.destroy()
    if c==d:
        try:
            c=int(c)
            x=0
        except:
            x=2
    else:
        x=1
    if x==0:
        y1.execute("update atm set pin={} where acc={}".format(c,l[3]))
        x1.commit()
        l[0]=c
        w17=Tk()
        icon=PhotoImage(file='2354424-200.png')
        w17.iconphoto(True,icon)
        w17.title("Piggy Bank")
        w17.geometry("520x400")
        w17.config(background="#f8d8e7")
        f17=Frame(w17,bg="#f8d8e7")
        f17.pack()
        Label(f17,text="Pin changed sucessfully!",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=1,columnspan=2,pady=20)
        Label(f17,text="Do you want to continue?",font=("Perpetua",30),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=1,columnspan=2)
        Button(f17,text="Yes",
               font=("Perpetua",18),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:menu(l,17)).grid(row=2,column=1,pady=50)
        Button(f17,text="No",
               font=("Perpetua",18),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:Exit(l,17)).grid(row=2,column=2)
    elif x==1:
        w17=Tk()
        icon=PhotoImage(file='2354424-200.png')
        w17.iconphoto(True,icon)
        w17.title("Piggy Bank")
        w17.geometry("520x400")
        w17.config(background="#f8d8e7")
        f17=Frame(w17,bg="#f8d8e7")
        f17.pack()
        Label(f17,text="Pin mis-match!",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)
        Label(f17,text="Enter your new pin again! ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
        Button(f17,text="Ok",
               font=("Perpetua",20),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:newpin(l,x=1)).grid(row=2,column=0,pady=20)
    else:
        w50=Tk()
        icon=PhotoImage(file='2354424-200.png')
        w50.iconphoto(True,icon)
        w50.title("Piggy Bank")
        w50.geometry("520x400")
        w50.config(background="#f8d8e7")
        f50=Frame(w50,bg="#f8d8e7")
        f50.pack()
        Label(f50,text="Pin not a number!",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=0,column=0,pady=20)
        Label(f50,text="Enter your new pin again! ",font=("Perpetua",40),fg="#e985b4",bg="#f8d8e7").grid(row=1,column=0)
        Button(f50,text="Ok",
               font=("Perpetua",20),
               fg="#e985b4",
               bg="#f8d8e7",
               activeforeground="#e985b4",
               activebackground="#f8d8e7",
               command=lambda:newpin(l,x=1)).grid(row=2,column=0,pady=20)          
def Trans(y):
    global w20
    x=y[3]
    w6.destroy()
    y1.execute('Select * from {}'.format("a_"+str(x)))
    s=y1.fetchall()
    w20=Tk()
    icon=PhotoImage(file='2354424-200.png')
    w20.iconphoto(True,icon)
    w20.title("Piggy Bank")
    w20.geometry("550x450")
    w20.config(background="#f8d8e7")
    f20=Frame(w20,bg="#f8d8e7")
    f20.pack()
    mt=ttk.Treeview(f20,columns=('S.no','Date','Time','Account','Transation\ntype','Amount'),show='headings')
    mt.column('#0',width=0,stretch=NO)
    mt.column('S.no',anchor=W,width=60)
    mt.column('Date',anchor=W,width=100)
    mt.column('Time',anchor=W,width=100)
    mt.column('Account',anchor=W,width=100)
    mt.column('Transation\ntype',anchor=CENTER,width=110)
    mt.column('Amount',anchor=W,width=100)
    mt.heading('#0',text='',anchor=W)
    mt.heading('S.no',anchor=W,text='S.no')
    mt.heading('Date',anchor=W,text='Date')
    mt.heading('Time',anchor=W,text='Time')
    mt.heading('Account',anchor=W,text='Account')
    mt.heading('Transation\ntype',anchor=CENTER,text='Transation type')
    mt.heading('Amount',anchor=W,text='Amount')
    sty=ttk.Style()
    sty.theme_use("clam")
    sty.configure("Treeview",background="#f8d8e7",foreground="#e985b4",rowheight=35,feildbackground="#f8d8e7")
    sty.map("Treeview",background=[("selected","#e985b4")])
    d=0
    if len(s)>10:
        for i in range(len(s)-1,(len(s)-11),-1):
            mt.insert(parent='',index=d,iid=i,text='',values=(d+1,s[i][4],s[i][5],s[i][1],s[i][2],s[i][3]))
            d+=1
        mt.grid(row=0,column=0)
    else:
        for i in range(len(s)-1,0,-1):
            mt.insert(parent='',index=d,iid=i,text='',values=(d+1,s[i][4],s[i][5],s[i][1],s[i][2],s[i][3]))
            d+=1
        mt.grid(row=0,column=0)
    Button(f20,text="Continue",
           font=("Perpetua",18),
           fg="#e985b4",
           bg="#f8d8e7",
           activeforeground="#e985b4",
           activebackground="#f8d8e7",
           command=lambda:menu(y,20),bd=3).grid(row=2,column=0)    
atm()

    

