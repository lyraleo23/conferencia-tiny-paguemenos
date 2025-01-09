import os
import asyncio
import time
import pandas as pd
from api_tiny import pesquisar_pedidos

TOKEN_TINY = '40134277698ea31727f6ee9950df2ca290d881fa'

async def main():
    dados = pd.read_excel('Pedidos.xlsx')
    lista_pedidos_vnda = dados['Nº pedido'].tolist()
    lista_pedidos_vnda = set(lista_pedidos_vnda)

    new_xlsx = [
        ['vnda', 'tiny']
    ]

    k = 1

    for pedido in lista_pedidos_vnda:
        os.system('cls')
        print(f'==== {k}/{len(lista_pedidos_vnda)} ====')
        print(pedido)

        status_tiny = '0'
        while status_tiny != '3' and status_tiny != '2':
            try:
                response = pesquisar_pedidos(TOKEN_TINY, pedido)
                status_tiny = response['retorno']['status_processamento']

                if status_tiny == '3':
                    pedidosTiny = response['retorno']['pedidos']
                else:
                    time.sleep(5)
            except:
                time.sleep(5)
        time.sleep(10)

        if len(pedidosTiny) > 0 and status_tiny != '2':
            for p in pedidosTiny:
                linha = [pedido, p['pedido']['numero']]
                new_xlsx.append(linha)
        else:
            linha = [pedido, '']
            new_xlsx.append(linha)

        k = k+1

        df = pd.DataFrame(new_xlsx)
        df.to_excel(f'conferencia.xlsx', index=True, header=False)

asyncio.run(main())
