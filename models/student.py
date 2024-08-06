from main import db

class Student(db.Model):
    __tablename__= 'students'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    national_id = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    booking = db.relationship('Booking',backref='student')
