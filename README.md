# 📦 Vendor Invoice Intelligence Portal

A Machine Learning-powered procurement analytics platform that predicts freight costs and identifies high-risk invoices to support smarter purchasing decisions and improve operational efficiency.

<p align="center">

  🚀 **[Live Application – Launch Streamlit App](https://vendorinvoicesystem.streamlit.app/)**

</p>

---

## 📌 Overview

Procurement teams often handle large volumes of vendor invoices and transportation costs, making it difficult to identify unusual expenses and potential invoice risks manually.

The **Vendor Invoice Intelligence Portal** leverages Machine Learning techniques to automate procurement analytics through:

- Freight Cost Prediction
- Invoice Risk Flagging
- Feature Engineering
- Interactive Business Intelligence Dashboard

The system enables procurement teams to make data-driven decisions, improve cost visibility, and proactively identify potentially risky transactions.

---

## 🚀 Key Features

### 1. Freight Cost Prediction

Predicts expected freight costs using historical procurement and transportation data.

- Estimates transportation expenses.
- Analyzes historical procurement patterns.
- Uses trained regression models for cost prediction.

### 2. Invoice Risk Flagging

Identifies potentially risky invoices based on procurement patterns and transactional indicators.

- Detects potentially suspicious invoices.
- Classifies invoice risk levels.
- Helps prioritize invoice verification.

### 3. Feature Engineering Pipeline

Transforms raw procurement data into business-relevant predictive features.

- Vendor performance indicators.
- Delivery delay metrics.
- Purchase aggregation features.
- Invoice characteristics.
- Cost-related variables.

### 4. Real-Time Predictions

Allows users to generate predictions through an interactive Streamlit application.

### 5. Business Decision Support

Provides actionable insights for procurement optimization and invoice review processes.

---

## 🧠 Machine Learning Approach

The project implements two major Machine Learning modules.

### Regression Module – Freight Cost Prediction

Used for estimating transportation and freight expenses.

**Models Evaluated:**

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

**Optimization Techniques:**

- GridSearchCV
- Cross Validation
- Model Performance Comparison

### Classification Module – Invoice Risk Detection

Used for identifying potentially risky invoices.

**Model Used:**

- Decision Tree Classifier

**Evaluation Techniques:**

- Accuracy Score
- Weighted F1 Score
- Classification Report
- Confusion Matrix

---

## 📊 Data Processing Pipeline

The project follows a structured Machine Learning workflow:

1. Procurement Data Collection
2. Data Cleaning
3. Missing Value Treatment
4. Feature Engineering
5. Categorical Encoding
6. Model Training
7. Model Evaluation
8. Risk Classification
9. Freight Cost Prediction
10. Streamlit Deployment

---

## 🔧 Feature Engineering

The system derives business-focused features from procurement and invoice records, including:

- Vendor Performance Indicators
- Delivery Delay Metrics
- Purchase Aggregation Features
- Invoice Characteristics
- Cost-Related Variables
- Procurement Activity Patterns

These engineered features improve predictive accuracy and business relevance.

---

## 📈 Model Performance

### Freight Cost Prediction

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.97 |
| Mean Absolute Error (MAE) | 24.46 |

### Invoice Risk Flagging

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 82% |
| Weighted F1 Score | 0.82 |

The models demonstrated strong predictive capability and reliable performance on unseen data.

*Note: Performance values represent the reported evaluation results of the trained models.*

---

## 📊 Business Impact

The platform helps procurement teams:

- Estimate transportation expenses more accurately.
- Detect potentially risky invoices before approval.
- Reduce manual review effort.
- Improve procurement transparency.
- Support data-driven purchasing decisions.
- Improve visibility into procurement operations.

---

## 💻 Technology Stack

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib

### Deployment
- Streamlit

### Machine Learning Algorithms
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Decision Tree Classification

---

## 🖥️ Application Workflow

### Freight Cost Prediction

1. User enters procurement information.
2. Data is preprocessed and transformed.
3. Regression model estimates freight cost.
4. Predicted cost is displayed through the application.

### Invoice Risk Flagging

1. User enters invoice details.
2. Features are generated and processed.
3. Classification model evaluates invoice risk.
4. Risk prediction is displayed instantly.

---

## 📂 Project Structure

```text
Vendor-Invoice-Intelligence-Portal/
│
├── Freight Cost Prediction/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   └── models/
│       └── predict_freight_model.pkl
│
├── Inventory/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   └── vendor_invoice.csv
│
├── Invoice Flagging/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   └── train.py
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── models/
│   ├── predict_flag_invoice.pkl
│   └── predict_freight_model.pkl
│
├── notebooks/
│   ├── Freight Cost notebook.ipynb
│   └── Invoice Flagging notebook.ipynb
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── app.py
```

---

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/aditya-madhu/Vendor-Invoice-Intelligence-Portal.git
```

### 2. Navigate to the Project Directory

```bash
cd Vendor-Invoice-Intelligence-Portal
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

---

## 🌐 Live Demo

🚀 **Try the application online:**

Experience freight cost prediction and invoice risk flagging through the deployed Streamlit application.

### 👉 [Launch Vendor Invoice Intelligence Portal](https://vendorinvoicesystem.streamlit.app/)

---

## 🌟 Future Enhancements

- Advanced Ensemble Models
- Explainable AI (XAI) Integration
- Vendor Performance Dashboard
- Automated Procurement Risk Scoring
- Cloud Deployment
- Real-Time Data Integration
- Advanced Anomaly Detection
- Automated Invoice Verification

---

## ⭐ Support

If you find this project interesting or useful, consider giving the repository a ⭐ on GitHub.

Your support and feedback are appreciated!

---

**Built with Python, Machine Learning, and Streamlit.**
