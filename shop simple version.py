from tkinter import*
from tkinter import ttk
def calculate_amount_due():
    try:
        total_bill = float(total_Bill_value.get())
        paid_amount = float(paid_amount_value.get())
        amount_left = total_bill - paid_amount
        Amount_due_value.set(str(amount_left))
    except ValueError:
        Amount_due_value.set("Invalid input")

root=Tk()
root.title("Quetta Karak Cafe Shop App")
root.geometry("2000x800")


# creating Labels an grids
welcome_label=Label(root,text="Welcome to Quetta karak Shop",font=("calberi",20,"bold"),padx=20).grid(row=1,column=0)
customer_label=Label(root,text="Name of customer:").grid(row=2,column=0)
total_Bill_label=Label(root,text="Total Bill:").grid(row=3,column=0)
Phone_number_label=Label(root,text="Contact number:").grid(row=7,column=0)
paid_Amount_label=Label(root,text="Paid Amount").grid(row=4,column=0)
Amount_due_label=Label(root,text="Amount Due:").grid(row=5,column=0)
Reciever_label=Label(root,text="AMOUNT paid to:").grid(row=6,column=0)

# variables
name_of_customer_value=StringVar()
total_Bill_value=StringVar()
Phone_number_value=StringVar()
paid_amount_value=StringVar()
Amount_due_value=StringVar()
Reciever_value=StringVar()
# entry points
name_of_customer=Entry(root,textvariable=name_of_customer_value).grid(row=2,column=1)
total_Bill=Entry(root,textvariable=total_Bill_value).grid(row=3,column=1)
Phone_number=Entry(root,textvariable=Phone_number_value).grid(row=7,column=1)
paid_Amount=Entry(root,textvariable=paid_amount_value).grid(row=4,column=1)
Amount_left=Entry(root,textvariable=Amount_due_value).grid(row=5,column=1)
Reciever=Entry(root,textvariable=Reciever_value).grid(row=6,column=1)

# buttons
calculate_button=Button(root,text="Calculate",command=calculate_amount_due).grid(row=9,column=1)
root.mainloop()