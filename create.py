import tkinter as tk
from tkinter import ttk

def login(username, password):
    #Read username and password from file, and check if function parameters match this
    pass



def regiser(username, password):
    # create_username_password.py

users = {} # initialize an empty dictionary to store user data

def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password # add the username and password to the users dictionary
    print("Account created successfully!")

create_account() # call the function to create a new account

# print the dictionary to check the data
print(users)

    #Write username and password to file, make sure credentials arent already used.
    pass


#with open(file_name, 'a') as file:
#    file.write(content)