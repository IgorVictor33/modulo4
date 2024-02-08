import requests
import json
import random
site = requests.get("http://loteriascaixa-api.herokuapp.com/api/megasena")
numero = site.json()
lista_sorteio = []

for dezena in numero:
    valores = dezena['dezenasOrdemSorteio']
    lista_sorteio.append(valores)
sorte = []
for i in range(6):
    sorte.append(random.choice(lista_sorteio))
    
print(sorte)