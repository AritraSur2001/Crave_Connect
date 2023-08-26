from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Surloves#69@localhost/food'
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customers'
    cus_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    contact = db.Column(db.Integer)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cus_id = request.form['customerId']
        customer = Customer.query.get(cus_id)

        if customer:
            return render_template('show_cus_index.html', customer=customer)
        else:
            customer_info = None
            return render_template('show_cus_index.html', customer_info=customer_info)

    return render_template('show_cus_index.html')

@app.route('/get_customer_info/<int:customer_id>', methods=['GET'])
def get_customer_info(customer_id):
    customer = Customer.query.get(customer_id)

    if customer:
        customer_info = {
            'name': customer.c_name,
            'email': customer.email,
            'contact': customer.contact
        }
        return jsonify(customer_info)
    else:
        return jsonify(error="Customer not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
