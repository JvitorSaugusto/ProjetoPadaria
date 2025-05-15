# Projeto Padaria — Sistema de Relatórios com MySQL e Python

Este projeto tem como objetivo fornecer uma solução simples e funcional para o gerenciamento de produtos e geração de relatórios em uma padaria. Utiliza Python com conexão a banco de dados MySQL, além da criação de relatórios em PDF e Excel.

---

## Tecnologias utilizadas

- **Python 3.11+**
- **MySQL**
- **reportlab** (geração de relatórios em PDF)
- **openpyxl** (geração de relatórios em Excel)
- **mysql-connector-python**
- Bibliotecas padrão como: `pathlib`, `datetime`, `os`, entre outras

---

## Estrutura do Projeto

```
 modelagem_dados/
├── modelo_conceitual.png        # Diagrama Entidade-Relacionamento (DER)
├── modelo_logico.png            # Diagrama lógico com tipos e relacionamentos
└── modelo_fisico.sql            # Script SQL para criação do banco de dados

 prototipo_access/
└── prototipo_padaria.accdb      # Protótipo funcional da primeira versão (em Microsoft Access)

 relatorios_pdf/
└── ...                          # Relatórios gerados em PDF

 relatorios_xlsx/
└── ...                          # Relatórios gerados em Excel

 src/
├── db_config.py                 # Configuração da conexão MySQL
├── functions.py                 # Funções utilitárias
├── product.py                   # Classe com métodos de manipulação de produtos
├── relatorio_pdf.py            # Geração de relatórios em PDF
└── relatorio_xlsx.py           # Geração de relatórios em Excel
```

---

## Funcionalidades principais

### Manipulação de Produtos (`Product`)
- `add_product()` — Insere um novo produto no banco
- `remove_product(nome)` — Remove um produto pelo nome
- `update_price(nome, novo_preco)` — Atualiza o preço de um produto específico

### Geração de Relatórios
- `create_full_report_pdf(table)` — Gera relatório PDF de qualquer tabela (formato A4 paisagem)
- `create_full_report_xlsx(table)` — Gera relatório `.xlsx` de qualquer tabela
- `create_custom_report_pdf(query, name)` — Gera PDF com base em uma `consulta SQL personalizada`
- `create_custom_report_xlsx(query, name)` — Gera `.xlsx` com base em `consulta SQL personalizada`

### Utilitários (`functions.py`)
- `select_table(table)` — Exibe todos os registros da tabela
- `list_itens(item, table_name=None)` — Lista tabelas do banco ou colunas de uma tabela
- `verify_is_str(valor)` — Verifica se um valor é string e remove espaços desnecessários
- `validate_query(query)` — Impede comandos perigosos (como `DROP`, `DELETE`, etc.) nas consultas SQL

---

## Como executar

1. Instale as dependências:
```bash
pip install reportlab openpyxl mysql-connector-python
```
ou

```bash
pip install -r requirements.txt
```

2. Ajuste o arquivo `db_config.py` com suas credenciais de acesso ao banco de dados MySQL.

3. Certifique-se de ter o banco de dados com as tabelas esperadas. O script de criação está disponível em:
```
modelagem_dados/modelo_fisico.sql
```

4. Execute os scripts principais para gerar relatórios ou manipular os dados.

---

##  Modelagem de Dados

A modelagem de dados passou por todas as etapas essenciais:

- **Modelo Conceitual**: `modelo_conceitual.png`
- **Modelo Lógico**: `modelo_logico.png`
- **Modelo Físico**: `modelo_fisico.sql`

---

##  Protótipo Access

A primeira versão deste projeto foi um protótipo funcional feito no Microsoft Access. Ele permitia testar a estrutura e as relações entre as tabelas antes da migração para MySQL e Python.

Arquivo: `prototipo_access/prototipo_padaria.accdb`

---

##  Relatórios Gerados

Os relatórios são salvos automaticamente em:

-  `relatorios_pdf/` — Relatórios em PDF
-  `relatorios_xlsx/` — Relatórios em Excel (.xlsx)

---

## Objetivo do Projeto

Este projeto foi desenvolvido com foco **educacional** e tem como principais objetivos:

- Consolidar conhecimentos em **integração Python + MySQL**
- Automatizar a **geração de relatórios** em múltiplos formatos
- Aplicar boas práticas em organização de código, segurança e manipulação de dados

---

> O projeto é uma evolução do meu **trabalho final no curso de Administração de Sistemas de Banco de Dados — Firjan SENAI Resende**, no qual fui responsável por todo o processo de modelagem, desde o modelo conceitual até a implementação física. A primeira versão foi um protótipo funcional desenvolvido em Microsoft Access.

> Estou muito satisfeito em ver essa ideia, criada do zero, ganhando forma com Python. Pretendo continuar aprimorando e adicionando novas funcionalidades nas próximas versões.

---

## Autor

**João Vitor Santos Augusto**  
🔗 [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-vitor-santos-augusto-784128224/)