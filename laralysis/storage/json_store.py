import json
from pathlib import Path
from core.function_model import FunctionModel

JSON_PATH = Path(__file__).parent / "functions.json"

def save_functions_to_json(functions):
    data = [f.serialize() for f in functions]
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_functions_from_json():
    if not JSON_PATH.exists():
        return []
    
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    functions = []
    for item in data:
        f = FunctionModel(
            expr_str=item["expr_str"],
            var_name=item["var_name"]
        )
        functions.append(f)
    
    return functions 


