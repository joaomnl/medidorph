# pip install flask
from flask import Flask
from projeto import projeto

app = Flask(__name__)
app.register_blueprint(projeto, url_prefix="/projeto")

if __name__ == '__main__':
    app.run(debug=True, port=8000)