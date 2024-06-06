# Lab-9
Лабораторна робота 9: Обробка JSON даних у Python

Мета роботи
Метою даної лабораторної роботи є вивчення методів обробки JSON даних у Python, зокрема читання, запису, пошуку та модифікації інформації у JSON файлах.

Опис завдання
Завдання 1: Написати функцію, яка читає JSON файл і повертає список імен людей, чий вік перевищує заданий поріг.
Завдання 2: Написати функцію, яка зберігає задані дані у JSON файл.
Завдання 3: Написати функцію, яка перевіряє правильність структури JSON файлів та повертає список файлів з помилками.
Завдання 4: Написати функцію, яка витягує всі значення за заданим ключем з JSON файлу.
Завдання 5: Написати функцію, яка оновлює значення у JSON файлі відповідно до заданої категорії та функції оновлення.

Виконання роботи

Завдання 1:
import json

def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above_threshold = [entry['name'] for entry in data if entry['age'] > age_threshold]
    return names_above_threshold

# Приклад використання:
file_path = 'people.json'
age_threshold = 30
print(task1(file_path, age_threshold))

Завдання 2:
def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Приклад використання:
data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
file_path = 'output.json'
task2(data, file_path)

Завдання 3:
import json

def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                invalid_files.append(file_path)
    return invalid_files

# Приклад використання:
schema = {}  # Додаємо схему, якщо потрібно
file_paths = ['file1.json', 'file2.json']
print(task3(schema, file_paths))

Завдання 4:
import json

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

# Приклад використання:
file_path = 'data.json'
key = 'name'
print(task4(file_path, key))

Завдання 5:
import json

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

# Приклад використання:
file_path = 'products.json'
category = 'electronics'
task5(file_path, category, increase_price)

Результати
Завдання 1: Отримано список імен людей, чий вік перевищує заданий поріг.
Завдання 2: Дані успішно збережені у JSON файл.
Завдання 3: Отримано список файлів з неправильними JSON структурами.
Завдання 4: Витягнуто всі значення за заданим ключем з JSON файлу.
Завдання 5: Значення у JSON файлі оновлені відповідно до заданої категорії.

Вимоги до середовища:Python 3.x
