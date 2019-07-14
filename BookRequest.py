import smtplib
import ssl
from os.path import join, dirname, abspath

import yaml

from flask import Flask, render_template, request

credential_location = join(dirname(abspath(__file__)), 'credentials')
credentials = yaml.load(open(credential_location))

port = 465
from_email = credentials['credentials']['from_email']
password = credentials['credentials']['password']
to_email = credentials['credentials']['to_email']

context = ssl.create_default_context()

app = Flask(__name__)


@app.route("/")
def home():
    global name, email, textbook
    name = request.form.get('username')
    email = request.form.get('email')
    textbook = request.form.get('textbook')
    return render_template('index.html')


@app.route('/', methods=['POST'])
def form_post():
    global name, email, textbook, author, ISBN
    name = request.form.get('name')
    email = request.form.get('email')
    textbook = request.form.get('textbook')
    author = request.form.get('author')
    ISBN = request.form.get('ISBN')

    msg = f'{name}\n{email}\n{textbook}\n{author}\n{ISBN}\n\n'
    subject = "New Text Book Request"
    info = 'Subject: {}\n\n{}'.format(subject, msg)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, info)
        server.quit()

    return render_template('restart.html')


if __name__ == "__main__":
    app.run(debug=True)
