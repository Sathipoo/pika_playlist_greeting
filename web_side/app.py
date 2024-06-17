from flask import Flask, render_template
import yaml

app = Flask(__name__)

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

@app.route('/')
def index():
    config = load_config()
    return render_template('index.html', pages=config['pages'])

if __name__ == '__main__':
    app.run(debug=True)