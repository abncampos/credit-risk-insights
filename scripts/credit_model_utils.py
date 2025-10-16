"""Utility functions for preprocessing and basic modelling (placeholder).

Contains functions to:
- preprocess the German Credit dataset
- split data and train baseline models
- evaluate common metrics
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

def basic_preprocess(df):
    # Example preprocessing: rename columns to snake_case placeholder
    df = df.copy()
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df

def train_baseline_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lr = LogisticRegression(max_iter=1000)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    lr.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    results = {}
    for name, model in [('logistic_regression', lr), ('random_forest', rf)]:
        preds = model.predict(X_test)
        proba = model.predict_proba(X_test)[:,1] if hasattr(model, 'predict_proba') else None
        results[name] = {
            'classification_report': classification_report(y_test, preds, output_dict=True),
            'roc_auc': roc_auc_score(y_test, proba) if proba is not None else None
        }
    return results
