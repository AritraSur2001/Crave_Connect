from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Surloves#69@localhost/food'
db = SQLAlchemy(app)

class Contacting(db.Model):
    __tablename__ = 'SUPPORT'
    sup_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    dated = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(30))
    message = db.Column(db.String(300))

@app.route("/")
def contacting():
    return render_template("index_contact.html")

@app.route("/contact", methods=['GET', 'POST'])
def reach():
    if request.method == 'POST':
        # add an entry to the database
        cus_id = request.form.get('Name')
        email = request.form.get('E-mail')
        msg = request.form.get('Your_Message')

        entry = Contacting(name=cus_id, dated=str(datetime.now()), email=email, message=msg)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact_details.html")

app.run(debug=True)