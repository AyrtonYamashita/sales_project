from flask import Flask
from .routes.register_user_data import register_bp
import uuid

app = Flask(__name__)
uid = uuid.uuid4()

app.register_blueprint(register_bp, url_prefix='/register')

if __name__ == "__main__":
    app.run(debug=True)