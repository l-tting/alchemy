from main import db
class Booking(db.Model):
    __tablename__= 'bookings'
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer,db.ForeignKey('courses.id'))
    completion_status = db.Column(db.Boolean)
    created_date = db.Column(db.String)
    booking_payment = db.relationship('BookingPayment',backref='booking_payment')

