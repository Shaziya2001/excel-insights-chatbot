import dotenv
dotenv.load_dotenv()

import streamlit as st
from chatbot.llm_interface import LLMInterface
from chatbot.data_processor import DataProcessor
from chatbot.visualization import Visualization
from chatbot.openai_model import OpenAIModel  
import pandas as pd

# Initialize components
model = OpenAIModel(model_name="gpt-3.5-turbo")
llm_interface = LLMInterface(model=model)
data_processor = DataProcessor()
visualization = Visualization()

st.title("Excel Insights Chatbot")

# File upload section
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file is not None:
    try:
        data = data_processor.load_excel(uploaded_file)
        normalized_data = data_processor.normalize_columns(data)
        st.success("File processed successfully!")
        st.dataframe(normalized_data)
        st.session_state['data'] = normalized_data
    except Exception as e:
        st.error(f"Error processing file: {e}")

# Query section
st.header("Ask a Question")
user_query = st.text_input("Enter your query:")
if st.button("Get Answer"):
    if user_query:
        try:
            response = llm_interface.query_model(user_query)
            st.write("Response:", response)
        except Exception as e:
            st.error(f"Error getting response: {e}")
    else:
        st.warning("Please enter a query.")

# Visualization section
st.header("Visualize Data")
if 'data' in st.session_state:
    data = st.session_state['data']
    x_column = st.selectbox("Select X-axis column:", data.columns)
    y_column = st.selectbox("Select Y-axis column:", data.columns)
    if st.button("Generate Bar Chart"):
        try:
            chart = visualization.create_bar_chart(data, x_column, y_column)
            st.pyplot(chart)
        except Exception as e:
            st.error(f"Error generating visualization: {e}")
else:
    st.info("Please upload and process an Excel file first.")
