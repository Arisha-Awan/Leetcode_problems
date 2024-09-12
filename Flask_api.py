from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/get_data", methods=["GET"])
def get_data():
    response = {
        "message": "data fetch successfully",
        "data": {"key1": "value1", "key2": "value2"},
    }
    return jsonify(response)


@app.route("/fetch_data", methods=["GET"])
def fetch_data():
    response = get_data()
    data = response.get_json()
    if isinstance(data, dict):
        return response

    return jsonify({"message": "data is not in correct format", "data": {}}), 400


if __name__ == "__main__":
    app.run(debug=True)
