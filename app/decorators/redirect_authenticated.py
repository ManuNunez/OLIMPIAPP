from functools import wraps
from flask import redirect, url_for, session, flash

def redirect_authenticated(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'user_id' in session:     
            return redirect(url_for('home.index'))
        return f(*args, **kwargs)
    return decorator
