import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Kate Patil Farm AI", page_icon="🌱", layout="centered")
st.title("🌱 Kate Patil Farm AI")
st.subheader("Smart Agriculture & Crop Recommendation System")
st.write("Enter soil and weather values to see a demonstration crop recommendation.")

DATA_PATH = Path(__file__).parent / "data" / "demo_crop_data.csv"
df = pd.read_csv(DATA_PATH)
features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
X, y = df[features], df["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)
test_accuracy = accuracy_score(y_test, model.predict(X_test))

with st.sidebar:
    st.header("About this project")
    st.write("Student mini project • CSE–AIML")
    st.write("Model: Random Forest Classifier")
    st.metric("Demo test accuracy", f"{test_accuracy:.1%}")
    st.caption("This score applies only to the included synthetic demo dataset, not real farms.")

st.info("Educational prototype. Use a soil test and local agricultural advice before making real crop decisions.")
with st.form("crop_form"):
    c1, c2 = st.columns(2)
    with c1:
        N = st.number_input("Nitrogen (N)", min_value=0, max_value=500, value=80)
        P = st.number_input("Phosphorus (P)", min_value=0, max_value=500, value=45)
        K = st.number_input("Potassium (K)", min_value=0, max_value=500, value=45)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=55.0, value=27.0, step=0.5)
    with c2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)
        ph = st.number_input("Soil pH", min_value=3.0, max_value=10.0, value=7.0, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=4000.0, value=850.0, step=25.0)
    submitted = st.form_submit_button("Recommend a Crop 🌾")

if submitted:
    values = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], columns=features)
    pred = model.predict(values)[0]
    probs = model.predict_proba(values)[0]
    confidence = float(probs.max())
    st.success(f"Suggested crop (demo): **{pred.replace('_', ' ').title()}**")
    st.write(f"Model confidence score: **{confidence:.1%}**")
    st.caption("Confidence is not a guarantee of success. It reflects the model's scores on its demo classes.")
    top = sorted(zip(model.classes_, probs), key=lambda z: z[1], reverse=True)[:5]
    st.write("Top model predictions:")
    st.bar_chart(pd.DataFrame({"Crop": [x[0].replace('_',' ').title() for x in top],
                               "Score": [float(x[1]) for x in top]}).set_index("Crop"))
    st.write("Input summary")
    st.dataframe(values, use_container_width=True)

with st.expander("Dataset & limitations"):
    st.write(f"Rows: {len(df)} • Crop classes: {df['label'].nunique()}")
    st.write("The included dataset is synthetically generated for learning and UI demonstration. It is not a validated agricultural dataset. Replace it with a trusted, locally relevant dataset before claiming real-world accuracy.")
    st.dataframe(df.head(10), use_container_width=True)
    