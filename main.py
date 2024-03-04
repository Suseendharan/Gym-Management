import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

# Database Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '2004'
MYSQL_DB = 'gymmanagement'

# Connect to MySQL
db = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)
cursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    cursor.execute("SELECT * FROM Members")
    members_data = cursor.fetchall()
    print(members_data)
    return render_template('members.html', members_data=members_data)


@app.route('/insert_member', methods=['POST'])
def insert_member():
    if request.method == 'POST':
        name = request.form['name']
        contact_number = request.form['phone']
        email = request.form['email']
        membership_type = request.form['membership_type']
        start_date = request.form['join_date']

        sql = "INSERT INTO Members (name, contact_number, email, membership_type, start_date) VALUES (%s, %s, %s, %s, %s)"
        values = (name, contact_number, email, membership_type, start_date)

        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('members'))


@app.route('/trainers')
def trainers():
    cursor.execute("SELECT * FROM Trainers")
    trainers_data = cursor.fetchall()
    return render_template('trainers.html', trainers_data=trainers_data)


@app.route('/insert_trainer', methods=['POST'])
def insert_trainer():
    if request.method == 'POST':
        name = request.form['name']
        speciality = request.form['speciality']
        phone = request.form['Phone']

        sql = "INSERT INTO Trainers (name, speciality,Contact_number) VALUES (%s, %s, %s)"
        values = (name, speciality,phone)

        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('trainers'))

@app.route('/classes')
def classes():
    cursor.execute("SELECT * FROM Classes")
    classes_data = cursor.fetchall()
    return render_template('classes.html', classes_data=classes_data)


@app.route('/insert_class', methods=['POST'])
def insert_class():
    if request.method == 'POST':
        class_name = request.form['class_name']
        trainer_id = request.form['trainer_id']
        time = request.form['time']

        sql = "INSERT INTO Classes (class_name, trainer_id, time) VALUES (%s, %s, %s)"
        values = (class_name, trainer_id, time)

        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('classes'))


@app.route('/payments')
def payments():
    cursor.execute("SELECT * FROM Payments")
    payments_data = cursor.fetchall()
    return render_template('payments.html', payments_data=payments_data)


@app.route('/insert_payment', methods=['POST'])
def insert_payment():
    if request.method == 'POST':
        member_id = request.form['member_id']
        amount = request.form['amount']
        payment_date = request.form['payment_date']

        sql = "INSERT INTO Payments (member_id, amount, payment_date) VALUES (%s, %s, %s)"
        values = (member_id, amount, payment_date)

        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('payments'))

@app.route('/attendance')
def attendance():
    cursor.execute("SELECT * FROM attendance")
    attendance_data = cursor.fetchall()
    return render_template('attendance.html', attendance_data=attendance_data)


@app.route('/insert_attendance', methods=['POST'])
def insert_attendance():
    if request.method == 'POST':
        member_id = request.form['member_id']
        class_id = request.form['class_id']
        date = request.form['payment_date']

        sql = "INSERT INTO attendance ( member_id, class_id,date) VALUES (%s, %s, %s)"
        values = (member_id, class_id,date)

        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('attendance'))


if __name__ == '__main__':
    app.run(debug=True)

# Close the database connection
db.close()