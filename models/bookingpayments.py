from main import db

class BookingPayment(db.Model):
    __tablename__= 'booking_payments'
    id = db.Column(db.Integer,primary_key=True)
    booking_id = db.Column(db.Integer,db.ForeignKey('booking_payments.id'))
    amount = db.Column(db.Integer)
    created_at= db.Column(db.String)
