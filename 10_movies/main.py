from flask import Flask, render_template, request, redirect

app = Flask(__name__)

moviesArr = ['Avatar', 'Avengers', 'RRR']


@app.route('/', methods=['POST', 'GET'])
def home():
    global moviesArr
    if request.method == 'POST':
        moviesArr.append(request.form['name'])
        # return 'new movie '+request.form['name']
        return redirect('/movies')
    else:
        return render_template('add.html')


@app.route('/movies')
def movies():
    global moviesArr
    print(moviesArr)
    return render_template('index.html', movies=moviesArr)


if __name__ == '__main__':
    app.run(debug=True)
