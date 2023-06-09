from flask import Flask, render_template, request, session
import sqlalchemy

app = Flask(__name__)
app.secret_key = "insecurekey"
db = sqlalchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # No input validation or sanitization

    # No parameterized queries - vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = db.engine.execute(query)

    # No password security - storing plaintext passwords
    if result:
        session['username'] = username
        return "Login successful"
    else:
        return "Invalid username or password"

# No secure session management

# No principle of least privilege

if __name__ == '__main__':
    app.run(debug=True)
