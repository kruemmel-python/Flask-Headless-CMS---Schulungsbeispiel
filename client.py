import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io
import base64

def fetch_products():
    try:
        response = requests.get('http://127.0.0.1:5000/products')
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")
    return []

def display_products(products):
    for widget in frame.winfo_children():
        widget.destroy()
    if not products:
        no_product_label = tk.Label(frame, text="No products available.")
        no_product_label.pack()
        return
    for product in products:
        name_label = tk.Label(frame, text=product['name'], font=('Helvetica', 14, 'bold'))
        name_label.pack(pady=2)
        price_label = tk.Label(frame, text=f"Price: ${product['price']}")
        price_label.pack(pady=2)
        desc_label = tk.Label(frame, text=f"Description: {product['description']}")
        desc_label.pack(pady=2)
        try:
            if product['image_data']:
                image_data = base64.b64decode(product['image_data'])
                img = Image.open(io.BytesIO(image_data))
                img = img.resize((200, 200), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=img)
                img_label.image = img
                img_label.pack(pady=2)
            else:
                img_label = tk.Label(frame, text="No image available", fg='red')
                img_label.pack(pady=2)
        except Exception as e:
            img_label = tk.Label(frame, text=f"Error loading image: {e}", fg='red')
            img_label.pack(pady=2)
        separator = ttk.Separator(frame, orient='horizontal')
        separator.pack(fill='x', pady=5)
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def refresh_products():
    products = fetch_products()
    display_products(products)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Product Catalog')

    refresh_button = ttk.Button(root, text="Refresh Products", command=refresh_products)
    refresh_button.pack(pady=10)

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame = scrollable_frame

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    products = fetch_products()
    display_products(products)

    root.mainloop()
