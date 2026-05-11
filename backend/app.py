from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__)

@app.route('/frontend/<path:path>')
def send_frontend(path):
    return send_from_directory('frontend', path)

@app.route('/')
def home():
    return redirect('/frontend/login.html')

@app.route('/login', methods=['POST'])
def login():

    role = request.form['role']

    if role == 'admin':
        return redirect('/frontend/admin-dashboard.html')

    else:
        return redirect('/frontend/user-dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)