from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  last_name = db.Column(db.String(100), nullable=False)
  active = db.Column(db.Boolean, nullable=False)
  users = db.relationship('User', backref='person', lazy=True)

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "last_name": self.last_name,
      "active": self.active,
    }
  def getFullName(self):
    return {
      "id": self.id,
      "full_name": self.name + " " + self.last_name
    }