"""
task 1
pylint 10
"""
import json
import requests

if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/todos/'
    RESPONSE = requests.get(URL, timeout=5)
    if RESPONSE.status_code == 200:
        TODOS_DATA = RESPONSE.json()
        with open('todos.json', 'w', encoding="utf-8") as f:
            json.dump(TODOS_DATA, f, indent=2)
        print('Данные успешно записаны в файл todos.json.')
    else:
        print(f'Ошибка при запросе данных: {RESPONSE.status_code}')

    with open('todos.json', 'r', encoding="utf-8") as f:
        todos_data = json.load(f)
    if todos_data:
        print(f'Прочитано {len(todos_data)} записей из файла.')
    else:
        print('Ошибка при чтении файла или файл пуст.')
    for idx, todo in enumerate(todos_data, start=1):
        filename = f'todo_{idx}.json'
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(todo, f, indent=2)
        print(f'Файл {filename} успешно записан.')
    print(f'Все файлы были успешно записаны. Всего создано {len(todos_data)} файлов.')
