import tkinter as tk
from tkinter import font
import requests
import json


def post_to_feed(username, text):
    url = "http://107.152.44.102:5000/post-to-feed"  # Replace with your server's URL if needed
    data = {'username': username, 'text': text}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        print("Post created successfully!")
    else:
        print("Error:", response.text)

def view_post(username):
    url = "http://107.152.44.102:5000/view-post"  # Replace with your server's URL if needed
    data = {'username': username}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        posts = response.json()
        print(f"Posts by {username}:")
        for post in posts:
            print(f"{post['text']}")
    else:
        print("Error:", response.text)

def get_joint_posts(username):
    url = "http://107.152.44.102:5000/view-joint-posts"  # Replace with your server's URL if needed
    data = {'username': username}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        joint_posts = response.json()
        post_dict = {}
        for post in joint_posts:
            user = post['username']
            if user not in post_dict:
                post_dict[user] = [post['text']]
            else:
                post_dict[user].append(post['text'])
        return post_dict
    else:
        print("Error:", response.text)
        return None
def add_friend_ss(username, friend):
    url = "http://107.152.44.102:5000/friends"  # Replace with your server's URL if needed
    data = {'username': username, 'friend': friend}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        print("Friend added successfully!")
    else:
        print("Error:", response.text)


def create_post(text, feed_listbox, username):
    feed_listbox.delete(0, tk.END)
    # Read input from the Post_text item and pass it to the Feed_listbox item
    print(text)
    post_to_feed(username, text)
    view_post(username)
    joint_posts = get_joint_posts(username)
    if joint_posts:
        for user, posts in joint_posts.items():
            feed_listbox.insert(tk.END, user + ": ")
            feed_listbox.insert(tk.END, "-------------------------------")
            print(f"{user}:")
            for post in posts:
                print(f"  {post}")
                feed_listbox.insert(tk.END, post)
