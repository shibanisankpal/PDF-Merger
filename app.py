import streamlit as st
import PyPDF2
from io import BytesIO

def merge_pdfs(files):
    merger = PyPDF2.PdfMerger()
    for file in files:
        pdf_reader = PyPDF2.PdfReader(file)
        merger.append(fileobj=pdf_reader)
    return merger

def main():
    st.title("PDF Merger App")

    st.write("Upload multiple PDF files, and the app will merge them into a single PDF.")

    uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type=["pdf"])

    if st.button("Merge PDFs") and uploaded_files:
        merger = merge_pdfs(uploaded_files)

        output_pdf = BytesIO()
        merger.write(output_pdf)

        st.success("PDFs merged successfully!")
        st.download_button("Download the merged PDF", file_name="combined.pdf", data=output_pdf.getvalue(), mime="application/pdf")

if __name__ == "__main__":
    main()
