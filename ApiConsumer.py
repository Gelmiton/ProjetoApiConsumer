from flask import request
import requests

clienteid = input('Digite o ID do cliente: ')

r = requests.get('https://personal-hihflja6.outsystemscloud.com/Projeto_Ficr_Clientes/rest/ApiClientes/')

print(r.json)
