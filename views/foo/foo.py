from flask import Blueprint

foo = Blueprint('foo', __name__)

@foo.route('/')
def foo_view():
    return "<h1> This is a blueprint! </h1>"