# PDF-Merger


## Overview

The PDF Merger App is a simple web application that allows users to merge multiple PDF files into a single PDF document. The app is designed to be user-friendly, secure, and privacy-conscious.

## Features

- Merge multiple PDF files into a single PDF.
- No data storage: The app does not store any user data on the server or any persistent storage.

## How it Works

1. Upload PDF files: Users can upload multiple PDF files using the "Choose PDF files" button.
2. Merge PDFs: Click the "Merge PDFs" button to combine the uploaded PDFs into a single merged PDF.
3. Download Merged PDF: Once the merging process is complete, the app will provide a downloadable link for the merged PDF. The merged PDF is generated in-memory and not stored on the server.

#3 Link to Application

[Link to application]

## Privacy and Security

- **No Data Storage**: The PDF Merger App does not store any user data, including the uploaded PDF files and the resulting merged PDF.
- **Data Encryption**: If accessed over the internet, the app uses encryption to protect data during transmission.
- **User Consent**: The app explicitly asks for user consent before merging the uploaded PDF files.
- **Data Deletion**: Uploaded PDF files are processed in-memory and discarded once the merging process is complete.


To run the PDF Merger App, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies (`streamlit` and `PyPDF2`) using `pip`.
3. Run the app using `streamlit run app.py`.
4. Access the app through your web browser at `http://localhost:8501`.

## Requirements

- Python 3.6+
- Streamlit (install using `pip install streamlit`)
- PyPDF2 (install using `pip install PyPDF2`)


