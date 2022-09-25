from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/S&P500")
def two():
    return render_template("S&P500.html")
    
@app.route("/S&P500_plate")
def three():
    return render_template("S&P500_plate.html")

if __name__=="__main__":
    app.run(debug=True)