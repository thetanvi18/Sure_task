
import streamlit as st
import re
import fitz  # PyMuPDF

st.set_page_config(page_title="Credit Card Statement Parser")
st.title("Credit Card Statement Parser")

# Dropdown for credit card issuer
issuer = st.selectbox("Select Credit Card Issuer", ["HDFC Bank", "ICICI Bank", "State Bank of India (SBI)", "Axis Bank", "Kotak Bank"])

# File uploader for PDF
uploaded_file = st.file_uploader("Upload your PDF statement", type=["pdf"])
if uploaded_file is not None:
    pdf_data = uploaded_file.read()
    try:
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        text = ""

    if text:
        text = re.sub(r'[\r\n\xa0]+', ' ', text)
        results = {}

        # Card last 4 digits (e.g., XXXX-XXXX-XXXX-1234)
        card_match = re.search(r'(?:X{4}-){2}X{4}-(\d{4})', text)
        if card_match:
            results["Card Last 4 Digits"] = card_match.group(1)

        # Card Network (e.g., RuPay, Visa)
        network_match = re.search(r'Card Network:\s*(\w+)', text)
        if network_match:
            results["Card Network"] = network_match.group(1)

        # Cardholder Name (cleaned to avoid trailing labels)
        name_match = re.search(r'Cardholder Name:\s*([A-Za-z\s]+?)(?:\s+Card|$)', text)
        if name_match:
            results["Cardholder Name"] = name_match.group(1).strip()

        # Statement Period
        stmt_match = re.search(r'Statement Period:\s*([\d/]+)\s*to\s*([\d/]+)', text)
        if stmt_match:
            results["Statement Period"] = f"{stmt_match.group(1)} to {stmt_match.group(2)}"

        # Total Amount Due
        amt_match = re.search(r'Total Amount Due:\s*([₹]?[0-9,]+\.\d{1,2})', text)
        if amt_match:
            results["Total Amount Due"] = amt_match.group(1)

        # Payment Due Date
        due_match = re.search(r'Payment Due Date:\s*([\d/]+)', text)
        if due_match:
            results["Payment Due Date"] = due_match.group(1)

        # Display results
        if results:
            st.subheader("Extracted Data")
            for key, value in results.items():
                st.write(f"**{key}:** {value}")
        else:
            st.warning("No data found with current patterns. Try a different issuer or verify PDF content.")
    else:
        st.warning("Failed to extract text. The PDF may be scanned or poorly formatted.")
