from flask import Flask, jsonify
from mlib.mchange import change

app = Flask(__name__)


@app.route("/")
def Index():
    return jsonify({"message": "hi"})


@app.route("/change/<dollars>/<cents>")
def change_route(dollars, cents):
    print(f"Make change for {dollars}.{cents}")
    return jsonify(change(float(f"{dollars}.{cents}")))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
