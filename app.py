import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
st.set_page_config(layout="wide")
uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    # Determine the file type and use the appropriate pandas function to read it
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)  # Remove the encoding parameter for Excel files
    elif uploaded_file.name.endswith(('.json')):
        df = pd.read_json(uploaded_file, encoding="utf-8")
    elif uploaded_file.name.endswith(('.txt')):
        df = pd.read_csv(uploaded_file, delimiter='\t', encoding="utf-8")
    else:
        raise ValueError("Unsupported file type")
        
    # Display the DataFrame using Streamlit
    st.write(df)
    
    # Optionally, render the DataFrame using Streamlit Renderer
    statlance_app = StreamlitRenderer(df)
    statlance_app.explorer()
else:
    st.write("No file uploaded yet.")
