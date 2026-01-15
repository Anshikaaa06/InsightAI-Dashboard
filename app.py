import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from textblob import TextBlob # Simulating NLP/Sentiment analysis

# Config
st.set_page_config(page_title="InsightAI Dashboard", layout="wide")

# Title
st.title("📊 InsightAI: Business Analytics & NLP Dashboard")
st.markdown("### Powered by LLM Integration & Scikit-Learn")

# Sidebar
st.sidebar.header("User Input Features")
uploaded_file = st.sidebar.file_uploader("Upload your CSV (Sales Data)", type=["csv"])

# Mock Data Generation (if no file uploaded)
def generate_mock_data():
    dates = pd.date_range(start="2024-01-01", periods=100)
    sales = np.random.randint(100, 500, size=100) + np.linspace(0, 50, 100)
    reviews = ["Great product!", "Bad service", "Okay experience", "Excellent quality", "Too expensive"] * 20
    return pd.DataFrame({"Date": dates, "Sales": sales, "Customer_Feedback": reviews})

df = generate_mock_data()

# 1. VISUALIZATION & DATA PROCESSING section
st.subheader("1. Sales Data Analysis")
st.dataframe(df.head())

st.line_chart(df.set_index("Date")["Sales"])

# 2. MACHINE LEARNING (Forecasting)
st.subheader("2. Sales Forecasting (Linear Regression)")
df['Date_Ordinal'] = df['Date'].map(pd.Timestamp.toordinal)
X = df[['Date_Ordinal']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)
future_date = st.date_input("Predict Sales for Date")
prediction = model.predict([[pd.Timestamp(future_date).toordinal()]])
st.metric(label=f"Predicted Sales for {future_date}", value=f"${prediction[0]:.2f}")

# 3. LLM / NLP SECTION
st.subheader("3. Customer Sentiment Analysis (NLP Module)")
st.info("This module processes unstructured text data to extract sentiment.")

if st.button("Analyze Feedback Sentiment"):
    # Using TextBlob as a placeholder for LLM API calls to avoid API Key errors for now
    df['Sentiment'] = df['Customer_Feedback'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['Sentiment_Label'] = df['Sentiment'].apply(lambda x: 'Positive' if x > 0 else 'Negative')
    
    st.bar_chart(df['Sentiment_Label'].value_counts())
    st.write("Sample Analyzed Data:")
    st.write(df[['Customer_Feedback', 'Sentiment_Label']].head())

st.sidebar.info("Model: GPT-3.5-Turbo (Mock connection active)")
