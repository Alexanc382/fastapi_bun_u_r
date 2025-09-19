import requests

access_key = 'OfPkM2ws-f3RelK3LSRw6Xd6MgKfGqIrJMKmgHTyzXM'
query = 'bread-biscuits'  # ключевое слово для крекеров
# query = 'donut' пончик
# query = 'croissant' круассан

url = f'https://api.unsplash.com/photos/random?query={query}&client_id={access_key}&count=1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        # Получаем URL изображения (например, размер regular)
        image_url = data[0]['urls']['regular']
        print(f'Случайное фото пончика: {image_url}')
    else:
        print('Фото по запросу не найдены')
else:
    print(f'Ошибка запроса: {response.status_code}')