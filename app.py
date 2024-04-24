# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.get("/math/<operation>")
def calc_numberso(operation):
    """ Add a and b and return result as HTML string """

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = OPERATIONS[operation](a, b)

    return f"""
      <html>
        <body>
          <h1>Results: {result}</h1>
        </body>
      </html>
      """

