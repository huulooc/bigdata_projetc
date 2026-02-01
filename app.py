import streamlit as st
import pandas as pd
import os

# ===============================
# Page config
# ===============================
st.set_page_config(
    page_title="✈️ Flight Delay Prediction",
    layout="wide"
)

st.title("✈️ Flight Delay Prediction Results")

# ===============================
# Load predicted file
# ===============================
FILE_PATH = "/content/predicted_results/part-00000-75b5e51b-bebd-47eb-9e18-312e1e961d71-c000.csv"

if not os.path.exists(FILE_PATH):
    st.error("❌ predicted_results.csv not found. Run prediction cell first.")
    st.stop()

df = pd.read_csv(FILE_PATH)

st.success("✅ Loaded prediction results")

# ===============================
# Map label
# ===============================
df["Result"] = df["prediction"].map({
    0: "Not Delay",
    1: "Delay",
    0.0: "Not Delay",
    1.0: "Delay"
})

# ===============================
# Display table
# ===============================
st.subheader("📊 Prediction Results")
st.dataframe(
    df.drop(columns=["prediction"]),
    use_container_width=True
)

# ===============================
# Charts
# ===============================
st.subheader("📈 Delay Distribution")
st.bar_chart(df["Result"].value_counts())

st.subheader("📊 Delay Probability (First 50 Flights)")
st.line_chart(df["delay_probability"].head(50))

# ===============================
# Summary
# ===============================
st.subheader("📌 Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Total Flights", len(df))

with c2:
    st.metric("Delayed Flights", int((df["Result"] == "Delay").sum()))

with c3:
    st.metric(
        "Average Delay Probability",
        f"{df['delay_probability'].mean() * 100:.2f}%"
    )
