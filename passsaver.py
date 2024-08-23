from tkinter import*
from tkinter import ttk
import datetime
root=Tk()
def getdata():
    with open("Passsaver","a") as f:
        f.write(f"The name of account is        :{namevalue.get()}\n")
        f.write(f"The user name of account is   :{usernamevalue.get()}\n")
        f.write(f"The password name of account  :{passwordvalue.get()}\n")
        f.write(f"The attched mobile no is      :{phonenumbervalue.get()}\n")
        f.write(f"The attached Emails   is :     :{emailvalue.get()}\n")
        f.write("               DATABASE SAVED      \n"                )
        f.write(f"time={datetime.datetime.now()}")
        f.write("____________________________________________________\n")    


    print(f"The name of account is        :{namevalue.get()}\n")
    print(f"The user name of account is   :{usernamevalue.get()}\n")
    print(f"The password name of account  :{passwordvalue.get()}\n")
    print(f"The attched mobile no is      :{phonenumbervalue.get()}\n")
    print(f"The attached Emails   is :     :{emailvalue.get()}\n")
    print("               DATABASE SAVED      \n"                )
    print("____________________________________________________\n")      

root.title("PassSaver")
root.geometry("2000x800")
mainline=Label(root,text="Welcome to PassSaver",font=("calberi",10,"bold"),fg="black",bg="white",padx=10)
mainline.grid(row=0,column=4)
# main texts on the form
name=Label(root,text="Name the Your Account:").grid(row=3,column=3)
username=Label(root,text="User Name of ID:").grid(row=4,column=3)
password=Label(root,text="Password of Your ID:").grid(row=5,column=3)
phonenumber=Label(root,text="Linked Phone no:").grid(row=6,column=3)
email=Label(root,text="Enter linked Email:").grid(row=7,column=3)
# value of variables
namevalue=StringVar()
usernamevalue=StringVar()
passwordvalue=StringVar()
phonenumbervalue=StringVar()
emailvalue=StringVar()
# entry fields
nameentry=Entry(root,textvariable=namevalue).grid(row=3,column=4)
usernameentry=Entry(root,textvariable=usernamevalue).grid(row=4,column=4)
passwordentry=Entry(root,textvariable=passwordvalue).grid(row=5,column=4)
phonenumberentry=Entry(root,textvariable=phonenumbervalue).grid(row=6,column=4)
emailvalueentry=Entry(root,textvariable=emailvalue).grid(row=7,column=4)

ttk.Button(text="Get verification Email").grid(row=33,column=4)

ttk.Button(text="Save to Data-Base",command=getdata).grid(row=35,column=4)

root.mainloop()