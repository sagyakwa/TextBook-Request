import smtplib
import ssl
from os.path import join, dirname, abspath

import yaml
from flask import Flask, render_template, request

import libgen

credential_location = join(dirname(abspath(__file__)), 'credentials')
credentials = yaml.load(open(credential_location))

libgenio = 'http://93.174.95.29'
libgenme = 'http://libgen.me'
booksdl = 'http://libgen.io/get'

port = 465
from_email = credentials['credentials']['from_email']
password = credentials['credentials']['password']
# to_email = credentials['credentials']['to_email']

context = ssl.create_default_context()

app = Flask(__name__)


@app.route("/")
def home():
    global name, to_email, textbook
    name = request.form.get('username')
    to_email = request.form.get('email')
    textbook = request.form.get('textbook')
    return render_template('index.html')


@app.route('/', methods=['POST'])
def form_post():
    global name, to_email, ISBN
    name = request.form.get('name')
    to_email = request.form.get('email')
    ISBN = request.form.get('ISBN')

    get = libgen.Get(ISBN)
    link_mirror_1 = get.link_from()
    link_mirror_2 = get.link_from(libgenme, 'Get from vault')
    link_mirror_3 = get.link_from(booksdl)
    links = link_mirror_1 + link_mirror_2 + link_mirror_3
    new_list = '\n\n'.join('{}'.format(item) for item in links)

    msg = f'Hey {name}, \nHere are the links for download\n{new_list}'
    subject = 'Textbook Links'
    info = 'Subject: {}\n\n{}'.format(subject, msg)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        print(info)
        print(to_email)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, info)
        server.quit()

    return render_template('restart.html')


if __name__ == "__main__":
    app.run(debug=True)
