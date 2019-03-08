from flask import Flask

app = Flask(__name__)


def find_factors(num):
    return [x for x in range(1, num + 1) if num % x == 0]


# convert integers to numbers
@app.route("/factors/<int:num>")
def find_factors_route(num):
    return f"The factor of {num} are {find_factors(num)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
