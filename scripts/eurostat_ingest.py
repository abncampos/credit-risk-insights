"""Eurostat ingest helper

This script downloads Eurostat CSV if a direct URL is provided or loads a local CSV file.
It is intentionally conservative: Eurostat bulk downloads may require specific endpoints.
Use the notebook for full ingestion steps.
"""
import os
import pandas as pd
import requests

def load_local_csv(path):
    return pd.read_csv(path)

def download_csv(url, save_path):
    r = requests.get(url)
    r.raise_for_status()
    with open(save_path, 'wb') as f:
        f.write(r.content)
    return pd.read_csv(save_path)

if __name__ == '__main__':
    print('This script is a helper. Prefer using the notebook 01_data_ingestion_cleaning.ipynb for interactive ingestion.')