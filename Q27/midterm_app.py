from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def login():
    return render_template("Login.html")

@app.route("/reg")
def register():
    return render_template("Registration.html")

if __name__== "__main__":
    app.run(host = "0.0.0.0", port= 5000, debug=True)