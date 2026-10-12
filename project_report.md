# MINI PROJECT REPORT
## Kate Patil Farm AI: Smart Agriculture & Crop Recommendation System

### 1. Abstract
This project demonstrates a beginner-friendly machine learning application for agriculture. It accepts nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall values and predicts a possible crop class using a Random Forest classifier. A Streamlit interface allows users to enter values and view the prediction and model scores. The included dataset is synthetic and intended only for educational demonstration.

### 2. Problem Statement
Choosing a crop depends on several soil and climate factors. This project explores how a supervised ML classifier can demonstrate data-based crop recommendation.

### 3. Objectives
- Build a complete introductory ML workflow.
- Process tabular data using Pandas.
- Train and test a Random Forest classifier.
- Build an interactive Streamlit interface.
- Connect CSE–AIML learning with agriculture and Kate Patil Farm branding.

### 4. Tools and Technologies
Python, Pandas, Scikit-learn, Streamlit, CSV.

### 5. Input Features and Output
Inputs: N, P, K, temperature, humidity, pH, rainfall.
Target/output: crop class predicted by the trained model.

### 6. Methodology
1. Load the CSV dataset.
2. Separate input features and target labels.
3. Split data into training and testing sets.
4. Train a Random Forest classifier.
5. Evaluate on held-out test rows.
6. Collect user inputs in Streamlit.
7. Display predicted crop, model score, and top class scores.

### 7. Algorithm
Random Forest is an ensemble classifier that builds multiple decision trees and combines their predictions. It is a reasonable baseline for structured tabular data.

### 8. Results
The application displays a crop prediction and model score. The reported test accuracy is only for the synthetic demonstration dataset. It must not be interpreted as real-world agricultural accuracy.

### 9. Limitations
- Synthetic dataset is not validated for Maharashtra or any specific farm.
- Recommendations depend on the quality and relevance of training data.
- The model does not consider all factors such as crop rotation, irrigation access, market prices, pests, seed variety, and local advisories.
- A confidence score is not a guarantee of success.

### 10. Future Scope
- Replace synthetic data with a trustworthy and locally relevant dataset.
- Add cotton leaf disease image classification.
- Integrate weather data.
- Add Marathi UI and farm expense records.
- Conduct field validation with agronomists.

### 11. Conclusion
The project demonstrates how Python, supervised machine learning, and a web interface can be combined into a small agriculture-focused application. It is suitable as an educational prototype and requires validated local data before real-world use.

### References
- Scikit-learn documentation: https://scikit-learn.org/
- Streamlit documentation: https://docs.streamlit.io/
- Pandas documentation: https://pandas.pydata.org/docs/
