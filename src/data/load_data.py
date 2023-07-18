import json


async def load_materias_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
