import tkinter as tk
from tkinter import messagebox

# Predefined Menu with Prices in INR
MENU = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Salad": 100,
    "Fries": 80,
    "Drink": 50,
}

# Predefined Login Credentials
LOGIN_CREDENTIALS = {
    "admin": "admin123",
    "user": "user123",
}


# Login Page
def login_page():
    def validate_login():
        username = username_entry.get()
        password = password_entry.get()
        if username in LOGIN_CREDENTIALS and LOGIN_CREDENTIALS[username] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            login_window.destroy()
            customer_menu_system()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    # Create Login Window
    login_window = tk.Tk()
    login_window.title("Restaurant Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Restaurant Management System", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(login_window, text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    tk.Button(login_window, text="Login", command=validate_login).pack(pady=10)

    login_window.mainloop()


# Customer Menu System
def customer_menu_system():
    def add_to_cart():
        item = menu_var.get()
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity")
            return

        if item not in MENU:
            messagebox.showerror("Error", "Invalid Item Selected")
            return
        price = MENU[item]
        total = price * quantity

        # Add item to cart display
        cart_listbox.insert(tk.END, f"{item} (x{quantity}): ₹{total:.2f}")
        cart_items.append((item, quantity, total))
        calculate_total_bill()
        quantity_entry.delete(0, tk.END)

    def calculate_total_bill():
        total_bill = sum(item[2] for item in cart_items)
        total_label.config(text=f"Total: ₹{total_bill:.2f}")

    def clear_cart():
        cart_listbox.delete(0, tk.END)
        cart_items.clear()
        calculate_total_bill()

    def checkout():
        if not cart_items:
            messagebox.showerror("Error", "Cart is empty!")
            return
        total_bill = sum(item[2] for item in cart_items)
        messagebox.showinfo("Checkout", f"Thank you for your order!\nTotal Bill: ₹{total_bill:.2f}")
        clear_cart()

    # Main Customer Menu Window
    menu_window = tk.Tk()
    menu_window.title("Restaurant Menu")
    menu_window.geometry("400x500")

    tk.Label(menu_window, text="Restaurant Menu", font=("Arial", 16, "bold")).pack(pady=10)

    # Menu Selection
    tk.Label(menu_window, text="Select an Item:").pack(pady=5)
    menu_var = tk.StringVar()
    menu_var.set("Pizza")  # Default selection
    menu_dropdown = tk.OptionMenu(menu_window, menu_var, *MENU.keys())
    menu_dropdown.pack(pady=5)

    tk.Label(menu_window, text="Enter Quantity:").pack(pady=5)
    quantity_entry = tk.Entry(menu_window)
    quantity_entry.pack(pady=5)

    tk.Button(menu_window, text="Add to Cart", command=add_to_cart).pack(pady=10)

    # Cart Display
    tk.Label(menu_window, text="Your Cart:").pack(pady=10)
    cart_listbox = tk.Listbox(menu_window, width=50, height=10)
    cart_listbox.pack(pady=5)

    # Total Bill Display
    total_label = tk.Label(menu_window, text="Total: ₹0.00", font=("Arial", 12, "bold"))
    total_label.pack(pady=5)

    # Action Buttons
    tk.Button(menu_window, text="Clear Cart", command=clear_cart).pack(pady=5)
    tk.Button(menu_window, text="Checkout", command=checkout).pack(pady=10)

    cart_items = []

    menu_window.mainloop()


# Run the Login Page
if __name__ == "__main__":
    login_page()
