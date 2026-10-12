# Kate Patil Farm AI — Smart Agriculture & Crop Recommendation System

## Overview
Beginner-friendly CSE–AIML mini project. A Streamlit web app takes soil nutrients (N, P, K), temperature, humidity, soil pH, and rainfall, then uses a Random Forest classifier to suggest a crop.

## Important academic note
`data/demo_crop_data.csv` is a **synthetic educational dataset** generated for a working demonstration. It is not a real, locally validated crop dataset. The test accuracy shown in the app is only for this demo data and must not be presented as real farm accuracy. For field use, replace it with a reliable dataset and consult a soil test / local agricultural expert.

## Requirements
- Python 3.10 or newer recommended
- VS Code (optional but recommended)
- Internet connection for the first package installation

## Run on Windows (VS Code / Terminal)
1. Extract the ZIP folder.
2. Open the `Kate_Patil_Farm_AI_Project` folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:
   ```powershell
   py -m venv .venv
   ```
5. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt terminal and run:
   ```bat
   .venv\Scripts\activate.bat
   ```
6. Install packages:
   ```powershell
   python -m pip install -r requirements.txt
   ```
7. Start the app:
   ```powershell
   python -m streamlit run app.py
   ```
8. Browser opens with the app. If it does not, copy the local URL shown in Terminal (usually `http://localhost:8501`).

## Files
- `app.py` — web app and ML training code
- `data/demo_crop_data.csv` — synthetic demo dataset
- `requirements.txt` — Python libraries
- `presentation_outline_bilingual.md` — slide text and bilingual speaking script
- `project_report.md` — report content for college submission

## Viva talking points
- Supervised learning: learns from labeled examples.
- Features: N, P, K, temperature, humidity, pH, rainfall.
- Target: crop label.
- Random Forest: combines many decision trees and votes on the class.
- Train/test split: evaluate on held-out rows.
- Limitation: synthetic dataset means results are for demonstration only.
