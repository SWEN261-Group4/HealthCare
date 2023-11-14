from flask import Flask, render_template, request, redirect, url_for, session
from class_config import Config

app = Flask(__name__)
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
        if username == 'ruby':
            return render_template('user_ruby.html', welcome_message=welcome_message)
        elif username == 'sapphire':
            return render_template('user_sapphire.html', welcome_message=welcome_message)
        elif username == 'jasper':
            return render_template('user_jasper.html', welcome_message=welcome_message)
    return redirect(url_for('login'))


@app.route('/medications')
def medications():
    if 'username' in session:
        username = session['username']
        user_ids = {'ruby': 'U002', 'sapphire': 'U001', 'jasper': 'U003'}
        user_id = user_ids.get(username)
        table_data = config.get_table('medications')

        if user_id:
            # Fetch medications based on the user_id
            # Use dictionary cursor to fetch rows as dictionaries
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                f"SELECT medication_1, medication_2 FROM medications WHERE user_id = '{user_id}'")
            medications = cursor.fetchall()
            cursor.close()

            return render_template('medications.html', medications=medications)


@app.route('/health_logger')
def health_logger():
    if 'username' in session:
        return render_template('healthlogger.html')


@app.route('/appointments')
def appointments():
    if 'username' in session:
        return render_template('appointments.html')


@app.route('/aboutme')
def about_me():
    if 'username' in session:
        return render_template('aboutme.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
