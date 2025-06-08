# Excel Insights Chatbot

## Overview
The Excel Insights Chatbot is a web-based conversational assistant designed to help users extract insights from Excel files effortlessly. By leveraging natural language processing, the chatbot allows users to ask questions in plain English and receive quick, accurate responses based on the data contained in their Excel reports.

## Features
- Upload Excel files and analyze structured data.
- Ask natural language questions to retrieve insights.
- Generate statistical summaries, filtered queries, and comparisons.
- Visualize data trends and distributions through charts.
- Flexible and schema-agnostic design to accommodate various Excel formats.

## Project Structure
```
excel-insights-chatbot
├── src
│   ├── app.py                # Main entry point of the application
│   ├── chatbot
│   │   ├── __init__.py       # Initializes the chatbot package
│   │   ├── llm_interface.py   # Manages interactions with the language model
│   │   ├── data_processor.py   # Handles reading and analyzing Excel files
│   │   ├── visualization.py     # Generates charts based on processed data
│   │   └── openai_model.py       # Wrapper for OpenAI model integration
│   ├── ui
│   │   ├── __init__.py        # Initializes the UI package
│   │   └── streamlit_ui.py    # Sets up the user interface using Streamlit
│   └── utils
│       └── helpers.py         # Contains utility functions for various tasks
├── requirements.txt           # Lists project dependencies
├── README.md                  # Documentation for the project
└── solution.pptx              # Presentation describing the solution
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd excel-insights-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the chatbot interface.

3. Upload your Excel file and start asking questions to gain insights from your data.

## Deployment

- If deploying to Streamlit Cloud or another platform, set your `OPENAI_API_KEY` in the platform's secrets or environment variable settings (do not upload your `.env` file).

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.
