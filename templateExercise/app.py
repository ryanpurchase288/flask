from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main')
def main_():
    return render_template('main.html', users=['ben', 'harry', 'bob', 'jay', 'matt', 'bill'])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
