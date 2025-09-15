# 📈 IPO Performance Prediction – Academic Project

**Author**: Aniket Yadav
**Domain**: Finance | Data Science | Machine Learning
**Project Type**: Academic Year Project
**Status**: 🚧 In Progress

---

## 🧠 Project Objective

Retail investors often invest in IPOs based on media hype or peer advice, without enough financial analysis — which can lead to losses, especially when IPOs are overvalued or part of manipulated market activity.

This project aims to predict whether investing in a **recently launched IPO** is a **"Good to Go", "Wait", or "Avoid"** decision — based on:

* Subscription patterns (QIB, HNI, Retail)
* Financial health of the company
* Promoter holding
* Business tenure since listing

---

## 🏗️ Project Structure

### 🔄 Phase 1: Data Collection (In Progress)

Collected data (2019–2025) from sources like [Trendlyne](https://trendlyne.com), covering:

#### ✅ IPO-Level Data (Mainboard & SME)

| Company | Issue Type | Market Cap | IPO Price | Listing Price | LTP | Gain | QIB/HNI/Retail Subscriptions | Total Subscription | Listing Date |
| ------- | ---------- | ---------- | --------- | ------------- | --- | ---- | ---------------------------- | ------------------ | ------------ |

#### ✅ Annual Financials (Mar’15–Mar’25)

| Company | Indicator | CAGR 3 Yrs | CAGR 5 Yrs | Mar '25 | Mar '24 | ... | Mar '15 |
| ------- | --------- | ---------- | ---------- | ------- | ------- | --- | ------- |

#### ✅ Financial Ratios, Balance Sheet, Cash Flow

* Will be made available as `.csv` and `.pkl` files in this repo

#### 🔄 Upcoming:

* Sector/Industry Info
* Promoter Holding

### 🧹 Phase 2: Data Cleaning

* Standardizing formats
* Handling missing values
* Creating meaningful features (e.g., market tenure)

### 🏷️ Phase 3: Data Labeling Strategy

Custom logic under development:

* If IPO is 3+ years old, use real performance (current vs. listing price)
* If <3 years old, rely more on financial metrics and subscription strength

Labels:

* `Good to Go`
* `Wait for Good Time`
* `Avoid for Now`

### 🤖 Phase 4: Modeling & Prediction

* Feature engineering (Subscription, Financials, Holding)
* Model selection: Random Forest, XGBoost, etc.
* Evaluation metrics: Accuracy, Precision, AUC-ROC

### 📊 Phase 5: Dashboard (Power BI or Streamlit)

* Interactive filter to check IPO performance prediction
* Filter by: Year, Industry, Subscription Type, Label, etc.

---

## 💡 Vision

This tool will act as a **decision-assist model** for:

* Retail investors to filter new IPOs
* Analysts to study post-listing performance
* Educators to show ML applications in finance

## 🔗 Follow Project Progress

This repository will be continuously updated.
Feel free to ⭐ star and watch the repo to stay informed.

> **📬 Feedback and suggestions are welcome!**

---

## 📌 Connect with Me

* LinkedIn : [LinkedIn](https://www.linkedin.com/in/aniketyadavofficial/)
* Email : [Gmail](aniket.yadav52005@gmail.com)

---

**#IPO #StockMarket #RetailInvesting #Finance #MachineLearning #AcademicProject #Python #WebScraping #DataScience #Trendlyne #PowerBI #AIinFinance #GitHubProject**

