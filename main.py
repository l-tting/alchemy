from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:6979@localhost/students_system'

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__= 'students'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    national_id = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    booking = db.relationship('Booking',backref='student')

class Course(db.Model):
    __tablename__= 'courses'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String,nullable=False)
    description = db.Column(db.String,nullable=False)
    cost = db.Column(db.Integer,nullable=False)
    start_date = db.Column(db.Date,nullable=False)
    end_date = db.Column(db.Date,nullable=False)
    status = db.Column(db.Boolean,default=False,nullable=False)
    booking = db.relationship('Booking',backref="course")

    
class Booking(db.Model):
    __tablename__= 'bookings'
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer,db.ForeignKey('courses.id'))
    completion_status = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime,server_default=func.now())
    booking_payment = db.relationship('BookingPayment',backref='booking')

class BookingPayment(db.Model):
    __tablename__= 'booking_payments'
    id = db.Column(db.Integer,primary_key=True)
    booking_id = db.Column(db.Integer,db.ForeignKey('bookings.id'))
    amount = db.Column(db.Integer)
    created_at= db.Column(db.DateTime,server_default=func.now())


@app.route('/student',methods=['GET','POST'])
def student():
    if request.method == 'GET':
        students = db.session.execute(db.select(Student).order_by(Student.name)).scalars()
        return render_template("students.html", students=students)
    else:
        name = request.form['name']
        email = request.form['email']
        national_id= request.form['national_id']
        status = bool(request.form['status'])
        student = Student(name=name,email=email,national_id=national_id,status=status)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('student'))

@app.route('/courses',methods=['GET','POST'])
def courses():
    if request.method == 'GET':
        courses = db.session.execute(db.select(Course).order_by(Course.name)).scalars()
        return render_template("courses.html", courses=courses)
    else:
        name = request.form['name']
        description = request.form['description']
        cost= request.form['cost']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        status = bool(request.form['status'])
        course = Course(name=name,description=description,cost=cost,start_date=start_date,end_date=end_date,status=status)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses'))

@app.route('/bookings',methods=['GET','POST'])
def bookings():
    if request.method == 'GET':
        bookings = db.session.execute(db.select(Booking).order_by(Booking.student_id)).scalars()
        courses = db.session.execute(db.select(Course).order_by(Course.name)).scalars()
        students = db.session.execute(db.select(Student).order_by(Student.name)).scalars()
        return render_template("booking.html",bookings=bookings,courses=courses,students=students)
    else:
        student_id = request.form['student']
        course_id = request.form['course']
        completion_status= bool(request.form['status'])
        
        booking = Booking(student_id=student_id,course_id=course_id,completion_status=completion_status)
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('bookings'))


with app.app_context():
    db.create_all()

app.run(debug=True)

