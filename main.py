from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'steven'

USERS = {
    'ruby': 'red',
    'sapphire': 'blue',
    'jasper': 'orange'
}
