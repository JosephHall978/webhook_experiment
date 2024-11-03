from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get_ifo():
    bloodSugar = 7
    unit = "mmol/dL"
    trend = "steady"
    response = {
        "bool sugar":bloodSugar,
        "unit":unit,
        "descript":trend
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)