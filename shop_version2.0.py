from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tmsg
def myfunction():
    print("We are working on these options")
def calculate_total_bill():
    total_bill = 0
    for i, item in enumerate(order_items):
        if order_item_vars[i].get() == 1:
            quantity = quantity_entries[i].get()
            price = price_entries[i].get()
            if quantity and price:
                total_bill += float(quantity) * float(price)
    total_Bill_value.set(str(total_bill))

def calculate_amount_due():
    try:
        total_bill = float(total_Bill_value.get())
        paid_amount = float(paid_amount_value.get())
        amount_left = total_bill - paid_amount
        Amount_due_value.set(str(amount_left))
    except ValueError:
        Amount_due_value.set("Invalid input")

def save_to_file():
    file_name = "quetta karak chai.txt"
    with open(file_name, "a") as f:
        f.write("Welcome to Quetta karak Shop\n")
        f.write("Name of customer: {}\n".format(name_of_customer_value.get()))
        f.write("Contact number: {}\n".format(Phone_number_value.get()))
        f.write("Order details:\n")
        for i, item in enumerate(order_items):
            if order_item_vars[i].get() == 1:
                quantity = quantity_entries[i].get()
                price = price_entries[i].get()
                f.write("{} - Quantity: {}, Price: {}\n".format(item, quantity, price))
        f.write("Total Bill: {}\n".format(total_Bill_value.get()))
        f.write("Paid Amount: {}\n".format(paid_amount_value.get()))
        f.write("Amount Due: {}\n".format(Amount_due_value.get()))
        f.write("AMOUNT paid to: {}\n".format(Reciever_value.get()))
        f.write("_________________________________________________")
    print("Order details saved to", file_name)
    

def messagebox():
    tmsg.showinfo("Help", "Records will update Shortly!!\nplease wait App is under construction")
def helpbox():
    print("This box will help you")
    a=tmsg.showinfo("Help","Muabshir Abbas team will help you\nPlease Contact:03041654629")
    print(a)
def email():
    a=tmsg.showinfo("Gmail","please sent a mail at:mubashirabbasedu12@gmail.com")
    print(a)

root=Tk()
root.title("Quetta Karak Cafe Shop App")
root.geometry("2000x800")

# creating Labels an grids
welcome_label=Label(root,text="Welcome to Quetta karak Shop",font=("calibri",20,"bold"),bg="white",fg="black",padx=20).grid(row=1,column=1)
customer_label=Label(root,text="Name of customer:").grid(row=2,column=0)
paid_Amount_label=Label(root,text="Paid Amount").grid(row=14,column=0)
Amount_due_label=Label(root,text="Amount Due:").grid(row=15,column=0)
Reciever_label=Label(root,text="AMOUNT paid to:").grid(row=16,column=0)
total_Bill_label=Label(root,text="Total Bill:").grid(row=13,column=0)
Phone_number_label=Label(root,text="Contact number:").grid(row=17,column=0)

# variables
name_of_customer_value=StringVar()
total_Bill_value=StringVar()
Phone_number_value=StringVar()
paid_amount_value=StringVar()
Amount_due_value=StringVar()
Reciever_value=StringVar()

# entry points
name_of_customer=Entry(root,textvariable=name_of_customer_value).grid(row=2,column=1)
Phone_number=Entry(root,textvariable=Phone_number_value).grid(row=17,column=1)
paid_Amount=Entry(root,textvariable=paid_amount_value).grid(row=14,column=1)
Amount_left=Entry(root,textvariable=Amount_due_value).grid(row=15,column=1)
Reciever=Entry(root,textvariable=Reciever_value).grid(row=16,column=1)
total_Bill=Entry(root,textvariable=total_Bill_value,state='readonly').grid(row=13,column=1)

# Order items
order_items = ["Tea", "Coffee", "Sandwich", "Burger", "Pizza", "Fries", "Salad", "Chicken Wings", "Soda", "Water"]
order_item_vars = []
quantity_entries = []
price_entries = []
for i, item in enumerate(order_items):
    var = IntVar()
    order_item_vars.append(var)
    Checkbutton(root, text=item, variable=var).grid(row=3+i, column=0)
    quantity_label = Label(root, text="Quantity:").grid(row=3+i, column=1)
    quantity_entry = Entry(root)
    quantity_entry.grid(row=3+i, column=2)
    quantity_entries.append(quantity_entry)
    price_label = Label(root, text="Price:").grid(row=3+i, column=3)
    price_entry = Entry(root)
    price_entry.grid(row=3+i, column=4)
    price_entries.append(price_entry)

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="open hotel Record",command=messagebox)
m1.add_command(label="open Files",command=messagebox)
m1.add_command(label="save Hotel record",command=messagebox)
m1.add_command(label="save as Hotel record",command=messagebox)
m1.add_command(label="print Hotel record",command=messagebox)
m1.add_command(label="share Hotel record",command=messagebox)
m1.add_command(label="auto save Hotel record",command=messagebox)
m1.add_command(label="open folder of records ",command=messagebox)
m1.add_command(label="Exit",command=messagebox)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
# 2nd menu
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo Hotel record",command=messagebox)
m2.add_command(label="Redo Hotel record",command=messagebox)
m2.add_command(label="copy Hotel record",command=messagebox)
m2.add_command(label="paste Hotel record",command=messagebox)
m2.add_command(label="cut Hotel record",command=messagebox)
m2.add_command(label="paste Hotel record",command=messagebox)
m2.add_command(label="clear Hotel record",command=messagebox)
m2.add_command(label="Replace Hotel record",command=messagebox)
m2.add_command(label="Exit",command=myfunction)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)
# 3rd menu
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Open Excel record",command=messagebox)
m3.add_command(label="Search Hotel record",command=messagebox)
m3.add_command(label="copy with",command=messagebox)
m3.add_command(label="paste with",command=messagebox)
m3.add_command(label="cut with",command=messagebox)
m3.add_command(label="paste with",command=messagebox)
m3.add_command(label="clear with",command=messagebox)
m3.add_command(label="Replace in files",command=messagebox)
m3.add_command(label="Exit menu",command=messagebox)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Selection",menu=m3)

m4=Menu(mainmenu,tearoff=0)
m4.add_command(label="Contact us",command=helpbox)
m4.add_command(label="Gmail",command=email)
# m4.add_command(label="Email",command=myfunction)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m4)

# buttons
calculate_total_bill_button=ttk.Button(root,text="Total Bill",command=calculate_total_bill).grid(row=18,column=1)
calculate_button=ttk.Button(root,text="Calculate remaining bill",command=calculate_amount_due).grid(row=19,column=1)
save_button=ttk.Button(root,text="Save to file",command=save_to_file).grid(row=20,column=1)
root.mainloop()