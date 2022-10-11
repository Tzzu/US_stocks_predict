from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/demo.html")
def demo():
    return render_template("demo.html")

@app.route("/S&P500.html")
def SP500():
    return render_template("S&P500.html")

@app.route("/dowjones30.html")
def DJ30():
    return render_template("dowjones30.html")

@app.route("/nasdaq100.html")
def NQ100():
    return render_template("nasdaq100.html")
    
@app.route("/S&P500_plate.html")
def three():
    return render_template("S&P500_plate.html")

@app.route('/dowJones')
def pipe():
    f=open('./static/historical_DowJones.json')
    data=json.load(f)
    f.close()
    return {"res":data}

@app.route('/usa_indices')
def usaIndices():
    f=open('./static/USA_indices_history.json')
    data=json.load(f)
    f.close()
    return {"res":data}

if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=5100)