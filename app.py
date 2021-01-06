from flask import Flask, render_template
from views.foo.foo import foo

app = Flask(__name__)
app.register_blueprint(foo, url_prefix='/foo')

@app.route('/')
def index():
    return '<h1> This is the main page </h1>'

if __name__ == '__main__':
    app.run()