from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
db = SQLAlchemy(app)


class Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(50), nullable=False)
    connection = db.Column(db.String(50), nullable=False)
    integration = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payers = db.Column(db.String(50), nullable=False)
    payment_system = db.Column(db.String(50), nullable=False)
    bank = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Information %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        connection = request.form['connection']
        if connection != 'With website':
            integration = 'Without integration'
        else:
            integration = request.form['integration']

        information = Information(
            client=request.form['client'],
            connection=connection,
            integration=integration,
            payment_method=request.form['payment_method'],
            payers=request.form['payers'],
            payment_system=request.form['payment_system'],
            bank=request.form['bank']
        )
        try:
            db.session.add(information)
            db.session.commit()
            return redirect('/orders')
        except:
            return '[ERROR]: Information has not been added!'
    else:
        return render_template('index.html')


@app.route('/orders')
def orders():
    all_orders = Information.query.order_by(Information.id).all()
    return render_template('orders.html', all_orders=all_orders)


@app.route('/orders/<int:order_id>/delete')
def post_delete(order_id):
    order = Information.query.get_or_404(order_id)
    try:
        db.session.delete(order)
        db.session.commit()
        return redirect('/orders')
    except:
        return "[ERROR]: Order has not been deleted!"


if __name__ == '__main__':
    app.run(debug=True)