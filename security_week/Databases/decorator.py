# decorator to check if user is logged in

from functools import wraps

from flask import session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return f'<h2>You must be logged in to view this page</h2>'
        return f(*args, **kwargs)
    return decorated_function


# decorator to validate admin access
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['role'] != 'admin':
            return f'<h2>You must be an admin to view this page</h2>'
        return f(*args, **kwargs)
    return decorated_function