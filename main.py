import tkinter as tk
from tkinter import ttk
import create
from post import create_post

def login():
    login_frame.grid_forget()
    feed_frame.grid(row=0, column=0, sticky="nsew")

def register():
    pass

def show_post_frame():
    feed_frame.grid_forget()
    post_frame.grid(row=0, column=0, sticky="nsew")

def show_feed_frame():
    post_frame.grid_forget()
    feed_frame.grid(row=0, column=0, sticky="nsew")

app = tk.Tk()
app.title("Social Media App")
app.geometry("800x600")

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

feed_frame = ttk.Frame(app)

feed_label = ttk.Label(feed_frame, text="Feed")
feed_label.grid(row=0, column=0, padx=10, pady=10)

feed_listbox = tk.Listbox(feed_frame, width=50, height=33)
feed_listbox.grid(row=1, column=0, padx=10, pady=10)

to_post_button = ttk.Button(feed_frame, text="Create Post", command=show_post_frame)
to_post_button.grid(row=2, column=0, padx=10, pady=10)

post_frame = ttk.Frame(app)

post_label = ttk.Label(post_frame, text="Create Post")
post_label.grid(row=0, column=0, padx=10, pady=10)

post_text = tk.Text(post_frame, height=5, width=30)
post_text.grid(row=1, column=0, padx=10, pady=10)

post_button = ttk.Button(post_frame, text="Post", command=lambda: create_post(post_text.get("1.0", "end-1c"), feed_listbox))
post_button.grid(row=2, column=0, padx=10, pady=10)

to_feed_button = ttk.Button(post_frame, text="Back to Feed", command=show_feed_frame)
to_feed_button.grid(row=3, column=0, padx=10, pady=10)

feed_frame.grid_forget()
post_frame.grid_forget()

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
feed_frame.columnconfigure(0, weight=1)
feed_frame.rowconfigure(1, weight=1)
post_frame.columnconfigure(0, weight=1)
post_frame.rowconfigure(1, weight=1)

app.mainloop()
