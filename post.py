import tkinter as tk
from tkinter import ttk
def create_post(text, feed_listbox):
    # Read input from the Post_text item and pass it to the Feed_listbox item
    print(text)
    feed_listbox.insert(tk.END, text)
