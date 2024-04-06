from flask import Flask


app = Flask(__name__)



with app.app_context():
    from routes import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')