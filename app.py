from flask import Flask


app = Flask(__name__)



with app.app_context():
    from routes.main import *
    from routes.caesar import *
    from routes.permutation import *
    from routes.playfair import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')