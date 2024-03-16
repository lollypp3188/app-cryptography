from flask import Flask
# from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)



# app.config['PREFERRED_URL_SCHEME'] = 'https'

# # Apply ProxyFix middleware to handle reverse proxy headers
# app.wsgi_app = ProxyFix(app.wsgi_app)


with app.app_context():
    from routes.main import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')