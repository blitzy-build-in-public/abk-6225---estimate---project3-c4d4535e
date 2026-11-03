from flask import Flask

app = Flask(__name__)
METHODS = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]


@app.route("/", methods=METHODS)
@app.route("/<path:path>", methods=METHODS)
def hello(path=""):
    return "Hello, World!\n"


if __name__ == "__main__":
    print("Server running at http://127.0.0.1:3000/")
    app.run(port=3000)
