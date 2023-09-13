from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/contact")
def contact():
    return "contact"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5005, debug=True)