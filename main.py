import tkinter as tk
from tkinter import ttk
import create
import post

def login():
    login_frame.grid_forget()
    main_frame.grid(row=0, column=0, sticky="nsew")

def register():
    pass

app = tk.Tk()
app.title("Social Media App")
app.geometry("800x600")

# Login Screen
login_frame = ttk.Frame(app)
login_frame.grid(row=0, column=0, sticky="nsew")

username_label = ttk.Label(login_frame, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = ttk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = ttk.Label(login_frame, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = ttk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

register_button = ttk.Button(login_frame, text="Register", command=register)
register_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Main Screen
main_frame = ttk.Frame(app)

# Feed
feed_label = ttk.Label(main_frame, text="Feed")
feed_label.grid(row=0, column=0, padx=10, pady=10)

feed_listbox = tk.Listbox(main_frame, width=50, height=33)  # Adjusted width and height
feed_listbox.grid(row=1, column=0, padx=10, pady=10)

# Post creation
post_label = ttk.Label(main_frame, text="Create Post")
post_label.grid(row=0, column=1, padx=10, pady=10)

post_text = tk.Text(main_frame, height=5, width=30)
post_text.grid(row=1, column=1, padx=10, pady=10)

post_button = ttk.Button(main_frame, text="Post", command=post)
post_button.grid(row=2, column=1, padx=10, pady=10)

# Profile
profile_label = ttk.Label(main_frame, text="Profile")
profile_label.grid(row=0, column=2, padx=10, pady=10)

profile_details = ttk.Label(main_frame, text="Profile Details")
profile_details.grid(row=1, column=2, padx=10, pady=10)

# Hide the main_frame by default
main_frame.grid_forget()

# Set up grid for frames
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
main_frame.columnconfigure((0, 1, 2), weight=1)
main_frame.rowconfigure(1, weight=1)

app.mainloop()
