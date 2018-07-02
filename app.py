'''
svakulenko
2 Jul 2018

Flask web app for chatbot interface based on https://github.com/chamkank/flask-chatterbot
'''
from flask import Flask, render_template, request

from chatbot import Chatbot

app = Flask(__name__)

my_chatbot = Chatbot()


@app.route("/")
def init():
    return render_template("chatbot.html")


@app.route("/search")
def search():
    user_message = request.args.get('msg')
    bot_response = my_chatbot.search(user_message)
    return bot_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8008)
