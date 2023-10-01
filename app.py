from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, welcome to Brian's resume website!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

