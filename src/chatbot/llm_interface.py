class LLMInterface:
    def __init__(self, model):
        self.model = model

    def query_model(self, query):
        response = self.model.generate_response(query)
        return response

    def process_response(self, response):
        # Implement any necessary processing of the response here
        return response.strip()