import json
from flask import render_template, Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/cleanblog"
db = SQLAlchemy(app)


class Contacts(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Fetch form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone_no = request.form.get('phone')
        msg = request.form.get('message')

        # Get the current date
        date = datetime.now().strftime("%Y-%m-%d")  # Add current date

        # Save to the database
        entry = Contacts(name=name, email=email, phone_no=phone_no, msg=msg, date=date)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)
