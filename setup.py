from setuptools import find_packages, setup

setup(
    name="PDFCHATRAGBOT",
    version="0.0.1",
    author="Pramod",
    author_email="pramodklal@gmail.com",
    packages=find_packages(),
    install_requires=['openai','google-cloud-aiplatform','langchain ','langchain-openai','datasets','PyPDF2','python-dotenv','streamlit','pytesseract','google-generativeai','faiss-cpu','altair']
)