import requests
import json
import time


def obter_pedidos_v3(access_token, params):
    offset = 0
    total = 100
    lista_pedidos = []

    url_params = ''
    for key, value in params.items():
        url_params += f'{key}={value}&'

    while offset < total:
        try:
            url = f'https://api.tiny.com.br/public-api/v3/pedidos?{url_params}offset={offset}'
            print(url)

            payload = ''
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            response = response.json()

            offset = offset + 100
            total = response['paginacao']['total']
            print(f'total: {total}')

            lista_pedidos = [*lista_pedidos, *response['itens']]
        except Exception as e:
            print(e)
            time.sleep(5)
    
    return lista_pedidos

def obter_pedido_v3(access_token, id_pedido):
    url = f'https://api.tiny.com.br/public-api/v3/pedidos/{id_pedido}'
    print(url)

    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response

def obter_nota_fiscal_v3(access_token, id_nota):
    url = f'https://api.tiny.com.br/public-api/v3/notas/{id_nota}'
    print(url)

    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response

def obter_marcadores_v3(access_token, id_pedido):
    url = f'https://api.tiny.com.br/public-api/v3/pedidos/{id_pedido}/marcadores'
    print(url)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers)
    response = response.json()
    return response
