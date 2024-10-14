from flask import Flask

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return {"status": "OK"}, 200

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port, debug=True)

