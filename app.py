from flask import Flask, request, render_template
from nypass import get_content

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/content', methods=['POST'])
def content():
    url = request.form['url']
    text = get_content(url)
    return render_template('content.html', text=text)
