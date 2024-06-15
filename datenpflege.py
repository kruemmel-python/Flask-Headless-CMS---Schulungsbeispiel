import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from app import db, app as flask_app, Product
from werkzeug.utils import secure_filename
import os
import shutil

class DataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Data Entry")

        self.name_label = ttk.Label(root, text="Product Name:")
        self.name_label.grid(column=0, row=0, padx=10, pady=5, sticky='E')
        self.name_entry = ttk.Entry(root, width=30)
        self.name_entry.grid(column=1, row=0, padx=10, pady=5)

        self.price_label = ttk.Label(root, text="Price:")
        self.price_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.price_entry = ttk.Entry(root, width=30)
        self.price_entry.grid(column=1, row=1, padx=10, pady=5)

        self.desc_label = ttk.Label(root, text="Description:")
        self.desc_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.desc_entry = ttk.Entry(root, width=30)
        self.desc_entry.grid(column=1, row=2, padx=10, pady=5)

        self.image_label = ttk.Label(root, text="Image:")
        self.image_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.image_entry = ttk.Entry(root, width=30)
        self.image_entry.grid(column=1, row=3, padx=10, pady=5)
        self.image_button = ttk.Button(root, text="Browse", command=self.browse_image)
        self.image_button.grid(column=2, row=3, padx=10, pady=5)

        self.submit_button = ttk.Button(root, text="Add Product", command=self.add_product)
        self.submit_button.grid(column=1, row=4, padx=10, pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, file_path)

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        description = self.desc_entry.get()
        image_path = self.image_entry.get()

        if not name or not price or not description or not image_path:
            messagebox.showerror("Input Error", "All fields are required")
            return

        filename = secure_filename(os.path.basename(image_path))
        image_url = os.path.join('static/images', filename).replace('\\', '/')
        os.makedirs('static/images', exist_ok=True)

        try:
            shutil.copy(image_path, image_url)
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to copy file: {e}")
            return

        new_product = Product(
            name=name,
            price=float(price),
            description=description,
            image_url=image_url
        )

        with flask_app.app_context():
            db.session.add(new_product)
            db.session.commit()

        messagebox.showinfo("Success", "Product added successfully")
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.image_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()
