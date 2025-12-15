"""
    WARNING: This is meant as a mock of the authorization layer. It is assumed
    in a production app that a well vetted, shared internal package would be
    use by all services.
"""
from functools import wraps

import jwt  # real pkg is "pyjwt" not "jwt"
from flask import request, jsonify, make_response
from pathlib import Path

# Certainly don't store secrets in version control, and even though
# this doesn't need to be secret, it still needs to change per environment
# so, this isn't how you want to store a public key in a real app.
PUBLIC_KEY = Path('auth/public.key').read_text()

def auth_check(flask_view_func):
    @wraps(flask_view_func)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token: 
            return make_response(jsonify({"message": "No Token in Request"}), 401)
        try:
            decoded_token = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
            return flask_view_func(decoded_token, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({"message": "jwt.ExpiredSignatureError"}), 401)
        except jwt.InvalidTokenError as e:
            print("InvalidTokenError ERROR:", type(e), e)
            return make_response(jsonify({"message": "InvalidTokenError ERROR"}), 401)
        return make_response(jsonify({"message": "Unauthorized"}), 401)

    return decorator
