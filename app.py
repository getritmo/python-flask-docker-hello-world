from flask import Flask
import os

app = Flask(__name__)

@app.route("/__health")
def hello():
    return "Ritmo dummy service for testing!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True,host='0.0.0.0',port=port)
