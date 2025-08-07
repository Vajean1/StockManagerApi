# StockManagerApi ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

Uma API RESTful moderna e eficiente para gerenciamento de estoques, construída com **FastAPI** e **SQLAlchemy**.

---

## 📋 Sobre o Projeto

O **StockManagerApi** é uma solução de código aberto projetada para simplificar o gerenciamento de estoques. Ele oferece uma interface de API intuitiva que permite:

- **Gerenciar categorias**: Organize produtos em categorias personalizadas.
- **Controlar produtos**: Adicione, edite e consulte produtos com informações detalhadas.
- **Monitorar estoques**: Registre entradas e saídas para manter o inventário atualizado.
- **Gerar relatórios**: Visualize o status do estoque em tempo real.

---

## ✨ Funcionalidades

- **API RESTful**: Endpoints bem definidos para CRUD (criação, leitura, atualização e exclusão).
- **Validação de dados**: Uso de **Pydantic** para garantir entradas consistentes.
- **Documentação interativa**: Disponível via **Swagger UI**.
- **Docker**: Utilizado para conteinerização e facilitar a execução da aplicação em qualquer ambiente.
- **Banco de dados leve**: Utiliza **SQLite** para configuração simples, com suporte a outros bancos via **SQLAlchemy**.
- **Escalabilidade**: Arquitetura modular para facilitar expansões futuras.

---

## 🚀 Tecnologias Utilizadas

- ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) **FastAPI**: Framework de alta performance para APIs.
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge) **SQLAlchemy**: ORM robusto para banco de dados.
- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) **SQLite**: Banco leve e embarcado.
- ![Pydantic](https://img.shields.io/badge/Pydantic-FF0000?style=for-the-badge) **Pydantic**: Validação e serialização de dados.
- ![Uvicorn](https://img.shields.io/badge/Uvicorn-FF6F00?style=for-the-badge) **Uvicorn**: Servidor ASGI para execução da API.
- ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) **Docker**: Padronização e deploy facilitado da aplicação.

---

## 📂 Estrutura do Projeto

A organização do código é clara e modular:

```
StockManagerApi/
├── controller/          # Lógica de negócios e acesso ao banco
│   └── controller.py
├── database/            # Configuração e conexão com o banco
│   └── database.py
├── models/              # Definições dos modelos de dados
│   └── models.py
├── routes/              # Rotas da API (endpoints)
│   ├── categories.py
│   ├── products.py
│   └── stockMovement.py
├── schemas/             # Esquemas para validação de entrada/saída
│   └── schemas.py
├── main.py
├── DockerFile
├── docker-compose.yml 
└── requirements.txt     # Lista de dependências
