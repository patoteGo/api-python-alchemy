from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sdgjqrizoydkdr:d2ac2d23b620205d94a6adb3697e9049d6f2e7ce49b468886358e0fcf4615a06@ec2-54-86-170-8.compute-1.amazonaws.com/d7thrjda3s0jtv" # postgresql://user:pass@localhost/mydatabase

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/', methods=['GET'])
def test():
  return 'test'


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=3245, debug=True)