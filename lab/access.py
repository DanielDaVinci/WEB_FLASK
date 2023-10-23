from flask import session
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            return func(args, kwargs)
        else:
            return 'Вам необходимо зарегестрироваться'

    return wrapper
