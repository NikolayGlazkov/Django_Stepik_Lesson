import requests

def collect_usernames(data, usernames={}):
    """
    Рекурсивно собирает имена пользователей из сообщений и комментариев.

    :param data: часть данных, которую необходимо обработать (словарь или список)
    :param usernames: словарь для сбора имен пользователей, где ключ - имя пользователя, а значение - количество упоминаний
    """
    # Если data - это список, обрабатываем каждый элемент списка
    if isinstance(data, list):
        for item in data:
            collect_usernames(item, usernames)
    # Если data - это словарь и содержит ключ 'username', добавляем/обновляем имя пользователя в словаре
    elif isinstance(data, dict):
        if 'username' in data:
            username = data['username']
            if username in usernames:
                usernames[username] += 1
            else:
                usernames[username] = 1
        # Рекурсивно обрабатываем вложенные комментарии, если они есть
        for key in data:
            if isinstance(data[key], (dict, list)):
                collect_usernames(data[key], usernames)
    return usernames

# Получаем данные
response = requests.get(url='https://parsinger.ru/3.4/3/dialog.json')
if response.status_code == 200:
    data = response.json()
    usernames = collect_usernames(data)
    print(usernames)
else:
    print("Ошибка при получении данных")
