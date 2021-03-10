import os
from flask import Flask

from voters_db import *

APP = Flask(__name__)

APP.config["SQLALCHEMY_DATABASE_URI"] = "postgres://kkyorsvsudekje:50d2cf9cd8cf7d0e44f2e39c3de05d71bedc0abb959a876e0824917f71a25ab7@ec2-54-162-119-125.compute-1.amazonaws.com:5432/dc7hua40a4apb6"
# os.getenv("DATABASE_URL")
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(APP)


def main():
    db.create_all()


if __name__ == '__main__':
    with APP.app_context():
        main()
