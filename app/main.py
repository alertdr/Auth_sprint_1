from flask import Flask

from app.core.config import Config
from db.db import pg_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

pg_db.init_app(app=app)


def main(flask_app):
    flask_app.run(debug=True, host='0.0.0.0', port=5001)


if __name__ == '__main__':
    main(app)
