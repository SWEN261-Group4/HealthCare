from flask import Flask, render_template, request, redirect, url_for, session, current_app
from class_config import Config
import uuid

app = Flask(__name__)
config = Config()
app.secret_key = 'steven'

USERS = {
    'ruby': 'red',  # fitness wellness trainer (will use health logger a lot)
    # health-conscious medical patient (will use appointments & medications a lot)
    'sapphire': 'blue',
    'jasper': 'orange'  # old person (general use)
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and password == USERS[username]:
            session['username'] = username
            return redirect(url_for('user_profile'))
        else:
            return 'Invalid user. Please try again'

    return render_template('login.html')


@app.route('/')
def user_profile():
    if 'username' in session:
        username = session['username']
        welcome_message = f"Welcome back, {username}!"
        return render_template('user.html', welcome_message=welcome_message, username=username)
    return redirect(url_for('login'))


@app.route('/medications')
def medications():
    if 'username' in session:
        username = session['username']
        user_ids = {'ruby': 'U001', 'sapphire': 'U002', 'jasper': 'U003'}
        user_id = user_ids.get(username)
        medications = config.get_meds('medications', user_id)
        return render_template('medications.html', medications=medications,  username=username)
    else:
        return redirect(url_for('login'))


@app.route('/health_logger', methods=['GET', 'POST'])
def health_logger():
    log_health = None
    if 'username' in session:
        username = session['username']
        user_ids = {'ruby': 'U001', 'sapphire': 'U002', 'jasper': 'U003'}
        user_id = user_ids.get(username)

        if request.method == 'POST':
            heart_rate = request.form['heartRate']
            blood_pressure = request.form['bloodPressure']
            body_temperature = request.form['bodyTemperature']

            config.add_healthlog(user_id, heart_rate,
                                 blood_pressure, body_temperature)

        # Retrieve health logs specific to the current user
        log_health = config.get_health_logs(user_id)
        return render_template('healthlogger.html', log_health=log_health)
    else:
        return redirect(url_for('login'))


@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    appointments = None
    available_timings = None

    if 'username' in session:
        username = session['username']
        doctors = [
            {'id': 'D001', 'name': 'Dr. Rick'},
            {'id': 'D002', 'name': 'Dr. Garfield'}
        ]
        user_ids = {'ruby': 'U001', 'sapphire': 'U002', 'jasper': 'U003'}
        user_id = user_ids.get(username)

        if username == 'ruby':
            doctor_id = doctors[0]['id']
            doctor_name = doctors[0]['name']
        elif username == 'sapphire':
            doctor_id = doctors[0]['id']
            doctor_name = doctors[0]['name']
        elif username == 'jasper':
            doctor_id = doctors[1]['id']
            doctor_name = doctors[1]['name']

        if request.method == 'POST':
            appointment_date = request.form['appointment_date']
            slot_time = request.form['slot_time']
            doctor_full_name = doctor_name
            doctor_id = doctor_id
            appointment_id = f"A{str(uuid.uuid4())[:3]}"

            config.add_appointment(
                appointment_id, user_id, appointment_date, slot_time, doctor_full_name, doctor_id)

            config.book_appointment(doctor_id, appointment_date, slot_time)

        # retrieve appointments data specific to the user
        appointments = config.get_appointments(user_id)

        # retrieve doctor available timings
        available_timings = config.get_available_timings(doctor_id)

        return render_template('appointments.html', appointments=appointments, available_timings=available_timings, doctors=doctors, doctor_name=doctor_name, username=username)
    else:
        return redirect(url_for('login'))


@app.route('/aboutme')
def about_me():
    if 'username' in session:
        username = session['username']
        return render_template('aboutme.html', username=username)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
