import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------- DB ----------
def db_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Shop"
    )

# ---------- MAIN ----------
def app():
    wn = tk.Tk()
    wn.title("Shop Management - All in One")
    wn.geometry("750x500")

    # ---------- FORM ----------
    frm = tk.Frame(wn)
    frm.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(frm, text="Date").grid(row=0, column=0)
    tk.Label(frm, text="Name").grid(row=0, column=2)
    tk.Label(frm, text="Price").grid(row=0, column=4)

    e_date = tk.Entry(frm, width=15)
    e_name = tk.Entry(frm, width=20)
    e_price = tk.Entry(frm, width=10)

    e_date.grid(row=0, column=1)
    e_name.grid(row=0, column=3)
    e_price.grid(row=0, column=5)

    # ---------- TABLE ----------
    tree = ttk.Treeview(
        wn, columns=("ID","Date","Name","Price"), show="headings"
    )
    for c in ("ID","Date","Name","Price"):
        tree.heading(c, text=c)
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # ---------- FUNCTIONS ----------
    def load_data():
        tree.delete(*tree.get_children())
        db = db_conn()
        cur = db.cursor()
        cur.execute("SELECT id, date, prodName, prodPrice FROM products")
        for r in cur.fetchall():
            tree.insert("", tk.END, values=r)
        db.close()

    def add_product():
        if not e_date.get() or not e_name.get() or not e_price.get():
            return messagebox.showwarning("Warning","Fill all fields")

        db = db_conn()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO products (date, prodName, prodPrice) VALUES (%s,%s,%s)",
            (e_date.get(), e_name.get(), e_price.get())
        )
        db.commit()
        db.close()
        load_data()

    def delete_product():
        sel = tree.selection()
        if not sel:
            return
        pid = tree.item(sel)["values"][0]
        db = db_conn()
        cur = db.cursor()
        cur.execute("DELETE FROM products WHERE id=%s",(pid,))
        db.commit()
        db.close()
        load_data()

    def search_product():
        tree.delete(*tree.get_children())
        db = db_conn()
        cur = db.cursor()
        cur.execute(
            "SELECT id, date, prodName, prodPrice FROM products WHERE prodName LIKE %s",
            ("%" + e_name.get() + "%",)
        )
        for r in cur.fetchall():
            tree.insert("", tk.END, values=r)
        db.close()

    # ---------- BUTTONS ----------
    btn = tk.Frame(wn)
    btn.pack(pady=5)

    tk.Button(btn, text="ADD", command=add_product).pack(side=tk.LEFT, padx=5)
    tk.Button(btn, text="DELETE", command=delete_product).pack(side=tk.LEFT, padx=5)
    tk.Button(btn, text="SEARCH", command=search_product).pack(side=tk.LEFT, padx=5)
    tk.Button(btn, text="REFRESH", command=load_data).pack(side=tk.LEFT, padx=5)

    load_data()
    wn.mainloop()

# Run
app()
