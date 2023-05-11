import random

from flask import Flask, render_template
app = Flask(name)


STRINGS = [
"Are you sussy baka?",
"What Fuck Are you looking for?",
"Who tf are you?",
"Nothing, what are you looking so for?"
]

@app.route("/")
def index():
    fuck = random.choice(STRINGS)
    return fuck 

if name == "__main__":

    app.run(debug=True)

