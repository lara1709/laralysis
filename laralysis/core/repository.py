from typing import List
from core.function_model import FunctionModel
from storage.database import init_db, save_function, load_functions
from storage.json_store import save_functions_to_json, load_functions_from_json

class FunctionRepository:
    def __init__(self):
        self.functions: List[FunctionModel] =[]
        init_db()

    def add_function(self, func: FunctionModel):
        self.functions.append(func)
        save_function(func)
        save_functions_to_json(self.functions)

    def load_all(self):
        self.functions = load_functions()
        save_functions_to_json(self.functions)
        return self.functions
    def find_by_expression(self, expr_str: str):
        return [f for f in self.functions if f.expr_str == expr_str]