# use cmd run
from flask import Flask, jsonify, render_template

# create flask app
app = Flask(__name__)


@app.route("/")
# def index():
#     return "This is my homepage"
@app.route("/hello/<name>")
def homme(name=None):
    return render_template('index.html', name=name)


@app.route('/info', methods=['POST'])
def returnSomething():
    return jsonify({'info': 'You have successfully make a request.'})


if __name__ == '__main__':
    app.run(debug=True)
