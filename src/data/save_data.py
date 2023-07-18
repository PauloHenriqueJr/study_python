import json


def save_materias_to_json(materias, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(materias, file, ensure_ascii=False)
