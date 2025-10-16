# Credit Risk Insights: A Data-Driven Analysis of European Lending Trends

## 📊 Project Overview
This project demonstrates an **end-to-end data analysis workflow** applied to **credit risk and financial stability** across European markets. This analysis was designed and coded independently by me, reflecting my own reasoning and portfolio work.
It combines **macroeconomic indicators** from **Eurostat** and the **European Central Bank (ECB)** with an individual-level dataset (German Credit Data) to simulate a realistic analytical environment for evaluating credit default behavior.

The goal is to showcase a **data-driven approach to understanding and managing credit risk**, integrating statistical analysis, data visualization, and predictive modeling techniques aligned with financial industry standards.

---

## 🎯 Objectives
- Analyze **credit risk dynamics** using open and verifiable European financial data.  
- Build a transparent and reproducible **data pipeline** for risk assessment.  
- Develop a **baseline predictive model** for credit default classification.  
- Visualize **key credit and lending indicators** by country and time.  
- Communicate analytical insights that support strategic decisions in risk and finance.

---

## 🧠 Key Skills Demonstrated
- Data extraction, cleaning, and transformation using `pandas` and `numpy`.  
- Exploratory Data Analysis (EDA) with `matplotlib`, `seaborn`, and `plotly`.  
- Predictive modeling for credit default risk using `scikit-learn`.  
- Financial storytelling and presentation of insights through dashboards and reports.  
- Reproducible analytics workflow with clear structure and documentation.

---

## 🗂️ Project Structure
```
credit-risk-insights/
│
├── data/
│   ├── raw/                # Original datasets (Eurostat & German Credit CSV)
│   └── processed/          # Cleaned and transformed datasets
│
├── notebooks/
│   ├── 01_data_ingestion_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_credit_risk_model.ipynb
│
├── reports/
│   ├── visuals/            # Exported charts and figures
│   └── insights_summary.pdf
│
├── scripts/
│   ├── eurostat_ingest.py
│   ├── credit_model_utils.py
│
├── requirements.txt
└── README.md
```

---

## 🧾 Data Sources (verified)

### 1. **Eurostat – Non-Performing Loans (NPL) and related statistics**
- **Main page (NPL statistics explanation):**
  https://ec.europa.eu/eurostat/web/financial-corporations/non-performing-loans
- **Relevant dataset examples and endpoints:**
  - Gross non-performing loans: https://ec.europa.eu/eurostat/databrowser/view/TIPSBD10/default/table?lang=en
  - Contingent liabilities and NPLs (overview): https://ec.europa.eu/eurostat/web/products-eurostat-news/-/ddn-20250131-1

**Usage:** Provides macro-level credit risk context (NPL ratios, time series by country) for trend analysis and feature creation.

### 2. **Kaggle / UCI – German Credit Data**
- **Kaggle (example dataset):** https://www.kaggle.com/datasets/uciml/german-credit
- **UCI (original Statlog/German Credit):** https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)

**Usage:** Micro-level, anonymized records used to build and evaluate a baseline credit default prediction model. The notebook expects the CSV to be placed at `data/raw/german_credit.csv` (download from Kaggle or UCI).

---

## ⚙️ Methodology (concise)

1. **Data Ingestion:** Load Eurostat macro indicators and the German Credit CSV.  
2. **Data Cleaning:** Normalize column names, handle missing values, encode categorical variables, and create derived features.  
3. **Exploratory Data Analysis (EDA):** Visualize distributions, correlations, and country-level NPL trends.  
4. **Modeling:** Train baseline classifiers (Logistic Regression, Random Forest) and evaluate with metrics such as accuracy, recall, precision, and ROC-AUC.  
5. **Reporting:** Produce clear visuals and an executive summary describing business implications and model limitations.

---

## 📈 Analytical Framework
The repository follows **CRISP-DM** and standard risk-analytics best practices: business understanding, data understanding, preparation, modeling, evaluation, and communication.

---

## 🧾 Recommended Reading & References (corrected)
- Lando, D. (2004). *Credit Risk Modeling: Theory and Applications*. Princeton University Press.  
- Bluhm, C., Overbeck, L., & Wagner, C. (2016). *Introduction to Credit Risk Modeling* (2nd ed.). Chapman & Hall/CRC.  
- Eurostat – Non-performing loans statistics and related releases.  
- ECB – AnaCredit (documentation and methodology).  
- UCI Machine Learning Repository – Statlog (German Credit Data).

---

## ✅ License
This project is released under the **MIT License** for educational and portfolio purposes.  
All external data sources are publicly accessible and properly cited.

---

## Author
**Ana Campos** – Data Analyst | Finance & Risk Analytics
