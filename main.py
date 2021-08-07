from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", title="Home", loggedin=False)

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Login")

@app.route("/login")
def login():
    return "<h1>login Stuff and whatever</h1>"

if __name__ == "__main__":
    app.run(debug = True)