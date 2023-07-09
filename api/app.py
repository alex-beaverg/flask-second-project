from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        info = {
            'client': request.form['client'],
            'connection': request.form['connection'],
            'integration': request.form['integration'],
            'payment_method': request.form['payment_method'],
            'payers': request.form['payers'],
            'payment_system': request.form['payment_system'],
            'bank': request.form['bank']
        }
        return render_template('index.html', info=info)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)