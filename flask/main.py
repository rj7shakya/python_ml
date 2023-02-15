from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        name = request.form['test']
        print(request.args['test'])
        return 'Hello World '+name
    else:
        return 'Hello World'


@app.route('/class/<int:id>')
def classes(id):
    if (id == 2):
        return redirect(url_for('hello_world'))
    return 'class id is ' + str(id)


@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
