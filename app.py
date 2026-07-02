from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load("placement_model.pkl")
encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        age = int(request.form["age"])

        gender = encoders["Gender"].transform([request.form["gender"]])[0]
        degree = encoders["Degree"].transform([request.form["degree"]])[0]
        branch = encoders["Branch"].transform([request.form["branch"]])[0]

        cgpa = float(request.form["cgpa"])
        internships = int(request.form["internships"])
        projects = int(request.form["projects"])
        coding = int(request.form["coding"])
        communication = int(request.form["communication"])
        aptitude = int(request.form["aptitude"])
        softskills = int(request.form["softskills"])
        certifications = int(request.form["certifications"])
        backlogs = int(request.form["backlogs"])

        # Create dataframe
        input_data = pd.DataFrame([{
            "Age": age,
            "Gender": gender,
            "Degree": degree,
            "Branch": branch,
            "CGPA": cgpa,
            "Internships": internships,
            "Projects": projects,
            "Coding_Skills": coding,
            "Communication_Skills": communication,
            "Aptitude_Test_Score": aptitude,
            "Soft_Skills_Rating": softskills,
            "Certifications": certifications,
            "Backlogs": backlogs
        }])

        # Predict
        prediction = model.predict(input_data)[0]

        result = target_encoder.inverse_transform([prediction])[0]

        return render_template(
            "index.html",
            prediction_text=f"Prediction Result: {result}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)