import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

# =========================
# Function: Add product to database
# =========================
def prodtoTable():
    pname = prodName.get()
    price = prodPrice.get()
    dt = date.get()

    if pname == "" or price == "" or dt == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="Shop"
        )
        cursor = db.cursor()

        query = "INSERT INTO products (date, prodName, prodPrice) VALUES (%s, %s, %s)"
        details = (dt, pname, price)

        cursor.execute(query, details)
        db.commit()

        messagebox.showinfo("Success", "Product added successfully")

        cursor.close()
        db.close()
        wn.destroy()

    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Database connection failed")

# =========================
# Function: GUI Form
# =========================
def addProd():
    global prodName, prodPrice, date, wn

    wn = Tk()
    wn.title("Shop Management System")
    wn.geometry("700x600")
    wn.configure(bg="mint cream")

    Canvas1 = Canvas(wn, bg="LightBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    # Heading
    headingFrame = Frame(wn, bg="LightBlue1")
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.1)

    headingLabel = Label(
        headingFrame,
        text="Add Product",
        font=("Courier", 16, "bold"),
        fg="grey19"
    )
    headingLabel.pack(expand=True, fill=BOTH)

    # Form
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.4)

    # Date
    Label(labelFrame, text="Date").place(relx=0.05, rely=0.2)
    date = Entry(labelFrame)
    date.place(relx=0.3, rely=0.2, relwidth=0.6)

    # Product Name
    Label(labelFrame, text="Product Name").place(relx=0.05, rely=0.4)
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.4, relwidth=0.6)

    # Product Price
    Label(labelFrame, text="Product Price").place(relx=0.05, rely=0.6)
    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3, rely=0.6, relwidth=0.6)

    # Buttons
    Button(wn, text="ADD", command=prodtoTable, bg="#d1ccc0").place(
        relx=0.3, rely=0.82, relwidth=0.15, relheight=0.07
    )

    Button(wn, text="QUIT", command=wn.destroy, bg="#f7f1e3").place(
        relx=0.55, rely=0.82, relwidth=0.15, relheight=0.07
    )

    wn.mainloop()
