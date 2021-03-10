from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class voter(db.Model):
    __tablename__ = "voters"
    UserId = db.Column(db.String, primary_key=True)
    Password = db.Column(db.String, nullable=False)
    Age = db.Column(db.String, nullable=False)
    Area = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __init__(self, UserId, Password, Age, Area, status):
        self.UserId = UserId
        self.Password = Password
        self.Age = Age
        self.Area = Area
        self.status = status


class candidate(db.Model):
    __tablename__ = "candidates"
    Name = db.Column(db.String, primary_key=True)
    Votes = db.Column(db.Integer, nullable=False)

    def __init__(self, Name, Votes):
        self.Name = Name
        self.Votes = Votes
