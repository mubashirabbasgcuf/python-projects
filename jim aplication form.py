from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tmsg

def biodata():
    with open("records.txt","a") as f:
        f.write(f"The name is               :{namevalue.get()}\n")
        f.write(f"Emails address is         :{gmailvalue.get()}\n")
        f.write(f"Age of Application is     :{agevalue.get()}\n")
        f.write(f"The fathername            :{fathernamevalue.get()}\n")
        f.write(f"Applicant Blood group is  :{bloodgroupvalue.get()}\n")
        f.write(f"Contact no :              :{Contactnovalue.get()}\n")
        f.write(f"checkbox                  :{foodservices.get()}\n")
        f.write("_________________________________________________________\n")
    print(f"The name is               :{namevalue.get()}")
    print(f"Emails address is         :{gmailvalue.get()}")
    print(f"Age of Application is     :{agevalue.get()}")
    print(f"The fathername            :{fathernamevalue.get()}")
    print(f"Applicant Blood group is  :{bloodgroupvalue.get()}")
    print(f"Contact no :              :{Contactnovalue.get()}")
    print(f"checkbox                  :{foodservices.get()}")

def myfunction():
   ans=tmsg.askretrycancel("IT team","Records will update Shortly!!\nplease wait App is under construction")
   if ans:
      tmsg.showinfo("IT team message","Dear user please wait !! IT team will update it soon") 
   else:
        tmsg.showinfo("IT support","Thanks for having patience!!!")

root=Tk()
root.title("STRONG GYM ENTRY FORM")
root.geometry("2000x800")
# Lables means main text forms
welcome = Label(root, text="Strong GYM NEW COMMERS ENTRY FORM",font=("Calberi", 16, "bold"), fg="black")
name=Label(root,text="Name:")
fathername=Label(root,text="Father Name:")
age=Label(root,text="Age:")
bloodgroup=Label(root,text="BloodGroup")
Gender=Label(root,text="Gender")
Contactno=Label(root,text="Mobileno:")
gmail=Label(root,text="Enter Your Gmail:")
def helpbox():
    print("This box will help you")
    a=tmsg.showinfo("Help","Mubashir Abbas team will help you\nPlease Contact:03041654629")
    print(a)
def email():
    a=tmsg.showinfo("Gmail","please sent a mail at:mubashirabbasedu12@gmail.com")
    print(a)

# packing the forms
welcome.grid(row=0,column=3)
name.grid(row=2,column=2)
fathername.grid(row=3,column=2)
Contactno.grid(row=4,column=2)
gmail.grid(row=5,column=2)
Gender.grid(row=6,column=2)
age.grid(row=7,column=2)
bloodgroup.grid(row=8,column=2)


# selecting their datatypes
namevalue=StringVar()
fathernamevalue=StringVar()
Contactnovalue=IntVar()
gmailvalue=StringVar()
gendervalue=StringVar()
agevalue=IntVar()
bloodgroupvalue=StringVar()
foodservices=StringVar()

# assign the valuse
namevalue=Entry(root,textvariable=namevalue)
fathernamevalue=Entry(root,textvariable=fathernamevalue)
Contactnovalue=Entry(root,textvariable=Contactnovalue)
gmailvalue=Entry(root,textvariable=gmailvalue)
gendervalue=Entry(root,textvariable=gendervalue)
agevalue=Entry(root,textvariable=agevalue)
bloodgroupvalue=Entry(root,textvariable=bloodgroupvalue)

# packing the enteries
namevalue.grid(row=2,column=3)
fathernamevalue.grid(row=3, column=3)
Contactnovalue.grid(row=4, column=3)
gmailvalue.grid(row=5, column=3)
gendervalue.grid(row=6, column=3)
agevalue.grid(row=7,   column=3)
bloodgroupvalue.grid(row=8, column=3)

# button
foodpackets=Checkbutton(text="Do you want to get JYM protein packets",variable=foodservices)
foodpackets.grid(row=22,column=3)
Button(text="Apply",command=biodata).grid(row=33,column=3)
ttk.Button(text="Get verification Email").grid(row=31,column=3)
ttk.Button(text="Get OTP").grid(row=32,column=3)
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New Entry",command=myfunction)
m1.add_command(label="open list",command=myfunction)
m1.add_command(label="save list",command=myfunction)
m1.add_command(label="save list",command=myfunction)
m1.add_command(label="print list",command=myfunction)
m1.add_command(label="share list",command=myfunction)
m1.add_command(label="auto  list",command=myfunction)
m1.add_command(label="open folder",command=myfunction)
m1.add_command(label="Exit Application",command=myfunction)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
# 2nd menu
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo",command=myfunction)
m2.add_command(label="Redo",command=myfunction)
m2.add_command(label="copy data",command=myfunction)
m2.add_command(label="paste ",command=myfunction)
m2.add_command(label="cut data",command=myfunction)
m2.add_command(label="paste",command=myfunction)
m2.add_command(label="clear data",command=myfunction)
m2.add_command(label="Replace in files",command=myfunction)
m2.add_command(label="Exit",command=myfunction)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)
# 3rd menu
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Open list with notepad",command=myfunction)
m3.add_command(label="Search in list",command=myfunction)
m3.add_command(label="copy with",command=myfunction)
m3.add_command(label="paste in notepad",command=myfunction)
m3.add_command(label="cut with",command=myfunction)
m3.add_command(label="paste with",command=myfunction)
m3.add_command(label="clear with",command=myfunction)
m3.add_command(label="Replace in files",command=myfunction)
m3.add_command(label="Exit menu",command=myfunction)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Selection",menu=m3)

m4=Menu(mainmenu,tearoff=0)
m4.add_command(label="Contact us",command=helpbox)
m4.add_command(label="Gmail",command=email)
# m4.add_command(label="Email",command=myfunction)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m4)
root.mainloop()
