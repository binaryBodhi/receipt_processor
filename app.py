from flask import Flask, request, jsonify
from pydantic import ValidationError
from schemas import ReceiptSchema
from memory_store import store
from utils import calculate_points
import uuid

# APP
app = Flask(__name__)


# PROCESS RECEIPT ENDPOINT
@app.route("/receipts/process", methods=["POST"])
def process_receipts():
    try:
        data = request.json
        receipt = ReceiptSchema(**data)

        points = calculate_points(receipt)

        receiptID = str(uuid.uuid4())
        store[receiptID] = points

        return jsonify({"id": receiptID}), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    

# GET POINTS ENDPOINT
@app.route("/receipts/<id>/points", methods=["GET"])
def get_points(id):
    points = store.get(id)
    if points is None:
        return jsonify({"error": "Receipt not found"}), 404
    return jsonify({"points": points}), 200


# MAIN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)