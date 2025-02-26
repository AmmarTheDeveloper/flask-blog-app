from functools import wraps
from flask import redirect,session

def login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if not session.get("user"):
            return redirect("/login")
        return f(*args,**kwargs)
    return decorated_function

def logout_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if session.get("user"):
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function