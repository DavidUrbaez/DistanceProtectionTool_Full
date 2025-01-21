from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def read_root():
    return jsonify({"message": "Hello World from Flask on Vercel!"})


@app.route("/api/some-route")
def some_route():
    return jsonify({"message": "Some route"})


# For local development
if __name__ == "__main__":
    app.run(debug=True)
