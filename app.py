# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.get("/add")
def add_numbers():
    """ Add a and b and return result as HTML string """

    a = int(request.args.get["a"])
    b = int(request.args.get["b"])

    result = operations.add(a, b)

    return f"""
      <html>
        <body>
          <h1>Results: a + b = {result}</h1>
        </body>
      </html>
      """

# get the values of a and b
# use add function imported from operations to add
# add result to body of html string and return
