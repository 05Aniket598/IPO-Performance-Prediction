# 📊 IPO Performance Prediction

## 🔍 Project Overview

The goal of this project is to build a data-driven system that predicts whether investing in a recently launched IPO is a good decision for retail investors. This project was inspired by real-world IPO scam cases, where companies create artificial hype to inflate valuations, often leaving uninformed investors at risk.

Through this project, I aim to help retail investors filter out potentially weak IPOs early, based on publicly available financial and subscription data, acting as a **first-level decision support system**.

---

## 🎯 Objectives

- Collect and aggregate IPO listing data from multiple years
- Gather key financial indicators, subscription figures, and company fundamentals
- Clean and structure the data into a unified format
- Explore the data through EDA and domain logic
- Develop a custom labeling strategy to flag IPOs as:
  - `Good to Go`
  - `Wait`
  - `Avoid`
- Train ML models to validate the feasibility of IPO performance prediction

---

## 🗃️ Data Sources (Scraped Using Selenium & BeautifulSoup)

Currently being scraped from [Trendlyne.com](https://trendlyne.com) and potentially other sources.

### ✅ Collected So Far

#### 📌 IPO-Level Data (SME + Mainboard)
- `Company`
- `Issue Type`
- `Listing Date`
- `Issue Size`
- `Issue Price`
- `LTP (Last Traded Price)`
- `Market Cap (in Cr)`
- `QIB/HNI/Retail Subscription`
- `Total Subscription`
- `Listing Open Price`
- `Listing Close Price`
- `Listing Gain %`
- `Current Gain %`

#### 📌 Financials (Annual Results)
- `Revenue`, `Net Profit`, `EPS`, `ROE`, `ROCE`, `Debt to Equity`, `Cash Flow`
- Financial year columns from **Mar '15** to **Mar '25**
- Indicators like `CAGR 3 Yrs`, `CAGR 5 Yrs`, `TTM`
- Includes scraped tables: Balance Sheet, Cash Flow, Financial Ratios

---

## ⚙️ Project Stage

| Component              | Status         | Notes                                                  |
|------------------------|----------------|---------------------------------------------------------|
| Data Collection        | ⏳ In Progress  | SME + Mainboard IPOs, Financials from Trendlyne        |
| Data Cleaning          | ⏳ Not Started  | Will standardize columns, handle missing values         |
| Feature Engineering    | ⏳ Not Started  | Sector mapping, promoter holding, tenure calculation    |
| Label Creation         | ⏳ Not Started  | Domain-based labeling using subscription + fundamentals |
| EDA & Visualizations   | ⏳ Planned      | Sector-wise patterns, listing gains vs subscriptions    |
| Model Training         | ⏳ Planned      | Will explore classification models                     |
| Dashboard              | ⏳ Planned      | Streamlit or Power BI dashboard later stage             |

---

## 📌 Planned Custom Columns

- `Tenure`: Number of years since IPO listing (Current Year - Listing Year)
- `Label`: Based on a mix of tenure, subscription trends, and financial health (domain rules)

---

## 🧠 Why This Project Matters

Retail investors often rely on hearsay, news channels, or influencer hype when investing in IPOs. This project aims to build a **transparent and data-backed model** that empowers better decision-making — especially in the early days post-IPO when little public research exists.

---

## 🚧 Notes

- This is a **work-in-progress** project.
- Code will be modularized and refactored once the raw data collection is complete.
- Financial metric interpretations and labeling logic will be revisited post-EDA.

---

## 🛠️ Tools & Libraries

- Python, Pandas, NumPy
- Selenium, BeautifulSoup
- Matplotlib, Seaborn (for future EDA)
- Scikit-learn / XGBoost (for modeling later)

---

## 📬 Let's Connect

Feel free to share feedback, ideas, or collaborations.  
📧 aniket.yadav52005@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/aniketyadavofficial/)

---

## 🔖 Tags  
`#IPO #Finance #MachineLearning #DataScience #RetailInvesting #Python #Trendlyne #InvestmentResearch #Selenium #GitHubProject`
