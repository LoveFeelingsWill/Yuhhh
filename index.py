from flask import Flask, render_template

app = Flask(name)

@app.route("/")

def index():

    return render_template("index.html")

if name == "__main__":

    app.run(debug=True)

