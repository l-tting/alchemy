from main import db

class Course(db.Model):
    __tablename__= 'courses'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String,nullable=False)
    description = db.Column(db.String,nullable=False)
    cost = db.Column(db.Integer,nullable=False)
    start_date = db.Column(db.Date,nullable=False)
    end_date = db.Column(db.Date,nullable=False)
    status = db.Column(db.Boolean,default=False,nullable=False)
    booking = db.relationship('Course',backref="course")