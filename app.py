from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    news = request.form["news"]
    transformed = vectorizer.transform([news])

    prediction = model.predict(transformed)
    probability = model.predict_proba(transformed)
    confidence = round(max(probability[0]) * 100, 2)

    if prediction[0] == "REAL":
        result = "✅ REAL NEWS"
        color = "green"
    else:
        result = "❌ FAKE NEWS"
        color = "red"

    return render_template(
        "index.html",
        prediction_text=result,
        confidence=confidence,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)