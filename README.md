# 📊 InsightAI: Predictive Analytics & NLP Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **"Bridging the gap between raw data and actionable business intelligence."**

## 💡 Project Overview
**InsightAI** is a full-stack data science application designed to empower businesses with real-time analytics. It combines **Machine Learning** for sales forecasting with **Natural Language Processing (NLP)** to extract sentiment from unstructured customer feedback.

Unlike static reports, InsightAI offers an **interactive dashboard** where stakeholders can visualize trends, generate predictions, and understand customer sentiment at a glance.

---

## 🚀 Key Features

### 1. 📈 Intelligent Sales Forecasting
* **Algorithm:** Implements **Linear Regression** (Scikit-Learn) to model historical sales data.
* **Capability:** Predicts future revenue trends based on temporal features.
* **Metric:** Dynamic visualization of regression lines against actuals.

### 2. 🧠 NLP & Sentiment Analysis
* **Engine:** Processes unstructured text data (Customer Reviews) to gauge market sentiment.
* **Output:** Classifies feedback as **Positive**, **Neutral**, or **Negative** with polarity scoring.
* **Visualization:** Distribution charts to instantly identify customer satisfaction levels.

### 3. 📊 Interactive Data Visualization
* **Tech:** Built on **Streamlit** for rapid rendering of large datasets.
* **UX:** Seamless upload of CSV files with automatic data cleaning and type inference.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend/UI** | `Streamlit` | Interactive web-based dashboarding |
| **Data Manipulation** | `Pandas` & `NumPy` | Data cleansing, preprocessing, and vectorization |
| **Machine Learning** | `Scikit-Learn` | Predictive modeling and regression analysis |
| **NLP** | `TextBlob` / `OpenAI API` | Sentiment extraction and text processing |
| **Environment** | `Python` | Core logic and backend processing |

---

## ⚙️ Installation & Usage

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AnshikaPrasad/InsightAI-Dashboard.git](https://github.com/AnshikaPrasad/InsightAI-Dashboard.git)
   cd InsightAI-Dashboard

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Dashboard:**
   ```bash
   streamlit run app.py
