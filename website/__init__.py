from flask import Flask, render_template

def create():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('layout.html')

    return app
