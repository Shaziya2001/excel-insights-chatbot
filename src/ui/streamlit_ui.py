import streamlit as st
from chatbot.data_processor import DataProcessor
from chatbot.visualization import Visualization
from chatbot.llm_interface import LLMInterface

def main():
    st.title("Excel Insights Chatbot")
    
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        data_processor = DataProcessor()
        data = data_processor.load_excel(uploaded_file)
        
        if data is not None:
            st.write("Data Preview:")
            st.dataframe(data)
            
            user_query = st.text_input("Ask a question about the data:")
            
            if st.button("Get Insights"):
                llm_interface = LLMInterface()
                response = llm_interface.query_model(user_query, data)
                
                if response['type'] == 'text':
                    st.write(response['content'])
                elif response['type'] == 'table':
                    st.write("Results:")
                    st.dataframe(response['content'])
                elif response['type'] == 'chart':
                    visualization = Visualization()
                    chart = visualization.create_bar_chart(response['content'])
                    st.pyplot(chart)
        else:
            st.error("Failed to load data from the Excel file.")
    else:
        st.info("Please upload an Excel file to get started.")

if __name__ == "__main__":
    main()