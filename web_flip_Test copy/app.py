from flask import Flask, render_template
import yaml

app = Flask(__name__)

@app.route('/')
def home():
    with open('pages.yaml') as f:
        pages = yaml.safe_load(f)['pages']
    return render_template('index.html', pages=pages)

if __name__ == '__main__':
    app.run(debug=True)