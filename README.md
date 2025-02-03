# 🔍 Conferência de Pedidos: Tiny vs. PagueMenos

## 📋 Descrição

Este projeto em Python tem como objetivo automatizar a conferência dos pedidos da plataforma **PagueMenos**  
com os dados obtidos de duas contas do **Tiny ERP**.  

O código executa as seguintes etapas:  
1. **Lê a planilha de entrada** (`Pedidos.xlsx`) com os pedidos vindos da PagueMenos.  
2. **Consulta o Tiny ERP** em ambas as contas para verificar o status do pedido e obter os dados da nota fiscal.  
3. **Gera a planilha de saída** (`conferencia.xlsx`), consolidando as informações necessárias para abastecimento na plataforma da PagueMenos.  

📌 **Futuro aprimoramento:** Está planejada a automação do preenchimento dos dados da planilha `conferencia.xlsx` diretamente na plataforma da PagueMenos.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.  
- **Bibliotecas Principais**:
  - `pandas`: Manipulação e análise de dados da planilha.  
  - `openpyxl`: Leitura e escrita de arquivos Excel.  
  - `requests`: Comunicação com a API do Tiny ERP.  
  - `dotenv`: Gerenciamento de variáveis de ambiente.  

## 🚀 Como Utilizar o Projeto

### Passo 1: Clonar o Repositório
```bash
git clone https://github.com/lyraleo23/conferencia-tiny-paguemenos.git
cd conferencia-tiny-paguemenos
```

### Passo 2: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e configure suas credenciais de acesso ao Tiny ERP:
```bash
TOKEN_MILIAPP
```

### Passo 4: Executar o Script Principal
```bash
python main.py
```

### Passo 5: Verificar a Planilha Gerada
O arquivo `conferencia.xlsx` será salvo na pasta raiz contendo os dados dos pedidos cruzados com o Tiny ERP.

### 📄 Estrutura do Projeto  
```markdown
📂 conferencia-tiny-paguemenos  
 ├── main.py              # Script principal para conferência dos pedidos  
 ├── requirements.txt     # Arquivo com as dependências do projeto  
 ├── README.md            # Documentação do projeto  
 ├── .env                 # Exemplo do arquivo de configuração de credenciais  
 ├── input/               # Pasta onde deve ser inserida a planilha `Pedidos.xlsx`  
 └── output/              # Pasta onde será gerada a planilha `conferencia.xlsx`  
```

## 🧠 Conceitos Aplicados

- **Integração com API do Tiny ERP**: Consulta de status e dados da nota fiscal.  
- **Manipulação de Dados com Pandas**: Leitura, comparação e análise das planilhas.  
- **Geração de Relatórios**: Criação da planilha consolidada `conferencia.xlsx`.  
- **Automação (Futuro)**: Planejamento para preencher automaticamente os dados na plataforma PagueMenos.  

## 📄 Licença

Este projeto está sob a licença MIT.

## 🤝 Contribuições

Contribuições são bem-vindas! Caso encontre melhorias ou precise relatar problemas, sinta-se à vontade para abrir issues ou pull requests.

## 📞 Contato

- **Autor**: Leonardo Lyra  
- **GitHub**: [lyraleo23](https://github.com/lyraleo23)  
- **LinkedIn**: [Leonardo Lyra](https://www.linkedin.com/in/leonardo-lyra/)  

