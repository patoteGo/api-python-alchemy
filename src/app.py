from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123.admin@localhost/ejemplo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/', methods=['GET'])
def test():
  return 'test'


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=3245, debug=True)