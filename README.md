# Workforce CLI

Sistema de gerenciamento de pessoas desenvolvido em Python, com foco em
lógica de programação, organização de código e persistência de dados
utilizando SQLite.

O projeto simula um sistema interno simples de gestão de funcionários,
aplicando boas práticas como separação por camadas, validações e regras
de negócio.

---

##  Funcionalidades

- Cadastro de funcionários com validação de dados
- Listagem de todos os funcionários
- Listagem apenas de funcionários ativos
- Desativação lógica de funcionários (sem exclusão física)
- Relatórios de funcionários ativos e inativos
- Busca avançada por nome e/ou cargo
- Persistência de dados com SQLite
- Interface em linha de comando (CLI)

---

##  Estrutura do Projeto


- `model.py` → Modelo de dados (Funcionario)
- `database.py` → Acesso ao banco de dados (SQLite)
- `service.py` → Regras de negócio e validações
- `main.py` → Interface CLI e fluxo da aplicação

---

##  Tecnologias Utilizadas

- Python 3
- SQLite3
- SQL (CRUD, filtros e agregações)
- Programação Orientada a Objetos (POO)
- Organização por camadas

---
