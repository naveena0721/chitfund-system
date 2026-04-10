from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Chit Fund System Backend Running 🚀"

if __name__ == '__main__':
    app.run(debug=True)