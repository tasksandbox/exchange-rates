import requests
import json
import pandas as pd

# получаем JSON файл из открытого API с полученным ключом: ee67cc026a6ea30305d98993
url = "https://v6.exchangerate-api.com/v6/ee67cc026a6ea30305d98993/latest/USD"
response = requests.get(url)
data = response.json()

# сохраняем полученный JSON
with open('backup.json', 'w') as file:
    json.dump(data, file)

# заводим данные в таблицу Pandas, если запрос успешен
conversion_rates = data['conversion_rates']
df = pd.DataFrame(conversion_rates.items(), columns=['Currency', 'Rate_to_USD'])

# сохраняем в XLSX и CSV
df.to_excel('rates.xlsx', index=False)
df.to_csv('rates.csv', index=False)