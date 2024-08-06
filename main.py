from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:6979@localhost/flask_al_t'
db = SQLAlchemy(app)

from models.student import Student
from models.course import Course
from models.booking import Booking
from models.bookingpayments import BookingPayment


with app.app_context():
    db.create_all()

app.run(debug=True)

# source env/Scripts/activate
# export FLASK_APP=main.py
# flask run


# created_at = server_default=func.now()