from storage.database import load_functions, save_function
from storage.json_store import load_functions_from_json, save_functions_to_json

class FunctionRepository:
    def __init__(self):
        self.functions = []

    def load_all(self):
        self.functions = load_functions()
        return self.functions
    
    def load_from_json(self):
        self.functions = load_functions_from_json()
        return self.functions
    
    def add_function(self, function):
        self.functions.append(function)
        save_function(function)
        save_functions_to_json(self.functions)

    def get_all_functions(self):
        return self.functions