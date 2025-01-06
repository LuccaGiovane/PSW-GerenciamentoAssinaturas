<div align="center">
   <h1><b>Gerenciamento de Assinaturas</b></h1><br><br>

   <a href="" target="_blank">![License](https://img.shields.io/badge/license-MIT-blue.svg)</a>
   ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
   ![SQLite](https://img.shields.io/badge/SQLite-magenta.svg)

</div>

<div>
<h2>📖 Descrição</h2>
  
<a>Este projeto foi desenvolvido como parte da Pystack Week Returnal, onde o objetivo foi criar um sistema simples de gerenciamento de assinaturas utilizando Python puro e banco de dados SQLite. O sistema permite ao usuário adicionar, listar, excluir assinaturas e visualizar relatórios de gastos mensais por meio de gráficos gerados automaticamente.</a>
</div>

<div>
<h2>🎯 Funcionalidades</h2>

- Adicionar Assinatura: Cadastro de novas assinaturas, incluindo informações como empresa, site, data de assinatura e valor.
- Remover Assinatura: Exclusão de assinaturas existentes.
- Listar Assinaturas: Exibe todas as assinaturas cadastradas.
- Relatório de Gastos: Mostra o valor total gasto em assinaturas no mês atual e exibe um gráfico com os gastos dos últimos 12 meses.

</div>

<div>
<h2>⚙️ Configuração do Ambiente</h2>

  1. Crie o ambiente virtual:

```bash
# Linux
python3 -m venv venv

# Windows
python -m venv venv
```

2. Ative o ambiente virtual:

```bash
# Linux
source venv/bin/activate

# Windows
venv\Scripts\Activate

```

3. Instale as dependências:

```bash
pip install sqlmodel matplotlib
```
  
</div>

<div>
  <h2>🚀 Execução</h2>

  1. Certifique-se de que as tabelas estão criadas no banco de dados:
```bash
python models/database.py
```

2. Inicie a aplicação:
```bash
python templates/app.py
```

</div>

<div>
  <h2>✅ Requisitos</h2>
  
- Python 3.8+
- SQLModel
- Matplotlib

</div>
