from flask import Flask, request, jsonify
from PM_APP_Models import Schema
from PM_APP_Service import ReqServ
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def create_Requirements():
    return jsonify(ReqServ().create(request.get_json()))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)