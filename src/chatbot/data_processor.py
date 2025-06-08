class DataProcessor:
    def __init__(self):
        self.data = None

    def load_excel(self, file_path):
        import pandas as pd
        self.data = pd.read_excel(file_path)
        return self.data  # Return the loaded data

    def normalize_columns(self, data):
        data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]
        return data

    def generate_summary(self, query):
        pass

    def filter_data(self, conditions):
        pass

    def compare_groups(self, group_by_column, target_column):
        pass

    def handle_missing_values(self):
        pass
