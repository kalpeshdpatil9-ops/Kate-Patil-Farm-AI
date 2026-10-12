# Kate Patil Farm AI — PPT Content + Bilingual Presentation Script
Use these 10 slides to create or explain the presentation. Keep slide bullets in English and use the Marathi script while speaking.

## Slide 1: Kate Patil Farm AI
Smart Agriculture & Crop Recommendation System
CSE–AIML Mini Project

**Speaking script (English + Marathi):**
Good morning respected teacher and my friends. My project is Kate Patil Farm AI.
मराठीत: माझ्या प्रोजेक्टचे नाव Kate Patil Farm AI आहे. हा शेतीसाठी AI/ML वापरणारा शैक्षणिक प्रोटोटाइप आहे.

## Slide 2: Introduction | परिचय
• AI helps computers learn patterns from data
• Agriculture can use data for decision support
• This prototype recommends a possible crop

**Speaking script (English + Marathi):**
AI म्हणजे डेटामधील patterns शिकून अंदाज देणारी तंत्रज्ञान पद्धत.
या प्रोजेक्टमध्ये माती आणि हवामानाच्या डेटावरून संभाव्य पीक सुचवले जाते.

## Slide 3: Problem Statement | समस्या
• Crop choice depends on soil and climate
• Decisions based only on guesswork may be risky
• Need a simple data-driven learning tool

**Speaking script (English + Marathi):**
योग्य पीक निवडताना माती, पाऊस आणि हवामान महत्त्वाचे असतात.
हा प्रोजेक्ट निर्णय घेण्यास मदत करणारे शैक्षणिक tool आहे; तो हमखास यशाची खात्री देत नाही.

## Slide 4: Objectives | उद्दिष्टे
• Build a simple ML crop classifier
• Accept seven input features
• Show prediction and model score in a web app
• Use Kate Patil Farm branding

**Speaking script (English + Marathi):**
सात inputs घेऊन Random Forest model ने पीक predict करणे आणि Streamlit वर result दाखवणे हे मुख्य उद्दिष्ट आहे.

## Slide 5: Proposed System | प्रस्तावित प्रणाली
User inputs → DataFrame → Random Forest → Crop prediction
Inputs: N, P, K, temperature, humidity, pH, rainfall

**Speaking script (English + Marathi):**
वापरकर्ता values भरतो. त्या model ला दिल्या जातात आणि model त्याच्या training मधील patterns नुसार crop class सांगतो.

## Slide 6: Technology Stack | तंत्रज्ञान
• Python — programming
• Pandas — data handling
• Scikit-learn — ML model
• Streamlit — web interface

**Speaking script (English + Marathi):**
Python मध्ये logic, Pandas मध्ये dataset handling, Scikit-learn मध्ये model आणि Streamlit मध्ये user interface तयार केला आहे.

## Slide 7: Machine Learning | अल्गोरिदम
• Supervised classification
• Random Forest combines multiple decision trees
• Train/test split checks performance on held-out data

**Speaking script (English + Marathi):**
Dataset मध्ये input features आणि crop label असतो. Random Forest अनेक decision trees वापरतो आणि त्यांच्या voting वर prediction देतो.

## Slide 8: Implementation & Demo | अंमलबजावणी
• Load CSV dataset
• Train model
• Enter soil/weather values
• Display predicted crop and top scores

**Speaking script (English + Marathi):**
Live demo मध्ये मी inputs बदलेन आणि system कसा result देतो ते दाखवेन. Dataset demo साठी synthetic आहे हे लक्षात घ्यावे.

## Slide 9: Results, Limits & Future Scope | निकाल
• Test score applies only to synthetic demo data
• Not validated for real farms
• Future: trusted local data, cotton disease detection, weather integration

**Speaking script (English + Marathi):**
या version चा dataset शिकण्यासाठी तयार केलेला आहे. भविष्यात खरी स्थानिक माहिती, cotton disease detection आणि weather API जोडता येईल.

## Slide 10: Conclusion | निष्कर्ष
• Demonstrates a complete beginner ML workflow
• Connects AI/ML with agriculture
• Thank you

**Speaking script (English + Marathi):**
या प्रोजेक्टमधून dataset, model training आणि web app यांचा एकत्रित वापर समजतो. धन्यवाद. प्रश्न विचारू शकता.

## Common Viva Questions / सामान्य Viva प्रश्न
1. **What is AI?** AI is a field that builds systems able to perform tasks requiring intelligence. / AI म्हणजे बुद्धिमत्तेसारखी कामे करणारी प्रणाली तयार करण्याचे क्षेत्र.
2. **What is Machine Learning?** A method where a model learns patterns from examples. / उदाहरणांमधून patterns शिकण्याची पद्धत.
3. **What is supervised learning?** Learning from labeled examples. / label असलेल्या डेटावरून शिकणे.
4. **Why Random Forest?** It combines many decision trees and is a useful baseline for tabular classification.
5. **What are features and target?** Features are N, P, K, temperature, humidity, pH, rainfall; target is crop label.
6. **What is train-test split?** Some data trains the model and held-out data checks its performance.
7. **What does accuracy mean?** Correct predictions divided by all test predictions. Here it only reflects synthetic demo data.
8. **Can farmers rely on this output directly?** No. It is a prototype; use validated local data, soil testing, and agricultural expert advice.
9. **What is Streamlit?** A Python framework for quickly building interactive data apps.
10. **Future improvements?** Trusted Maharashtra-specific data, disease detection, weather API, Marathi UI, and farm record dashboard.