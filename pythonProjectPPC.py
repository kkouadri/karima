#Define the main application window

import tkinter as tk
app = tk. Tk()
app.title("PizzaOrderPro")

# Define GUI elements and layout
# Main Menu

menu_label =tk. Label(app, text="Select Menu Category:")
menu_label.pack()
menu_listbox = tk.Listbox(app)
menu_listbox.pack()

# Customer Information

customer_label = tk. Label (app, text="Customer Information:")
customer_label.pack()
name_entry = tk. Entry(app, text="Name")
name_entry. pack()
contact_entry = tk.Entry(app, text="Contact Information")
contact_entry.pack()
delivery_option = tk.StringVar()
delivery_option.set("Delivery")
delivery_radio1 = tk.Radiobutton(app, text="Delivery", variable=delivery_option, value="Delivery")
delivery_radio2 = tk.Radiobutton(app, text="Pickup", variable=delivery_option, value="Pickup")
delivery_radio1.pack()
delivery_radio2.pack()

# Payment Processing

payment_label=tk.Label (app, text= "Payment Information:")
payment_label.pack()
payment_entry = tk.Entry (app, text="Payment")
payment_entry.pack()

# Order Management (Staff Side)

staff_label = tk.Label(app, text="Order Management (Staff side):")
staff_label.pack()
order_listbox = tk.Listbox (app)
order_listbox.pack()
prepare_button = tk. Button (app, text="Prepare Order")
prepare_button. pack()
complete_button = tk. Button(app, text="Mark as Completed")
complete_button.pack()

# Order History

history_label = tk.Label(app, text="Order History:")
history_label.pack()
history_listbox = tk.Listbox(app)
history_listbox.pack()

# User Authentication

auth_label = tk.Label(app, text="User Authentication:")
auth_label.pack()
username_entry = tk.Entry(app, text="Username")
username_entry.pack()
password_entry = tk.Entry(app, text= "Password", show="*")
password_entry.pack()
login_button = tk.Button (app, text="Login")
login_button.pack()

# Feedback and Support

feedback_label = tk.Label(app, text="Feedback and Support:")
feedback_label.pack()
feedback_entry = tk.Entry(app, text="Feedback")
feedback_entry.pack()
rating_scale = tk.Scale(app, from_=1, to=5, orient="horizontal", label="Rate Your Experience:")
rating_scale.pack()
submit_feedback_button = tk.Button(app, text="submit Feedback")
submit_feedback_button.pack()

# Admin Panel (Optional)
# Define admin-only features here if needed

# Run the application

app.mainloop() 
