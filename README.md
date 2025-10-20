# Sure Financial Company task for placement process

Features<br>
-Lightweight Streamlit app that extracts key financial details from PDF credit card statement of popular Indian Banks & Credit Card Providers.<br>
-Clean UI with dropdown issuer selection<br>
-Handles noisy text and formatting inconsistencies<br>

Steps<br>
1)To run: streamlit run Sure_task.py<br>
2)Upload PDF statements from major Indian banks<br>

Output<br>
Extract key fields like:<br>
-Cardholder Name<br>
-Card Network (e.g., RuPay, Visa)<br>
-Last 4 Digits of Card<br>
-Statement Period<br>
-Total Amount Due<br>
-Payment Due Date<br>

Tech Stack<br>
1)Streamlit – for interactive UI<br>
command: pip install streamlit<br>

2)PyMuPDF (fitz) – for PDF text extraction<br>
command: pip install pymupdf<br>

3)Regex – for pattern-based parsing<br>
command in code(no need to install): import re<br>

Current Scope:-extracts text only from pdf

Future Scope:-integrate OCR for image-based pdf
