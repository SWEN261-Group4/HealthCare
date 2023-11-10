from flask import Flask, render_template, request, redirect, url_for, session

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
        return render_template('medications.html')


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
