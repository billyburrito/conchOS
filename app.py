import os
import random
from flask import Flask, render_template

app = Flask(__name__)

conch = ["i_dont_think_so", "maybe_someday", "neither", "no_sassy", "no2", "nothing", "try_asking_again", "yes1"]

def play_answer(input):
    os.system("aplay " + "./conch/" + input + ".wav")

def list_responses(in_data):
    stuff = '<a href="/">main</a> '
    for i in in_data:
        stuff += "<a href=/"+i+">"+i+"</a> "
    return stuff

@app.route('/')
def index():
    play_answer(random.choice(conch))
    return list_responses(conch)

@app.route('/<data>')
def answer(data):
    play_answer(data)
    return list_responses(conch)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

