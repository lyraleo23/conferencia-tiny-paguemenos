import os
import asyncio
import time
import pandas as pd
from dotenv import load_dotenv

from api_tiny_v3 import obter_pedidos_v3
from api_miliapp import obter_tokens_tiny

load_dotenv()
TOKEN_TINY = os.getenv('TOKEN_TINY')
origin = 'miligrama'
ACCESS_TOKEN, REFRESH_TOKEN = obter_tokens_tiny(origin)

async def main():
    dados = pd.read_excel('Pedidos.xlsx')
    lista_pedidos_vtex = dados['Pedido VTEX'].tolist()
    lista_pedidos_vtex = set(lista_pedidos_vtex)

    new_xlsx = [
        ['VTEX', 'tiny', 'situacao', 'transportadora', 'uf']
    ]

    k = 1

    for pedido in lista_pedidos_vtex:
        os.system('cls')
        print(f'==== {k}/{len(lista_pedidos_vtex)} ====')
        print(pedido)

        params = {
            'numeroPedidoEcommerce': 'PGM-' + pedido
        }
        pedidosTiny = obter_pedidos_v3(ACCESS_TOKEN, params)

        if len(pedidosTiny) > 0:
            for p in pedidosTiny:
                situacao = p['situacao']

                match situacao:
                    case 0:
                        situacao_nome = 'aberto'
                    case 1:
                        situacao_nome = 'faturado'
                    case 2:
                        situacao_nome = 'cancelado'
                    case 3:
                        situacao_nome = 'aprovado'
                    case 4:
                        situacao_nome = 'preparando_envio'
                    case 5:
                        situacao_nome = 'enviado'
                    case 6:
                        situacao_nome = 'entregue'
                    case 7:
                        situacao_nome = 'pronto_envio'
                    case 8:
                        situacao_nome = 'dados_incompletos'
                    case 9:
                        situacao_nome = 'nao_entregue'

                linha = [pedido, p['numeroPedido'], situacao_nome, p['transportador']['formaEnvio']['nome'], p['cliente']['endereco']['uf']]
                new_xlsx.append(linha)
        else:
            linha = [pedido, '', '']
            new_xlsx.append(linha)

        k = k+1

        df = pd.DataFrame(new_xlsx)
        df.to_excel(f'conferencia.xlsx', index=True, header=False)

asyncio.run(main())
