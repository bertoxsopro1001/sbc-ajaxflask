from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    if request.method == "POST":
        name = request.form["name"]
        bday = request.form["bday"]  
        
        birth_date = datetime.strptime(bday, "%Y-%m-%d")

        current_year = datetime.now().year
        age = current_year - birth_date.year - ((current_year, birth_date.month, birth_date.day) < (current_year, birth_date.month, birth_date.day))

        return jsonify({"name": name, "age": age})
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
