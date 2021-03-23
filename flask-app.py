from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/SubmitTicket')
def submit_ticket():

    return render_template('SubmitTicket.html')


@app.route('/ViewTicket')
def view_ticket():

    return render_template('ViewTicket.html')


@app.route('/Login')
@app.route('/Admin')
def login():

    return render_template('Login.html')

if __name__ == '__main__':
    app.run()
