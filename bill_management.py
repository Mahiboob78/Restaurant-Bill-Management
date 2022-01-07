from tkinter import *
from tkinter import ttk 

def Bill():
    total_amount = 0
    if (var1.get()):
        price = 200
        qty = int(e1.get())
        total_amount = int(price * qty)
        tempList = [["Mutton Biriyani", price, e1.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, total_amount) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))
 
    if (var2.get()):
        price = 180
        qty = int(e2.get())
        total_amount = int(price * qty)
        tempList = [["Chicken Biriyani", price, e2.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, total_amount) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))
 
    if (var3.get()):
        price = 80
        qty = int(e3.get())
        total_amount = int(price * qty)
        tempList = [["Egg Noodles", price, e3.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    if (var4.get()):
        price = 60
        qty = int(e4.get())
        total_amount = int(price * qty)
        tempList = [["Gobi Manchurian", price, e4.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    if (var5.get()):
        price = 40
        qty = int(e5.get())
        total_amount = int(price * qty)
        tempList = [["Veg Clear Soup", price, e5.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    if (var6.get()):
        price = 30
        qty = int(e6.get())
        total_amount = int(price * qty)
        tempList = [["Masala Papad", price, e6.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    if (var7.get()):
        price = 45
        qty = int(e7.get())
        total_amount = int(price * qty)
        tempList = [["Cocacola", price, e7.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    if (var8.get()):
        price = 40
        qty = int(e8.get())
        total_amount = int(price * qty)
        tempList = [["Pepsi", price, e8.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    if (var9.get()):
        price = 35
        qty = int(e9.get())
        total_amount = int(price * qty)
        tempList = [["Lime Soda", price, e9.get(), total_amount]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, ttl) in enumerate(tempList, start=1):
            list1.insert("", "end", values=(item, price, qty, total_amount))

    sum1 = 0.0
    for child in list1.get_children():
        sum1 += float(list1.item(child, 'values')[3])
    total_amt.set(sum1)

    
global restaurant 

restaurant = Tk()
restaurant.title("Restaurant Bill")
restaurant.geometry("900x700")


global total_amt
global balText
 
total_amt = IntVar()

Label(restaurant, text="Bill mangement system", font="arial 22 bold" ,bg="white").place(x=200, y=10)

Label(restaurant, text="ITEMS").place(x=200, y=80)
Label(restaurant, text="PRICES").place(x=400, y=80)
Label(restaurant, text="QUANTITY").place(x=600, y=80)

var1 = IntVar()   
Label(restaurant, text="Major Dishes:").place(x=20, y=100)
Checkbutton(restaurant, text="Mutton Biriyani", variable=var1).place(x=200, y=100)
Label(restaurant, text="200").place(x=400, y=100)
    
e1 = Entry(restaurant)
e1.place(x=600, y=100)

var2 = IntVar()  
Checkbutton(restaurant, text="Chicken Biriyani", variable=var2).place(x=200, y=120)
Label(restaurant, text="120").place(x=400, y=120)

e2 = Entry(restaurant)
e2.place(x=600, y=120)  

var3 = IntVar()   
Checkbutton(restaurant, text="Egg Noodles", variable=var3).place(x=200, y=140)
Label(restaurant, text="80").place(x=400, y=140)

e3 = Entry(restaurant)
e3.place(x=600, y=140)
    
var4 = IntVar()
Label(restaurant, text="Starters:").place(x=20, y=180)
Checkbutton(restaurant, text="Gobi Manchurian", variable=var4).place(x=200, y=180)
Label(restaurant, text="60").place(x=400, y=180)

e4 = Entry(restaurant)
e4.place(x=600, y=180)
    
var5 = IntVar()
Checkbutton(restaurant, text="Veg Clear Soup", variable=var5).place(x=200, y=200)
Label(restaurant, text="40").place(x=400, y=200)

e5 = Entry(restaurant)
e5.place(x=600, y=200) 

var6 = IntVar()
Checkbutton(restaurant, text="Masala Papad", variable=var6).place(x=200, y=220)
Label(restaurant, text="30").place(x=400, y=220)

e6 = Entry(restaurant)
e6.place(x=600, y=220)
    
var7 = IntVar()
Label(restaurant, text="Soft Drinks:").place(x=20, y=260)
Checkbutton(restaurant, text="Cocacola", variable=var7).place(x=200, y=260)
Label(restaurant, text="45").place(x=400, y=260)

e7 = Entry(restaurant)
e7.place(x=600, y=260)
    
var8 = IntVar()
Checkbutton(restaurant, text="Pepsi", variable=var8).place(x=200, y=280)
Label(restaurant, text="40").place(x=400, y=280)

e8 = Entry(restaurant)
e8.place(x=600, y=280)
    
var9 = IntVar()
Checkbutton(restaurant, text="Lime Soda", variable=var9).place(x=200, y=300)
Label(restaurant, text="35").place(x=400, y=300)
    
e9 = Entry(restaurant)
e9.place(x=600, y=300)

cols=('Item','Price','Quantity','Total')
list1=ttk.Treeview(restaurant, columns=cols, show='headings')
for col in cols:
    list1.heading(col, text=col)
    list1.grid(row=1, column=0, columnspan=1)
    list1.place(x=5,y=340)

Button(restaurant, text="Total Amount", command=Bill, font="arial 20 bold").place(x=100, y=580)    
# Button(restaurant, text="Clear", command=clear_all, font="arial 20 bold").place(x=600, y=580)

total_amount = Label(restaurant, background="skyblue", font="arial 20 bold", textvariable=total_amt)
total_amount.place(x=350, y=580, width=200, height=55)


restaurant.mainloop()
