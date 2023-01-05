from flask import Flask, jsonify, request
from client import call_method
from deploy import deploy

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify({'message': 'pong para ver si sirve flask 2 :)'})


@app.route("/deploy")
def deploy_smart_contract():
    response = deploy()
    return jsonify({'data': response})


@app.route("/call-method")
def call():
    call_m = call_method(app)
    return jsonify({'data': call_m })


if __name__ == "__app__":
    app.run(debug=True, host='0.0.0.0')
