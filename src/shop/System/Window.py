import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def delete_product():
    wn = tk.Tk()
    wn.title("Delete Product")
    wn.geometry("600x400")

    tree = ttk.Treeview(wn, columns=("ID","Date","Name","Price"), show="headings")
    for col in ("ID","Date","Name","Price"):
        tree.heading(col, text=col)
    tree.pack(fill=tk.BOTH, expand=True)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Shop"
    )
    cursor = db.cursor()
    cursor.execute("SELECT id, date, prodName, prodPrice FROM products")

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

    def delete_selected():
        item = tree.selection()
        if not item:
            messagebox.showwarning("Warning", "Select a product first")
            return

        pid = tree.item(item)["values"][0]
        cursor.execute("DELETE FROM products WHERE id=%s", (pid,))
        db.commit()
        tree.delete(item)

    tk.Button(wn, text="DELETE", bg="tomato", command=delete_selected)\
        .pack(pady=5)

    wn.mainloop()
    cursor.close()
    db.close()

# Run
delete_product()
