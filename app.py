from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/1536Osceola')
def home():
    return render_template('index.html')

@app.route('/request')
def request():
    return render_template('request.html')

@app.route('/shoppinglist')
def shop():
    return render_template('shop.html')

if __name__ == "__app__":
    app.run(debug=True)