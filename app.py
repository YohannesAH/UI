from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_digit():
    url = 'http://10.104.80.77:6000'

    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

@app.route('/convert', methods=['POST'])
def convert():
    url = 'http://10.102.124.20:5001'

    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

@app.route('/translate', methods=['POST'])
def translate():
    url = 'http://10.99.8.187:5002'

    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    url = 'http://10.108.28.39:5004'

    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

if __name__ == '__main__':
    app.run()
