import random
from flask import Flask, render_template
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    seed = random.randint(0, sys.maxint)
    return gen_pattern(seed)


@app.route('/<seed>')
def gen_pattern(seed):
    generator = random.Random(seed)

    rows = []
    cols = []

    for y in range(0, 40):
        cols = []
        for x in range(0, 40):
            cols.append(str(generator.randint(0, 255)))
        rows.append(cols)
    return render_template("table.html", rows=rows, cols=cols)


if __name__ == '__main__':
    app.run(debug=True)
