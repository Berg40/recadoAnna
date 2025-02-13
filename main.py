from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('principal.html')

@app.route('/recado1')
def recado1():
    return render_template('recado1.html')

@app.route('/recado2')
def recado2():
    return render_template('recado2.html')

@app.route('/recado3')
def recado3():
    return render_template('recado3.html')

@app.route('/recado4')
def recado4():
    return render_template('recado4.html')

@app.route('/recado5')
def recado5():
    return render_template('recado5.html')

if __name__ == '__main__':
    app.run(debug=True)