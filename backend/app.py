from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get', methods = ['GET'])
def get_article():
    return jsonify({"Hello":"World"})

if __name__ == "__main__":
    app.run(debug=True)