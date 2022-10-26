import os
from flask import Flask, jsonify

app = Flask(__name__)
app['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return jsonify({"success": "HelloWorld!"})

if __name__ == "__main__":
    app.run(debug=True)
