from flask import Flask, render_template
import os

app = Flask(__name__)

API_URL = os.getenv("API_URL", "http://127.0.0.1:5000")

@app.route('/')
def index():
    return render_template('index.html', api_url=API_URL)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
