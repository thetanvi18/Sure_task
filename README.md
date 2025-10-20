# Sure Financial Company task for placement process

Features
-Lightweight Streamlit app that extracts key financial details from PDF credit card statement of popular Indian Banks & Credit Card Providers. 
-Clean UI with dropdown issuer selection
-Handles noisy text and formatting inconsistencies
1)Upload PDF statements from major Indian banks
2)Extract key fields like:
Cardholder Name
Card Network (e.g., RuPay, Visa)
Last 4 Digits of Card
Statement Period
Total Amount Due
Payment Due Date


Tech Stack
1)Streamlit – for interactive UI
command: pip install streamlit

2)PyMuPDF (fitz) – for PDF text extraction
command: pip install pymupdf

3)Regex – for pattern-based parsing
command in code(no need to install): import re

Current Scope:
-extracts text only from pdf

Future Scope:
-integrate OCR for image-based pdf
