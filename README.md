#  Projeto Padaria — Sistema de Relatórios com MySQL e Python

Este projeto tem como objetivo fornecer uma solução simples e funcional para o gerenciamento de produtos e geração de relatórios em uma padaria. Utiliza Python com conexão a banco de dados MySQL, além da criação de relatórios em PDF e Excel.

---

##  Tecnologias utilizadas

- **Python 3.11+**
- **MySQL**
- **reportlab** (geração de relatórios em PDF)
- **openpyxl** (geração de relatórios em Excel)
- **pathlib**, **datetime**, e outras bibliotecas padrão do Python

---

##  Estrutura do Projeto

| Arquivo                  | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| `db_config.py`           | Configuração da conexão com o banco de dados MySQL                        |
| `functions.py`           | Funções auxiliares para exibir tabelas, validar strings e aplicar filtros |
| `product.py`             | Classe `Product` com métodos de CRUD (Create, Update, Delete)             |
| `relatorio_pdf.py`       | Gera relatórios em PDF no formato paisagem com dados de qualquer tabela   |
| `relatorio_xlsx.py`      | Gera relatórios em formato `.xlsx` utilizando OpenPyXL                    |

---

##  Funcionalidades principais

###  Manipulação de produtos (classe `Product`)
- `add_product()` — Insere um novo produto no banco
- `remove_product(nome)` — Remove um produto pelo nome
- `update_price(nome, novo_preco)` — Atualiza o preço de um produto específico

###  Geração de relatórios
- `create_full_report_pdf(table)` — Gera um relatório em PDF da tabela especificada, com layout paisagem (A4 Landscape), escolhido pra evitar sobreposição de informações
- `create_full_report_xlsx(table)` — Gera um relatório em Excel da tabela especificada

###  Utilitários (em `functions.py`)
- `select_table(table)` — Exibe todos os registros da tabela
- `list_itens(item, table_name=None)` — Lista tabelas do banco ou colunas específicas de uma tabela
- `verify_is_str(valor)` — Verifica se o valor é string e trata espaços extras

---

## ▶ Como executar

1. Certifique-se de ter o **MySQL Server** e um banco criado com as tabelas esperadas (`produto`, `tipo_produto`, etc.) vou disponibilizar o banco de dados para uso publico depois.
2. Instale as dependências:
```bash
pip install reportlab openpyxl mysql-connector-python
```
 ou 

 ```bash
pip install -r requirements.txt
```

3. Ajuste o arquivo `db_config.py` com suas credenciais de acesso ao banco.

## Relatórios gerados
Os relatórios são salvos automaticamente nas pastas:

relatorios_pdf/ — Arquivos .pdf

relatorios_xlsx/ — Arquivos .xlsx

##  Objetivo do Projeto

Este projeto foi desenvolvido com foco educacional e tem como principais objetivos:

- Consolidar conhecimentos em integração entre **Python** e **MySQL**
- Automatizar a **geração de relatórios** em PDF e Excel a partir do banco de dados
- Aplicar boas práticas na manipulação de arquivos e no uso de bibliotecas externas

O projeto é uma evolução do meu **trabalho final no curso de Administração de Sistemas de Banco de Dados — Firjan SENAI Resende**, no qual fui responsável por todo o processo de modelagem, desde o modelo conceitual até a implementação física. A primeira versão foi um protótipo funcional desenvolvido em Microsoft Access.

Estou muito satisfeito em ver essa ideia, criada do zero, ganhando forma com Python. Pretendo continuar aprimorando e adicionando novas funcionalidades nas próximas versões.

---

##  Autor

**João Vitor Santos Augusto**  
🔗 [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-vitor-santos-augusto-784128224/)
