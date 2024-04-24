# Put your app in here.
from flask import Flask
import operations

app = Flask(__name__)


@app.get("/add")
def add_numbers():
    """ Add a and b and return result. """

    a = request.args["a"]
    b = request.args["b"]

    add(a, b)

# get the values of a and b
# use add function imported from operations to add
# add result to body of html string and return
