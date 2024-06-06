import json
def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above_threshold = [entry['name'] for entry in data if entry['age'] > age_threshold]
    return names_above_threshold

def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                pass
            except json.JSONDecodeError:
                invalid_files.append(file_path)
    return invalid_files


def task4(file_path, key):
    def extract_values(obj, key):
        values = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    values.append(v)
                elif isinstance(v, (dict, list)):
                    values.extend(extract_values(v, key))
        elif isinstance(obj, list):
            for item in obj:
                values.extend(extract_values(item, key))
        return values

    with open(file_path, 'r') as file:
        data = json.load(file)
    values = extract_values(data, key)
    return values


def task5(file_path, category, update_function):
    with open(file_path, 'r+') as file:
        data = json.load(file)
        for item in data:
            if item.get('category') == category:
                update_function(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def increase_price(item):
    item['price'] += 10


