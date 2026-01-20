import tkinter as tk
from tkinter import ttk
import mysql.connector

def search_product():
    wn = tk.Tk()
    wn.title("Search Product")
    wn.geometry("600x420")

    tk.Label(wn, text="Search by name:").pack(pady=5)
    search_entry = tk.Entry(wn)
    search_entry.pack(fill=tk.X, padx=20)

    tree = ttk.Treeview(wn, columns=("Date","Name","Price"), show="headings")
    for col in ("Date","Name","Price"):
        tree.heading(col, text=col)
    tree.pack(fill=tk.BOTH, expand=True, pady=10)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Shop"
    )
    cursor = db.cursor()

    def do_search():
        tree.delete(*tree.get_children())
        keyword = "%" + search_entry.get() + "%"
        cursor.execute(
            "SELECT date, prodName, prodPrice FROM products WHERE prodName LIKE %s",
            (keyword,)
        )
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

    tk.Button(wn, text="SEARCH", command=do_search).pack(pady=5)

    wn.mainloop()
    cursor.close()
    db.close()

# Run
search_product()
