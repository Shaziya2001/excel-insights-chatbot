def normalize_column_name(column_name):
    # Normalize column names by stripping whitespace and converting to lowercase
    return column_name.strip().lower().replace(" ", "_")

def handle_missing_values(dataframe):
    # Fill missing values with a placeholder or drop them based on the context
    return dataframe.fillna("N/A")

def validate_query(query):
    # Basic validation for user queries to ensure they are not empty
    if not query:
        raise ValueError("Query cannot be empty.")
    return query

def extract_numeric_columns(dataframe):
    # Extract columns with numeric data types from the dataframe
    return dataframe.select_dtypes(include=['number']).columns.tolist()

def extract_categorical_columns(dataframe):
    # Extract columns with categorical data types from the dataframe
    return dataframe.select_dtypes(include=['object']).columns.tolist()