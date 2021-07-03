from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask_cors import CORS, cross_origin
import storage

app = Flask(__name__)
CORS(app)

@app.route('/')
def Main():
    return '<h1>HOOOOOLLLLaaaaa</h1>'

# @app.route('/booklist/v1/', methods=['GET'])
# def GetAll():
#     if request.method == "GET":
#         result = storage.GetBookList()
#         return result

# @app.route('/booklist/v1/', methods=['POST'])
# def Insert():
#     if request.method == "POST":
#         book = request.args
#         result = storage.InsertBook(book)
#         return result

# @app.route('/booklist/v1/', methods=['PUT'])
# def Update():
#     if request.method == "PUT":
#         book = request.args
#         result = storage.UpdateBook(book)
#         return result

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")