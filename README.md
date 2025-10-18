# 📊 Credit Risk Insights — Data-Driven Financial Analysis

Exploring Financial Data and Predicting Credit Risk  

![GitHub last commit](https://img.shields.io/github/last-commit/abncampos/credit-risk-insights?color=blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Platform](https://img.shields.io/badge/Platform-Colab%20%7C%20Kaggle%20%7C%20Local-green)

---

## 📚 Table of Contents
- [Overview](#overview)
- [Objectives](#objectives)
- [Key Skills Demonstrated](#key-skills-demonstrated)
- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Results & Insights](#results--insights)
- [Test & Environment Setup](#test--environment-setup)
- [Conclusion](#conclusion)
- [Recommended Reading & References](#recommended-reading--references)
- [License](#license)

---

## 🧠 Overview
**Credit Risk Insights** is an end-to-end data analytics project focused on understanding credit behavior and financial stability using open European datasets.

It combines data cleaning, exploratory analysis, and predictive modeling to evaluate credit risk, drawing on methods commonly used in financial analytics and risk management.

---

## 🎯 Objectives
- Explore relationships between borrower characteristics and default likelihood.  
- Build and evaluate a predictive model for credit risk classification.  
- Communicate insights that support strategic financial decisions.  
- Practice technical and analytical storytelling with financial context.

---

## 🧩 Key Skills Demonstrated
- Data cleaning, transformation, and validation.  
- Exploratory data analysis (EDA) and statistical interpretation.  
- Predictive modeling (Logistic Regression, Random Forest).  
- Feature importance analysis and model evaluation (AUC, recall, precision).  
- Financial storytelling and visualization using Python.  

---

## 🗂️ Project Structure
credit-risk-insights/
├─ notebooks/
│ ├─ 01_data_ingestion_cleaning.ipynb
│ ├─ 02_exploratory_analysis.ipynb
│ └─ 03_credit_risk_model.ipynb
├─ scripts/
│ ├─ eurostat_ingest.py
│ └─ credit_model_utils.py
├─ data/
│ └─ raw/ (reference only)
├─ requirements.txt
├─ .gitignore
└─ README.md

---

## 🗃️ Data Sources
- [UCI German Credit Data](https://archive.ics.uci.edu/ml/datasets/statlog+%28german+credit+data%29)  
- [Eurostat Financial Indicators](https://ec.europa.eu/eurostat)  
- [European Central Bank – Credit and Lending Statistics](https://sdw.ecb.europa.eu)  

All sources are publicly available and verified.

---

## ⚙️ Methodology
1. **Data Preparation:** Cleaning and formatting raw data, ensuring quality and interpretability.  
2. **Exploratory Analysis:** Identifying key variables that influence credit risk.  
3. **Feature Engineering:** Encoding categorical features, scaling numeric ones.  
4. **Modeling:** Training classification models to predict credit risk.  
5. **Evaluation:** Comparing model accuracy, recall, precision, and AUC.  
6. **Interpretation:** Connecting model results to real financial behavior and risk profiles.

---

## 📈 Results & Insights
- Borrowers with shorter employment duration and higher credit utilization rates showed greater default risk.  
- Loan purpose and credit history were significant predictors of repayment probability.  
- Logistic Regression provided strong interpretability with an **AUC of 0.87**, while Random Forest achieved slightly higher recall on default cases.  
- Combining behavioral and financial indicators improved model performance and reliability.  
- Macro-level trends aligned with Eurostat and ECB data on lending risk during rate fluctuations.

---

## 🧪 Test & Environment Setup
You can run the notebooks locally or in Google Colab.

### 🔹 Open in Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abncampos/credit-risk-insights/blob/main/notebooks/03_credit_risk_model.ipynb)

---

# 💳 Credit Risk Insights

Comprehensive data analysis and risk assessment project focusing on understanding and modeling credit risk behaviors using open financial datasets.

---

## 📊 Data Sources

The analysis is based on publicly available datasets related to credit scoring, customer demographics, and loan repayment performance.  
Data were cleaned, merged, and enriched to ensure reliability and consistency for modeling.

---

## 🧠 Methodology

The workflow followed a structured data analytics process, including:

1. **Data Understanding:**  
   Exploratory analysis to detect trends, patterns, and inconsistencies.  

2. **Data Preparation:**  
   Cleaning missing values, normalizing formats, and creating new relevant features.  

3. **Modeling:**  
   Building and evaluating classification models to predict credit risk levels.  

4. **Evaluation & Insights:**  
   Comparing models using performance metrics and extracting key business insights.  

---

## 🧭 Local Setup

1. **Clone the Repository:**  
   Clone this project from GitHub and navigate into the folder.
   ```bash
   git clone https://github.com/abncampos/credit-risk-insights.git
   cd credit-risk-insights

2. **Create a Virtual Environment:**
   Set up a Python virtual environment for package management.  
   python -m venv .venv
   source .venv/bin/activate   # or .venv\Scripts\activate on Windows

3. **Install Dependencies:**
  Install all required packages. 
  pip install -r requirements.txt

4. **Verify Environment and Notebook Execution:**
  Run automated tests or manually verify notebooks in Jupyter. 
  pytest --disable-warnings || echo "Manual check: open notebooks in Jupyter"

---

## ✅ Conclusion

This project strengthened my ability to apply data analytics in a financial context — from understanding raw data to building predictive models for credit risk analysis.

It also deepened my understanding of how data supports responsible financial decision-making and reinforced good practices in analytics-driven risk management.

---

## 📚 Recommended Reading & References

- McKinsey & Co. – AI in Risk and Compliance (2023)
- European Central Bank – Statistical Data Warehouse
- Kaggle – German Credit Risk Notebooks and Discussions
- Google Data Analytics Certificate – Capstone Methodology

---

## 🪪 License

This project is released under the MIT License

💡 Developed and documented independently by Ana Campos as part of a professional data analytics portfolio.
