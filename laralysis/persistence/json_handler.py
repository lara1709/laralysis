import json

def save_to_json(obj, filename):
    with open(filename, "w") as f:
        json.dump(obj.serialize(), f, indent=4)

def load_from_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data