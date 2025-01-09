# Conferência integração Vnda x Tiny<br/>

## Objetivo:<br/>
A partir da listagem de pedidos no arquivo Pedidos.xlsx, o programa deve procurar cada um dos pedidos na Tiny para conferência se todos os pedidos foram integrados.<br/>
O program irá gerar como output um arquivo em excel conferencia.xlsx mostrando o número do pedido na Vnda e o número do pedido na Tiny, quando houver.<br/>
<br/>

## Arquitetura<br/>
* Python<br/>
* API Miliapp<br/>
* API Tiny V2<br/>
<br/>

## Execução do código<br/>
Baixar a planilha de pedidos da Vnda que estejam com o status de Confirmado.<br/>
Colocar na pasta raiz do programa e rodar a função main.<br/>
Será gerado o arquivo conferencia.xlsx com a listagem dos pedidos da Vnda (coluna B) e o número do pedido na Tiny (coluna C).<br/>
Se a coluna C estiver vazia ou com o número 0, deverá ser feita a conferência manual do pedido para verificar se realmente não está na Tiny. Caso não esteja, forçar integração.<br/>
<br/>
