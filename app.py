from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    random_number = random.randint(1, 10)
    return f"<html><body><h1>Random Number</h1><p>Your random number is: {random_number}</p></body></html>"

if __name__ == "__main__":
    app.run(debug=True) 
