from flask import Flask, render_template

app = Flask(__name__)

# Set security headers
@app.after_request
def set_security_headers(response):
    # HTTP Strict Transport Security (HSTS)
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'

    # X-XSS-Protection
    response.headers['X-XSS-Protection'] = '1; mode=block'

    # X-Content-Type-Options
    response.headers['X-Content-Type-Options'] = 'nosniff'

    # X-Frame-Options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'

    return response

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
