from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rolunk')
def rolunk():
    return render_template('rolunk.html')

@app.route('/szolgaltatasok')
def szolgaltatasok():
    return render_template('szolgaltatasok.html')

@app.route('/kapcsolat')
def kapcsolat():
    return render_template('kapcsolat.html')

if __name__ == '__main__':
    app.run(debug=True)
