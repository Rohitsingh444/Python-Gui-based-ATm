from tkinter import *
import time

balance='1000'

Bank_Pin='123'



root=Tk()



def Balance_check():
    root = Tk()
    global balance
    root.title("my atm ")
    root.geometry("1000x600+120+120")
    root.configure(background="#3d3d5c")
    font = "orbitron 30 bold"
    l1 = Label(root, text="STATE BANK OF INDIA", font=font, background="#3d3d5c", foreground="white")
    l1.pack(side=TOP, pady=22)
    freelabel = Label(root, text="", font=font, background="#3d3d5c", foreground="white")
    freelabel.pack(side=TOP, pady=10)
    f = Frame(root, bg="#33334d")
    f.pack(fill="both", expand=True)
    l1=Label(f,text="Your current balance",font="orbitron 15 bold",bg="#33334d",fg="white")
    l1.pack(pady=8)
    balance_label = Label(f, text=balance, font="orbitron 15 bold", bg="#33334d", fg="white")
    balance_label.pack(pady=8)

    bottom_frame = Frame(root, bg="#33334d")
    bottom_frame.pack(fill="both", expand=True)
    back_button = Button(bottom_frame, text="Back", font="orbitron 15 ", activebackground='orange', bg="#29293d",
                         fg="white",
                         width="10", height="2", command=Banking_page)
    back_button.pack(side="left", padx=10, pady=5, anchor='s')

    def exit():
        root.destroy()

    Exit_button = Button(bottom_frame, text="Exit", font="orbitron 15 ", activebackground='orange', bg="#29293d",
                         fg="white",
                         width="10", height="2", command=exit)
    Exit_button.pack(side="right", padx=10, pady=5, anchor='s')

    bottom_frame2 = Frame(root, relief='raised', borderwidth=2)
    bottom_frame2.pack(fill='x', side='bottom')

    def tick():
        current_time = time.strftime('%I:%M %p').lstrip('0').replace('0', '')
        time1.config(text=current_time)
        time1.after(200, tick)

    time1 = Label(bottom_frame2, font=('orbitron', 19))
    time1.pack(side='right')
    tick()

def deposit():
    root = Tk()
    global balance
    root.title("my atm ")
    root.geometry("1000x600+120+120")
    root.configure(background="#3d3d5c")
    font = "orbitron 30 bold"
    l1 = Label(root, text="STATE BANK OF INDIA", font=font, background="#3d3d5c", foreground="white")
    l1.pack(side=TOP, pady=16)
    l2 = Label(root, text="Enter Amount", font="orbitron 15 bold", background="#3d3d5c", foreground="white")
    l2.pack(side=TOP, pady=15)

    f = Frame(root, bg="#33334d")
    f.pack(fill="both", expand=True)

    amount = StringVar()

    Amount= Entry(f, font=('orbitron',12), justify=CENTER,width=22, fg='white', bg="#29293d", textvariable=amount)
    Amount.pack( ipady=13,pady=10)

    def deposit_cash():
        global balance
        balance=str(int(balance)+int(Amount.get()))
        withdraw = Label(f, text=Amount.get() + " Rupees is successfully Deposit to your Bank Account", font=('orbitron', 19), fg='white',bg='#33334d')
        withdraw.pack(fill="both", expand=True, pady=10)
    B1 = Button(f, text="Deposit",font='orbitron', bg="#29293d", fg="white",borderwidth=3, width=19,height=3,command=deposit_cash)
    B1.pack(pady=6)
    bottom_frame=Frame(root,bg="#33334d")
    bottom_frame.pack(fill="both", expand=True)
    back_button= Button(bottom_frame, text="Back", font="orbitron 15 ", activebackground='orange', bg="#29293d", fg="white",
                width="10", height="2",command=Banking_page)
    back_button.pack(side="left", padx=10,pady=5,anchor='s')

    def exit():
        root.destroy()

    Exit_button = Button(bottom_frame, text="Exit", font="orbitron 15 ", activebackground='orange', bg="#29293d", fg="white",
                width="10", height="2", command=exit)
    Exit_button.pack(side="right", padx=10,pady=5,anchor='s')

    bottom_frame2 = Frame(root, relief='raised', borderwidth=2)
    bottom_frame2.pack(fill='x', side='bottom')

    def tick():
        current_time = time.strftime('%I:%M %p').lstrip('0').replace('0', '')
        time1.config(text=current_time)
        time1.after(200, tick)

    time1 = Label(bottom_frame2, font=('orbitron', 19))
    time1.pack(side='right')

    tick()


def withdraw():

    root = Tk()
    root.title("my atm ")
    root.geometry("1000x600+120+120")
    root.configure(background="#3d3d5c")
    font = "orbitron 30 bold"
    l1 = Label(root, text="STATE BANK OF INDIA", font=font, background="#3d3d5c", foreground="white")
    l1.pack(side=TOP, pady=16)


    l3 = Label(root, text="Enter amount you want to withdraw", font="orbitron 15 bold", background="#3d3d5c",
               foreground="white")
    l3.pack(side='top',pady=15)

    f = Frame(root, bg="#33334d")
    f.pack(fill="both", expand=True)
    amount = StringVar()

    Amount = Entry(f, font=('orbitron', 12), justify=CENTER, width=22, fg='white', bg="#29293d", textvariable=amount)
    Amount.pack(ipady=13, pady=10)

    def withdraw_cash():
        global balance
        if balance>=Amount.get():
            balance=str(int(balance)-int(Amount.get()))
            withdraw = Label(f, text=Amount.get()+" Rupees is successfully withdraw", font=('orbitron', 19), fg='white', bg='#33334d')
            withdraw.pack(fill="both", expand=True, pady=10)
        else:
            cant_withdraw = Label(f, text="Insufficient Balance", font=('orbitron', 19), fg='white', bg='#33334d')
            cant_withdraw.pack(fill="both", expand=True, pady=10)


    B1 = Button(f, text="Withdraw", font='orbitron', bg="#29293d", fg="white", borderwidth=3, width=19, height=3,
                command=withdraw_cash)
    B1.pack(pady=6)
    bottom_frame = Frame(root, bg="#33334d")
    bottom_frame.pack(fill="both", expand=True)
    back_button = Button(bottom_frame, text="Back", font="orbitron 15 ", activebackground='orange', bg="#29293d",
                         fg="white",
                         width="10", height="2", command=Banking_page)
    back_button.pack(side="left", padx=10, pady=5, anchor='s')

    def exit():
        root.destroy()

    L6 = Button(bottom_frame, text="Exit", font="orbitron 15 ", activebackground='orange', bg="#29293d", fg="white",
                width="10", height="2", command=exit)
    L6.pack(side="right", padx=10, pady=5, anchor='s')


    bottom_frame = Frame(root, relief='raised', borderwidth=2)
    bottom_frame.pack(fill='x', side='bottom')


    def tick():
        current_time = time.strftime('%I:%M %p').lstrip('0').replace('0','')
        time1.config(text=current_time)
        time1.after(200, tick)

    time1 = Label(bottom_frame, font=('orbitron', 19))
    time1.pack(side='right')

    tick()

    root.mainloop()
def  Change_password():

    root = Tk()
    root.title("my atm ")
    root.geometry("1000x600+120+120")
    root.configure(background="#3d3d5c")
    font = "orbitron 30 bold"
    l1 = Label(root, text="STATE BANK OF INDIA", font=font, background="#3d3d5c", foreground="white")
    l1.pack(side=TOP, pady=16)



    f = Frame(root, bg="#33334d")
    f.pack(fill="both", expand=True)
    l3 = Label(f, text="Enter New Pin", font="orbitron 15 bold", background="#33334d",foreground="white")
    l3.pack(side='top', pady=2)
    new_password = StringVar()
    new_password2 = StringVar()
    New_pin = Entry(f, font=('orbitron', 12), justify=CENTER, width=22, fg='white', bg="#29293d", textvariable=new_password,show='*')
    New_pin.pack(ipady=13, pady=5)
    l3 = Label(f, text="Renter New Pin", font="orbitron 15 bold", background="#33334d",foreground="white")
    l3.pack(side='top', pady=2)
    New_pin2 = Entry(f, font=('orbitron', 12), justify=CENTER, width=22, fg='white', bg="#29293d",textvariable=new_password2,show='*')
    New_pin2.pack(ipady=13)
    def change_pin():
        global  Bank_Pin
        if New_pin.get()!= New_pin2.get() :
            incorrect_pass = Label(f, text=" ", font=('orbitron', 19), fg='white', bg='#33334d')
            incorrect_pass.pack(fill="both", expand=True, pady=10)
            incorrect_pass['text'] = 'Pin not match'
        else:
            Bank_Pin=New_pin.get()
            correct_pass = Label(f, text="Pin Successfully Changed", font=('orbitron', 19), fg='white', bg='#33334d')
            correct_pass.pack(fill="both", expand=True, pady=10)




    B1 = Button(f, text="Change Pin", font='orbitron', bg="#29293d", fg="white", borderwidth=3, width=19, height=3,
                command=change_pin)
    B1.pack(pady=10)


    bottom_frame = Frame(root, bg="#33334d")
    bottom_frame.pack(fill="both", expand=True)
    back_button = Button(bottom_frame, text="Back", font="orbitron 15 ", activebackground='orange', bg="#29293d",
                         fg="white",
                         width="10", height="2", command=Banking_page)
    back_button.pack(side="left", padx=10, pady=5, anchor='s')

    def exit():
        root.destroy()

    L6 = Button(bottom_frame, text="Exit", font="orbitron 15 ", activebackground='orange', bg="#29293d", fg="white",
                width="10", height="2", command=exit)
    L6.pack(side="right", padx=10, pady=5, anchor='s')

    bottom_frame = Frame(root, relief='raised', borderwidth=2)
    bottom_frame.pack(fill='x', side='bottom')

    def tick():
        current_time = time.strftime('%I:%M %p').lstrip('0').replace('0', '')
        time1.config(text=current_time)
        time1.after(200, tick)

    time1 = Label(bottom_frame, font=('orbitron', 19))
    time1.pack(side='right')

    tick()
#Banking Page

def Banking_page():

        root=Tk()
        root.title("my atm ")
        root.geometry("1000x580+120+120")
        root.configure(background="#3d3d5c")
        font = "orbitron 30 bold"
        l1 = Label(root, text="STATE BANK OF INDIA", font=font, background="#3d3d5c", foreground="white")
        l1.pack(side=TOP, pady=10)

        l1 = Label(root, text="BANKING", font="orbitron 25 bold", background="#3d3d5c", foreground="white")
        l1.pack(side=TOP, pady=12)
        f = Frame(root, bg="#33334d")
        f.pack(fill="both",expand=True)
        l2 = Label(f, text="CHOOSE OPTION ", font="orbitron 20 bold", background="#33334d", foreground="white")
        l2.pack(side=TOP, pady=20)


        #FRAME
        f1 = Frame(f, bg="#29293d")
        f1.pack(side=TOP, padx=10)
        L1 = Button(f1, text="Balance", font="orbitron 15 ", bg="#29293d",activebackground='orange', fg="white",width="10",height="1",command=Balance_check)
        L1.grid(row=0, column=0, padx=40,pady=40)
        L2 = Button(f1, text="Deposit", font="orbitron 15 ", bg="#29293d",activebackground='orange', fg="white",width="10",height="1",command=deposit)
        L2.grid(row=0, column=1, padx=40,pady=40)
        L3 = Button(f1, text=" Withdraw", font="orbitron 15 ",activebackground='orange', bg="#29293d", fg="white",width="10",height="1",command=withdraw)
        L3.grid(row=1, column=0, padx=40,pady=40)
        L4 = Button(f1, text="Change Pin", font="orbitron 15 ",activebackground='orange', bg="#29293d", fg="white",width="10",height="1",command=Change_password)
        L4.grid(row=1, column=1, padx=40,pady=40)


        Back_button = Button(f, text="Back", font="orbitron 15 ", activebackground='orange', bg="#29293d", fg="white",
                    width="10", height="2")
        Back_button.pack(side="left",padx=10)
        def exit():
            root.destroy()
        exit_button = Button(f, text="Exit", font="orbitron 15 ", activebackground='orange', bg="#29293d", fg="white",
                    width="10", height="2",command=exit)
        exit_button.pack(side="right",padx=10)

        bottom_frame = Frame(root, relief='raised', borderwidth=2)
        bottom_frame.pack(fill='x', side='bottom')




        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace('0','')
            time1.config(text=current_time)
            time1.after(200, tick)

        time1 = Label(bottom_frame, font=('orbitron', 19))
        time1.pack(side='right')

        tick()


root.title("my atm ")
root.geometry("1000x580+120+120")
root.configure(background="#3d3d5c")
font="orbitron 30 bold"
#label
upper_frame=Frame(root,bg="#47476b")
upper_frame.pack(fill="both",expand=True)
l1=Label(upper_frame,text="STATE BANK OF INDIA",font=font,background="#47476b",foreground="white")
l1.pack(side=TOP,pady=20)
l2=Label(upper_frame,text="WELCOME TO ATM",font=('orbitron',25,'bold'),background="#47476b",foreground="white")
l2.pack(side=TOP,pady=40)

f=Frame(root,bg="#3d3d5c")
f.pack(side=TOP,padx=10)
L1=Label(f,text="Enter Your Pin :",font="orbitron 20 bold",bg="#3d3d5c",fg="white")
L1.grid(row=0,column=0,pady=30)

password=StringVar()

E1=Entry(f,font=font,justify=CENTER,fg='white',bg="#29293d",textvariable=password,show='*')
E1.grid(row=0,column=1,pady=30)




def check_password():
             global  Bank_Pin
             if E1.get()==Bank_Pin:
                 Banking_page()
               #  password.set()==''
                # incorrect_pass['text']=''

             else:
                 incorrect_pass['text']='Incorrect Password'
B1=Button(f,text="Submit",font=font,bg="#29293d",fg="white",command=check_password)
B1.grid(row=2,column=0,columnspan=2,pady=20)

incorrect_pass=Label(root,text=" ",font=('orbitron',19),fg='white',bg='#3d3d5c')
incorrect_pass.pack(fill="both",expand=True,pady=30)


bottom_frame=Frame(root,relief='raised',borderwidth=2)
bottom_frame.pack(fill='x',side='bottom')

r_pic=PhotoImage(file='rupay.png')
r_label=Label(bottom_frame,image=r_pic)
r_label.pack(side='left',padx=15)

v_pic=PhotoImage(file='visa.png')
v_label=Label(bottom_frame,image=v_pic)
v_label.pack(side='left',padx=15)

m_pic=PhotoImage(file='master.png')
m_label=Label(bottom_frame,image=m_pic)
m_label.pack(side='left',padx=15)

p_pic=PhotoImage(file='paypal.png')
p_label=Label(bottom_frame,image=p_pic)
p_label.pack(side='left',padx=15)

def tick():
        current_time=time.strftime('%I:%M %p').lstrip('0').replace('0','')
        time1.config(text=current_time)
        time1.after(200,tick)
time1=Label(bottom_frame,font=('orbitron',19))
time1.pack(side='right')

tick()
root.mainloop()

