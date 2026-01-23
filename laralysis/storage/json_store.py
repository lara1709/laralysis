import json
from pathlib import Path
from core.function_model import FunctionModel
from core.sequence_model import SequenceModel

JSON_PATH = Path(__file__).parent / "functions.json"

def save_functions_to_json(functions):
    data = []

    for f in functions:
        data.append(f.serialize())

    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_functions_from_json():
    if not JSON_PATH.exists():
        return []
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        
    objects = []

    for item in data:
        model_type = item.get("type")

        if model_type == "Function":
            obj = FunctionModel(
                expr_str=item["expr_str"],
                var_name=item["var_name"]
            )

        else:
            continue

        objects.append(obj)

    return objects
    


