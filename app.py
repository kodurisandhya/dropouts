from flask import Flask, render_template, request

app = Flask(__name__)

def predict_dropout(attendance, grades, participation, financial_issue, family_support, health_issue):
    score = 0
    
    if attendance < 75:
        score += 1
    if grades < 50:
        score += 1
    if participation < 5:
        score += 1
    if financial_issue == "Yes":
        score += 1
    if family_support == "Poor":
        score += 1
    if health_issue == "Yes":
        score += 1

    if score >= 4:
        return "High Risk", ["Immediate counseling required", "Check financial aid", "Provide health support"]
    elif score >= 2:
        return "Moderate Risk", ["Monitor closely", "Offer academic help"]
    else:
        return "Low Risk", ["Encourage continued performance"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        attendance = float(request.form["attendance"])
        grades = float(request.form["grades"])
        participation = int(request.form["participation"])
        financial_issue = request.form["financial_issue"]
        family_support = request.form["family_support"]
        health_issue = request.form["health_issue"]

        risk, suggestions = predict_dropout(attendance, grades, participation, financial_issue, family_support, health_issue)
        return render_template("index.html", risk=risk, suggestions=suggestions)

    return render_template("index.html", risk=None, suggestions=None)

if __name__ == "__main__":
    app.run(debug=True)
