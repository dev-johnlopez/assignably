from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.auth.models import User
from app.api.errors import error_response

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    print("SEARCHING USER!")
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    print("CHECKING USER PASSWORD!")
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    print("BASIC AUTH ERROR!")
    return error_response(401)


@token_auth.verify_token
def verify_token(api_key):
    print("VERIFYING TOKEN!")
    g.current_user = User.check_api_key(api_key) if api_key else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    print("ERROR LOGGING IN!")
    return error_response(401)
