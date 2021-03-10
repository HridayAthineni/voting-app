import os
from flask import Flask

from voters_db import *

APP = Flask(__name__)

APP.config["SQLALCHEMY_DATABASE_URI"] = "postgres://erqqvzscrzipjr:e0c4dccf2d2b7f7f5e04fbe4c0c8e21957455dcd909b5759d433a5b69f084171@ec2-52-23-14-156.compute-1.amazonaws.com:5432/dc3k02bm1vj0d4"
# os.getenv("DATABASE_URL")
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(APP)


def main():
    db.create_all()


if __name__ == '__main__':
    with APP.app_context():
        main()
