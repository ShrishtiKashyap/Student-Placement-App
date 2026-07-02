# 🎓 Student Placement Prediction System

<div align="center">

### Predict Campus Placement Using Machine Learning

A modern Machine Learning web application built with **Python**, **Flask**, and **Random Forest** to predict whether a student is likely to be placed based on academic and personal performance.

---

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

# 📖 Overview

This project is a Machine Learning based web application that predicts whether a student is likely to be placed during campus recruitment.

The application accepts student information through an interactive web interface, preprocesses the input using trained encoders, and performs prediction using a Random Forest Classifier.

The goal of this project is to demonstrate an end-to-end Machine Learning workflow including:

- Data preprocessing
- Feature encoding
- Model training
- Model serialization
- Flask integration
- Interactive web interface

---

# ✨ Features

- 🎯 Placement Prediction
- 🧠 Random Forest Classification
- 📊 Trained on Student Placement Dataset
- 💻 Responsive User Interface
- ⚡ Fast Prediction
- 🔥 Flask Backend
- 📁 Modular Project Structure
- 🏷 Encoded Categorical Features
- 📦 Ready for Deployment

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Backend Framework |
| HTML5 | Structure |
| CSS3 | Styling |
| Scikit-Learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Pickle | Model Serialization |

---

# 📂 Project Structure

```text
Student-Placement-App/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── placement_model.pkl
├── encoders.pkl
├── target_encoder.pkl
├── train.csv
├── test.csv
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 🤖 Machine Learning Workflow

```
Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Encoding
     │
     ▼
Train-Test Split
     │
     ▼
Random Forest Classifier
     │
     ▼
Model Evaluation
     │
     ▼
Model Saved (.pkl)
     │
     ▼
Flask Web Application
```

---

# 📊 Input Features

The application predicts placement using student information such as:

- Gender
- Degree
- Branch
- CGPA
- Academic Performance
- Technical Skills
- Other relevant student attributes

---

# 🎯 Prediction Output

The model predicts one of the following:

✅ **Placed**

or

❌ **Not Placed**

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ShrishtiKashyap/Student-Placement-App.git
```

Move into the project folder

```bash
cd Student-Placement-App
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Train the Model

```bash
python train_model.py
```

This generates:

- placement_model.pkl
- encoders.pkl
- target_encoder.pkl

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 📸 Application Preview

> *(Add screenshots here after deployment)*

### Home Page

```
Insert Screenshot
```

### Prediction Result

```
Insert Screenshot
```

---

# 💡 Future Improvements

- Docker Deployment
- Cloud Deployment
- Prediction Probability Score
- Feature Importance Visualization
- Dark / Light Theme
- User Authentication
- Prediction History
- Analytics Dashboard

---

# 👩‍💻 Author

**Shrishti Kashyap**

B.Tech Computer Science Engineering

VIT Bhopal University

GitHub:
https://github.com/ShrishtiKashyap

LinkedIn:
https://www.linkedin.com/in/shrishti-kashyap-41778431b

---

# ⭐ If you found this project useful, consider giving it a star!
