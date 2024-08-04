from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Index():
    return jsonify({'message': 'hi'})

if __name__ == "__main__":
    app.run(debug=True, port=8080)