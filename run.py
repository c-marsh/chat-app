import os
from datetime import datetime 
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """add messages to messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """get all messages and separate them with  a `br`"""
    return "<br>".join(messages)


@app.route('/')
def index():
    """main page brief instructions"""
    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """display chat messages"""
    return "<h1>Welcome, {0}<h1> {1}".format(username.title(),
                                             get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """create new message and redirect to chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
