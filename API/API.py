import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']['bid']
print(f'A cotaçõa do dolar é {cotacoes_dolar}')