import requests

url = requests.get("https://rf-naruto-api.herokuapp.com/api/v1/shinobi")

dados = url.json()

for dado in dados:
    print(dado.get('name'))


