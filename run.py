from flask import Flask
from routes.register_user_data import register_bp_user, register_bp_address_recip, register_bp_address_send
app = Flask(__name__)

app.register_blueprint(register_bp_user, url_prefix='/register')
app.register_blueprint(register_bp_address_send, url_prefix='/register')
app.register_blueprint(register_bp_address_recip, url_prefix='/register')


if __name__ == "__main__":
    app.run(debug=True)
