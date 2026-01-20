import tkinter as tk
from tkinter import ttk
import mysql.connector

def view_products():
    wn = tk.Tk()
    wn.title("View Products")
    wn.geometry("600x400")

    tree = ttk.Treeview(wn, columns=("Date","Name","Price"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Name", text="Product Name")
    tree.heading("Price", text="Price")
    tree.pack(fill=tk.BOTH, expand=True)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Shop"
    )
    cursor = db.cursor()
    cursor.execute("SELECT date, prodName, prodPrice FROM products")

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

    cursor.close()
    db.close()

    wn.mainloop()

# Run
view_products()
