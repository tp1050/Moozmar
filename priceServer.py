
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tgju')
def tgju():
    return render_template('tgju.org.html')


def main():
    app.run(debug=True, threaded=True,host= '0.0.0.0',port=4209821)

if __name__ == "__main__":
    main()