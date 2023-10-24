from flask import Flask, request, render_template
from pyshared.regexutils.regexutilities import is_alpha_or_numberic

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expression = request.form['user_input']
        result = is_alpha_or_numberic(expression)
        response = f'{expression} is alpha-numeric? {result}'
        return render_template('index.html', response=response)
    else:
        return render_template('index.html', response=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, debug=True)
