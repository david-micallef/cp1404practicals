from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)

@app.route('/f/<celsius>')
def calculate_fahrenheit(celsius=""):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return '{} Celsius converts to {} Fahrenheit'.format(celsius, fahrenheit)

@app.route('/c/<fahrenheit>')
def calculate_celsius(fahrenheit=""):
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return '{} Fahrenheit converts to {} Celsius'.format(fahrenheit, celsius)



if __name__ == '__main__':
    app.run()
