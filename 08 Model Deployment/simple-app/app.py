
from flask import Flask

app = Flask(__name__)

#Main endpoint
@app.route("/")
def home():
    return "<h1>Hello, World!</h1> <p>This is our first Flask app.</p>"

#Another endpoint
@app.route('/aai')
def hello():
    return "<h1>Hello, Class!</h1> <h3>This is a second page specifically for AAI.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
