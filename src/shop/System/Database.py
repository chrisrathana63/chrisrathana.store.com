def fetch_products():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="Shop"
        )
        cursor = db.cursor()
        cursor.execute("SELECT date, prodName, prodPrice FROM products")
        rows = cursor.fetchall()

        cursor.close()
        db.close()
        return rows

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []
