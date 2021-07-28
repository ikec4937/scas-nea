from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", title="Home", loggedin=False)

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Login")

if __name__ == "__main__":
    app.run(debug = True)