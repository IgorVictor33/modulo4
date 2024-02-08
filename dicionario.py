import requests
import json
site = requests.get("http://api.gameofthronesquotes.xyz/v1/random")
dic = site.json()
frase = dic ["sentence"]
nome = dic ["character"]["name"]
print(f'minha frase =', frase)
print(f' meu nome =', nome)

# "Frase" - meu nome