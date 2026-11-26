
import streamlit as st
import pandas as pd

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Vendor Management System",
    page_icon="V",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F5F6F8;
    color: #252B36;
}

/* Main content */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #202B3C;
}

[data-testid="stSidebar"] * {
    color: #E8EDF4 !important;
}

[data-testid="stSidebar"] hr {
    border-color: #3B4656;
}

/* Sidebar navigation */

[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px;
}

[data-testid="stSidebar"] [role="radio"] {
    padding: 9px 10px;
    border-radius: 4px;
}

[data-testid="stSidebar"] [role="radio"]:hover {
    background: #344357;
}

/* Headings */

h1 {
    color: #202B3C;
    font-size: 27px !important;
    font-weight: 600 !important;
    letter-spacing: -0.5px;
}

h2 {
    color: #202B3C;
    font-size: 21px !important;
    font-weight: 600 !important;
}

h3 {
    color: #344054;
    font-size: 17px !important;
    font-weight: 600 !important;
}

/* Header */

.hero {
    background: #FFFFFF;
    padding: 22px 24px;
    border: 1px solid #E1E5EB;
    border-left: 4px solid #344F70;
    border-radius: 4px;
    margin-bottom: 25px;
}

.hero h2 {
    color: #202B3C;
    font-size: 23px;
    font-weight: 600;
    margin: 0 0 7px 0;
}

.hero p {
    color: #667085;
    font-size: 14px;
    margin: 0;
}

/* Metric cards */

.metric-card {
    background: #FFFFFF;
    padding: 20px;
    border: 1px solid #E1E5EB;
    border-radius: 5px;
    height: 125px;
}

.metric-title {
    color: #667085;
    font-size: 12px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.4px;
}

.metric-value {
    color: #202B3C;
    font-size: 25px;
    font-weight: 600;
    margin-top: 10px;
}

.small-label {
    color: #7A8493;
    font-size: 12px;
    margin-top: 5px;
}

/* Information cards */

.info-card {
    background: #FFFFFF;
    padding: 22px;
    border: 1px solid #E1E5EB;
    border-radius: 5px;
    margin-bottom: 12px;
    min-height: 270px;
}

.info-card h3 {
    color: #344054;
    font-size: 17px;
    margin-top: 0;
    margin-bottom: 14px;
}

.info-card p {
    color: #667085;
    font-size: 14px;
    line-height: 1.7;
}

.info-card ul {
    color: #475467;
    font-size: 14px;
    line-height: 1.9;
    padding-left: 20px;
}

.info-card hr {
    border: none;
    border-top: 1px solid #E1E5EB;
    margin: 18px 0;
}

.model-label {
    color: #667085;
    font-size: 13px;
    margin-top: 15px;
}

/* Buttons */

.stButton > button,
.stFormSubmitButton > button {
    background: #344F70;
    color: #FFFFFF;
    border: 1px solid #344F70;
    border-radius: 4px;
    padding: 9px 18px;
    font-size: 14px;
    font-weight: 500;
    box-shadow: none;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #293F5A;
    border-color: #293F5A;
    color: #FFFFFF;
}

/* Inputs */

.stNumberInput input {
    border-radius: 4px;
}

/* Forms */

[data-testid="stForm"] {
    background: #FFFFFF;
    padding: 22px;
    border: 1px solid #E1E5EB;
    border-radius: 5px;
}

/* Dataframes */

[data-testid="stDataFrame"] {
    border: 1px solid #E1E5EB;
    border-radius: 5px;
}

/* Alerts */

[data-testid="stAlert"] {
    border-radius: 4px;
}

/* Footer */

.footer {
    text-align: center;
    color: #98A2B3;
    font-size: 12px;
    padding: 15px 0;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# REUSABLE FUNCTIONS
# ==================================================

def metric_card(title, value, description):

    st.html(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        <div class="small-label">{description}</div>
    </div>
    """)


def page_header(title, description):

    st.html(f"""
    <div class="hero">
        <h2>{title}</h2>
        <p>{description}</p>
    </div>
    """)


def section_title(title):

    st.markdown(f"### {title}")


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("# VENDOR PORTAL")

    st.caption("PROCUREMENT & INVOICE MANAGEMENT")

    st.markdown("---")

    st.markdown("#### WORKSPACE")

    module = st.radio(
        "Select Module",
        [
            "Overview",
            "Freight Prediction",
            "Invoice Risk Detection"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("#### SYSTEM INFORMATION")

    st.caption("Available Modules: 02")
    st.caption("Environment: Development")
    st.caption("Version: 1.0.0")

    st.markdown("---")

    st.caption("Vendor Management System")


# ==================================================
# OVERVIEW PAGE
# ==================================================

if module == "Overview":

    page_header(
        "Vendor Management Dashboard",
        "Monitor freight expenditure and evaluate vendor invoices using predictive analytics."
    )

    section_title("System Overview")

    col1, col2, col3 = st.columns(3)

    with col1:

        metric_card(
            "AVAILABLE MODULES",
            "02",
            "Prediction modules available"
        )

    with col2:

        metric_card(
            "FREIGHT ANALYSIS",
            "Regression",
            "Freight cost estimation"
        )

    with col3:

        metric_card(
            "INVOICE ANALYSIS",
            "Classification",
            "Invoice risk identification"
        )

    st.markdown("")

    section_title("Available Operations")

    col1, col2 = st.columns(2)

    with col1:

        st.html("""
        <div class="info-card">

            <h3>Freight Cost Prediction</h3>

            <p>
                Estimate expected transportation expenses
                based on shipment information.
            </p>

            <hr>

            <b>Input Parameters</b>

            <ul>
                <li>Shipment value</li>
                <li>Shipment quantity</li>
            </ul>

            <div class="model-label">
                Model Type: Regression
            </div>

        </div>
        """)

    with col2:

        st.html("""
        <div class="info-card">

            <h3>Invoice Risk Detection</h3>

            <p>
                Evaluate invoice details and identify
                transactions that require manual review.
            </p>

            <hr>

            <b>Input Parameters</b>

            <ul>
                <li>Invoice amount and quantity</li>
                <li>Freight cost and brand information</li>
                <li>Purchase order processing time</li>
                <li>Item quantity and amount</li>
            </ul>

            <div class="model-label">
                Model Type: Classification
            </div>

        </div>
        """)

    section_title("System Workflow")

    st.html("""
    <div class="info-card">

        <b>01. Data Entry</b>
        <p>Enter shipment or invoice information.</p>

        <hr>

        <b>02. Model Processing</b>
        <p>
            The trained machine learning model processes
            the provided input data.
        </p>

        <hr>

        <b>03. Prediction Generation</b>
        <p>
            The system generates freight estimates or
            invoice risk classifications.
        </p>

        <hr>

        <b>04. Business Review</b>
        <p>
            Use the generated results to support cost
            planning and invoice approval decisions.
        </p>

    </div>
    """)


# ==================================================
# FREIGHT PREDICTION PAGE
# ==================================================

elif module == "Freight Prediction":

    page_header(
        "Freight Cost Prediction",
        "Estimate transportation expenses based on shipment value and quantity."
    )

    section_title("Shipment Information")

    st.info(
        "Enter the shipment details below to calculate the estimated freight cost."
    )

    with st.form("freight_form"):

        col1, col2 = st.columns(2)

        with col1:

            dollars = st.number_input(
                "Shipment Value ($)",
                min_value=0.0,
                value=18500.0,
                step=500.0
            )

        with col2:

            quantity = st.number_input(
                "Shipment Quantity",
                min_value=0.0,
                value=10.0,
                step=1.0
            )

        st.markdown("---")

        submit = st.form_submit_button(
            "Predict Freight Cost",
            use_container_width=True
        )

    if submit:

        if dollars <= 0 or quantity <= 0:

            st.warning(
                "Please enter a valid shipment value and quantity."
            )

        else:

            input_data = {
                "Dollars": [dollars],
                "Quantity": [quantity]
            }

            try:

                with st.spinner("Processing shipment information..."):

                    result = predict_freight_cost(input_data)

                st.success("Freight prediction completed.")

                section_title("Prediction Results")

                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True
                )

            except Exception as e:

                st.error(
                    f"Unable to generate freight prediction: {e}"
                )


# ==================================================
# INVOICE RISK DETECTION PAGE
# ==================================================

elif module == "Invoice Risk Detection":

    page_header(
        "Invoice Risk Detection",
        "Evaluate invoice information and identify transactions requiring manual approval."
    )

    section_title("Invoice Information")

    st.info(
        "Provide the invoice and item details. "
        "The classification model will evaluate the information."
    )

    with st.form("invoice_form"):

        st.markdown("#### Invoice Details")

        col1, col2 = st.columns(2)

        with col1:

            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=0.0,
                value=10.0
            )

            invoice_dollars = st.number_input(
                "Invoice Amount ($)",
                min_value=0.0,
                value=8200.0
            )

            freight = st.number_input(
                "Freight Cost ($)",
                min_value=0.0,
                value=400.0
            )

        with col2:

            total_brands = st.number_input(
                "Total Brands",
                min_value=0.0,
                value=2.0
            )

            days_po_to_invoice = st.number_input(
                "Days: PO to Invoice",
                min_value=0.0,
                value=3.0
            )

        st.markdown("---")

        st.markdown("#### Item Details")

        col3, col4 = st.columns(2)

        with col3:

            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=0.0,
                value=10.0
            )

        with col4:

            total_item_dollars = st.number_input(
                "Total Item Amount ($)",
                min_value=0.0,
                value=8000.0
            )

        st.markdown("---")

        submit = st.form_submit_button(
            "Evaluate Invoice Risk",
            use_container_width=True
        )

    if submit:

        if invoice_dollars <= 0 or invoice_quantity <= 0:

            st.warning(
                "Please enter a valid invoice amount and quantity."
            )

        else:

            input_data = {

                "invoice_quantity": [invoice_quantity],

                "invoice_dollars": [invoice_dollars],

                "Freight": [freight],

                "total_brands": [total_brands],

                "days_po_to_invoice": [days_po_to_invoice],

                "total_item_quantity": [total_item_quantity],

                "total_item_dollars": [total_item_dollars]

            }

            try:

                with st.spinner("Evaluating invoice information..."):

                    result = predict_invoice_flag(input_data)

                prediction = result[
                    "Predicted_Invoice_Flag"
                ].values[0]

                section_title("Invoice Evaluation Result")

                if prediction == 1:

                    st.error("MANUAL APPROVAL REQUIRED")

                    st.html("""
                    <div class="info-card">

                        <h3 style="color:#B42318;">
                            Invoice Flagged for Review
                        </h3>

                        <p>
                            The classification model has identified
                            this invoice as requiring additional verification.
                        </p>

                        <p>
                            Review the invoice details before
                            approving the payment.
                        </p>

                    </div>
                    """)

                else:

                    st.success("NO RISK FLAG DETECTED")

                    st.html("""
                    <div class="info-card">

                        <h3 style="color:#027A48;">
                            Invoice Classified as Low Risk
                        </h3>

                        <p>
                            The model has not identified a risk flag
                            for this invoice.
                        </p>

                        <p>
                            The invoice can proceed to the
                            standard approval workflow.
                        </p>

                    </div>
                    """)

                section_title("Prediction Details")

                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True
                )

            except Exception as e:

                st.error(
                    f"Unable to evaluate invoice: {e}"
                )


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.html("""
<div class="footer">
    Vendor Management System |
    Machine Learning Based Analysis
</div>
""")
