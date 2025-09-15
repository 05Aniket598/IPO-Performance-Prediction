import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import datetime as dt
import altair as alt
home,about = st.tabs(["Home","About"])


model = pickle.load(open("xgb_c.pkl","rb"))

with home:
    st.title("IPO Performance prediction")

    df = pd.read_csv(r"C:\Users\Aniket\OneDrive\Desktop\Personal\Projects\IPO-Performance-Prediction\Notebooks\Data\All_IPO.csv")
    # ipo_validation = pd.read_csv("Validate_IPO.csv")

    # df = pd.concat([ipo,ipo_validation],axis=0)

    company = df['company'].values

    st.text("Enter an IPO name and get performance predictions instantly using machine learning algorithms")

    selected_company = st.selectbox(
        "Select Company.",
        company,
        placeholder="Prince Pipes",
    )
    # selected_company = st.text_input("Enter Company",placeholder="Enter Company name.")

    selected_company_info = df[df["company"] == selected_company]

    info_to_show = ['ltp', 'market cap(in cr)', 'listing open', 'listing close',
    'issue type', 'listing date', 'issue size (in Cr)',
    'issue price (in rupee)', 'listing gain %',
    'current gain %', 'sector', 'industry',
    'minimum_investment_rupee', 'subscription_status']

    features_to_pass_for_prediction = ['market cap(in cr)',
                                        'issue size (in Cr)',
                                        'hni subscription',
                                        'retail subscription',
                                        'total subscription',
                                        'listing gain %',
                                        'change_in_cffoa',
                                        'change_in_ebitda',
                                        'change_in_net_profit',
                                        'change_in_roce_percent',
                                        'change_in_roe_percent',
                                        'change_in_debt_to_equity_ratio']
    
    df_for_prediction = df[df['company'] == selected_company][features_to_pass_for_prediction]


    company_info = {
        'LTP':selected_company_info['ltp'].values[0],
        'Market Cap':selected_company_info['market cap(in cr)'].values[0],
        'Issue size':selected_company_info['issue size (in Cr)'].values[0],
        'Listing date':selected_company_info['listing date'].values[0],
        'Listing open':selected_company_info['listing open'].values[0],
    }

    if st.button("Get prediction"):

        

        # Model prediction
        prediction = model.predict(df_for_prediction)[0]
        y_pred_proba = model.predict_proba(df_for_prediction)[0]

        # Class mapping
        class_labels = {0: "Bad (<5% CAGR)", 1: "Neutral (5-15% CAGR)", 2: "Good (>15% CAGR)"}

        # Create tabs after clicking button
        tab1, tab2, tab3 = st.tabs(["Prediction", "Analytical", "Company Info"])

        # ---------------- PREDICTION TAB ----------------
        with tab1:
            st.subheader("Prediction Result")
            st.write(f"### Company: {selected_company}")
            st.write(f"**Prediction:** {class_labels[prediction]}")

            # Probability bar chart
            fig, ax = plt.subplots()
            ax.bar(class_labels.values(), y_pred_proba, color=["red", "orange", "green"])
            ax.set_ylabel("Probability")
            ax.set_title("Prediction Confidence")
            st.pyplot(fig)

        # ---------------- ANALYTICAL TAB ----------------
        with tab2:
            st.subheader("Analytical Insights")

            # Subscription comparison
            subs_cols = ["qib subscription", "hni subscription", "retail subscription", "total subscription"]
            subs_data = selected_company_info[subs_cols].T
            subs_data.columns = ["Value"]

            st.write("### Subscription Breakdown")
            st.bar_chart(subs_data)

            # Financial changes
            fin_cols = [
                'change_in_cffoa', 'change_in_ebitda', 'change_in_eps', 'change_in_net_profit',
                'change_in_npm_percent', 'change_in_roce_percent',
                'change_in_roe_percent', 'change_in_debt_to_equity_ratio'
            ]
            fin_data = selected_company_info[fin_cols].T
            fin_data.columns = ["Change"]

            st.write("### Financial Metric Changes")
            st.bar_chart(fin_data)

            # CAGR vs Listing Gain
            st.write("### CAGR vs Listing Gain %")

            # Calculate CAGR dynamically
            try:
                listing_date = pd.to_datetime(selected_company_info['listing date'].values[0])
                today = dt.datetime.today()
                years = (today - listing_date).days / 365.25
            except Exception:
                years = None

            cagr_value = None
            if (
                'issue price (in rupee)' in selected_company_info.columns
                and 'ltp' in selected_company_info.columns
                and years
                and years > 0
            ):
                issue_price = float(selected_company_info['issue price (in rupee)'].values[0])
                ltp = float(selected_company_info['ltp'].values[0])

                if issue_price > 0:
                    cagr_value = ((ltp / issue_price) ** (1 / years) - 1) * 100
                    st.write(f"**CAGR (calculated): {cagr_value:.2f}%**")
                else:
                    st.write("CAGR: Cannot be calculated (invalid issue price)")
            else:
                st.write("CAGR: Not Available")

            # Listing Gain %
            listing_gain_value = None
            if "listing gain %" in selected_company_info.columns:
                listing_gain_value = float(selected_company_info['listing gain %'].values[0])
                st.write(f"**Listing Gain %: {listing_gain_value:.2f}%**")
            else:
                st.write("Listing Gain %: Not Available")

            # ✅ Build bar chart if both values available
            if cagr_value is not None and listing_gain_value is not None:
                chart_df = pd.DataFrame({
                    "Metric": ["CAGR", "Listing Gain %"],
                    "Value": [cagr_value, listing_gain_value]
                })

                chart = (
                    alt.Chart(chart_df)
                    .mark_bar(cornerRadius=6)
                    .encode(
                        x=alt.X("Metric", sort=None, title=""),
                        y=alt.Y("Value", title="Percentage"),
                        color=alt.Color("Metric", legend=None)
                    )
                    .properties(width=400, height=300)
                )

                st.altair_chart(chart, use_container_width=True)


        # ---------------- COMPANY INFO TAB ----------------
        with tab3:
            st.subheader("Company Information")
            info_cols = [
                'company', 'ltp', 'market cap(in cr)', 'listing open', 'listing close',
                'issue type', 'listing date', 'issue size (in Cr)', 'issue price (in rupee)',
                'lot size', 'sector', 'industry',
                'minimum_investment_rupee', 'subscription_status',
                'min_price_range', 'max_price_range', 'no_of_share'
            ]
            st.dataframe(selected_company_info[info_cols].T.rename(columns={selected_company_info.index[0]: "Value"}))


with about:


    st.html("""
<!-- Hero Section -->
<section class="hero-section">
    <div class="container">
        <div class="hero-content text-center">
            <h1 class="display-4 fw-bold mb-4">About IPO Predictor</h1>
            <p class="lead mb-0">Advanced AI-powered IPO performance prediction platform</p>
        </div>
    </div>
</section>

<!-- About Content -->
<section class="py-5">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 mx-auto">
                <div class="card">
                    <div class="card-body p-5">
                        <h2 class="fw-bold mb-4">What is IPO Predictor?</h2>
                        <p class="fs-6 mb-4">
                            IPO Predictor is an innovative web application that leverages machine learningto predict the performance of 
                            Initial Public Offerings (IPOs) in the Indian stock market. Our platform analyzes multiple financial metrics and 
                            market indicators to provide accurate predictions with confidence scores.
                        </p>
                        
                        <h3 class="fw-bold mb-3">How It Works</h3>
                        <p class="mb-4">
                            Our advanced machine learning model processes various financial parameters including:
                        </p>
                        <ul class="mb-4">
                            <li><strong>Financial Metrics:</strong> EPS, Operating Profit Margin, Net Profit</li>
                            <li><strong>Corporate Structure:</strong> Promoter holding percentage</li>
                            <li><strong>Market Valuation:</strong> Market capitalization analysis</li>
                        </ul>
                        
                        <h3 class="fw-bold mb-3">Data Sources</h3>
                        <p class="mb-4">
                            We aggregate data from trusted financial platforms to ensure accuracy and reliability:
                        </p>
                        <div class="row mb-4">
                            <div class="col-md-6 mb-3">
                                <div class="card bg-light">
                                    <div class="card-body text-center">
                                        <i class="fas fa-chart-line fs-1 text-primary mb-3"></i>
                                        <h5>Trendlyne</h5>
                                        <p class="small mb-0">Comprehensive financial data and analytics</p>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                        
                        <h3 class="fw-bold mb-3">Technology Stack</h3>
                        <p class="mb-3">Our platform is built using cutting-edge technologies:</p>
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <div class="text-center">
                                    <i class="fab fa-python fs-1 text-warning mb-2"></i>
                                    <h6>Python</h6>
                                    <small class="text-muted">Core backend development</small>
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <div class="text-center">
                                    <i class="fas fa-flask fs-1 text-primary mb-2"></i>
                                    <h6>Streamlit</h6>
                                    <small class="text-muted">Web framework</small>
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <div class="text-center">
                                    <i class="fas fa-brain fs-1 text-success mb-2"></i>
                                    <h6>Machine Learning</h6>
                                    <small class="text-muted">Scikit-learn algorithms</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Features Section -->
<section class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center fw-bold mb-5">Key Features</h2>
        <div class="row">
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body text-center">
                        <div class="feature-icon">
                            <i class="fas fa-rocket"></i>
                        </div>
                        <h5 class="card-title">Real-time Predictions</h5>
                        <p class="card-text">Get instant predictions with confidence scores for any supported IPO.</p>
                    </div>
                </div>
            </div>
            
            
            
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body text-center">
                        <div class="feature-icon">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h5 class="card-title">Data-Driven Insights</h5>
                        <p class="card-text">Comprehensive analysis based on multiple financial metrics and market indicators.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>


<!-- Disclaimer Section -->
<section class="py-5 bg-warning bg-opacity-10">
    <div class="container">
        <div class="row">
            <div class="col-lg-10 mx-auto">
                <div class="alert alert-warning border-0" role="alert">
                    <div class="d-flex align-items-center">
                        <i class="fas fa-exclamation-triangle fs-3 me-3"></i>
                        <div>
                            <h1 class="alert-heading">Important Disclaimer</h1>
                            <p class="mb-0">
                                The predictions provided by IPO Predictor are for educational purposes only and should not be 
                                considered as investment advice. Past performance does not guarantee future results. Always 
                                consult with qualified financial advisors before making investment decisions. We are not 
                                responsible for any financial losses incurred based on our predictions.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>""")
