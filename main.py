from flask import Flask, render_template, request, redirect, send_from_directory
import csv

import os

app = Flask(__name__, )
print(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


def write_to_file(data):
        with open('database.txt', mode='a') as database:
            email=data['email']
            subject=data['subject']
            message=data['message']
            file=database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writer.writerow([email,subject,message])

# @app.route("/<username>")
# def hello_user(username=None):
#     return render_template('index.html',name=username)


# @app.route("/blog")
# def blog():
#     return "<p>This is a testing blog page</p>"


# @app.route("/blog/2023")
# def blog2():
#     return "<p>Testing 2023</p>"
