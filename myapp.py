from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    if request.method == "POST":
        name = request.form["name"]
        bday = int(request.form["bday"])  
        current_year = datetime.now().year
        age = current_year - bday  

        return jsonify({"name": name, "age": age})
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
