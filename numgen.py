from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/<int:param>")
def hello_world(param):
    return render_template('index.html', saida=range(param))


if __name__ == '__main__':
    app.run(debug=True)
