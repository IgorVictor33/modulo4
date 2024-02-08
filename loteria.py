import requests
import json
import statistics
site = requests.get("http://loteriascaixa-api.herokuapp.com/api/megasena")
numero = site.json()
lista_sorteio = []

for dezena in numero:
    valores = dezena['dezenasOrdemSorteio']
    lista_sorteio.append(valores)
    a = statistics.mode = [1, 2, 2, 3, 4]
    print(a)
