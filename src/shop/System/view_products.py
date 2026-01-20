def view_products():
    wn = tk.Tk()
    wn.title("View Products")
    wn.geometry("700x500")

    columns = ("Date", "Product Name", "Price")

    tree = ttk.Treeview(wn, columns=columns, show="headings")

    tree.heading("Date", text="Date")
    tree.heading("Product Name", text="Product Name")
    tree.heading("Price", text="Price")

    tree.column("Date", width=150)
    tree.column("Product Name", width=300)
    tree.column("Price", width=150)

    tree.pack(fill=tk.BOTH, expand=True)

    products = fetch_products()
    for product in products:
        tree.insert("", tk.END, values=product)

    wn.mainloop()
