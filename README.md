# 🏦 Bank Tognela System

Sistema bancário completo desenvolvido como projeto de portfólio em Engenharia de Software.

## 📋 Funcionalidades

### Versão Terminal (MVP)
- ✅ Criar conta com validação de CPF, email e maioridade
- ✅ Autenticação com senha
- ✅ Depósito e saque
- ✅ Transferência entre contas
- ✅ Sistema de empréstimo com juros
- ✅ Extrato detalhado
- ✅ Persistência em JSON

### Versão API REST
- ✅ Criar conta via POST /contas
- ✅ Autenticação via POST /login
- ✅ Consultar saldo via GET /saldo
- ✅ Depósito via POST /deposito
- ✅ Saque via POST /saque
- ✅ Transferência via POST /transferencia
- ✅ Empréstimo via POST /emprestimo
- ✅ Extrato via GET /extrato
- ✅ Documentação automática com Swagger em /docs

## 🏗️ Estrutura do Projeto

bank-system-python/
├── main.py
├── api.py
├── README.md
├── .gitignore
├── requirements.txt
└── src/
    ├── models/
    │   └── account.py
    ├── services/
    │   └── banking_service.py
    └── utils/
        ├── menu.py
        ├── api_routes.py
        ├── storage.py
        └── validators.py

## 🚀 Como Executar

### Versão Terminal
git clone https://github.com/Tognela/bank-system-python.git
cd bank-system-python
python main.py

### Versão API REST
pip install fastapi uvicorn
python api.py

Acesse: http://localhost:8000/docs

## 📚 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /contas | Criar nova conta |
| POST | /login | Autenticar usuário |
| GET | /saldo | Consultar saldo |
| POST | /deposito | Realizar depósito |
| POST | /saque | Realizar saque |
| POST | /transferencia | Transferir entre contas |
| POST | /emprestimo | Solicitar empréstimo |
| GET | /extrato | Consultar extrato |

## 🛠️ Tecnologias Utilizadas

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Git e GitHub
- JSON para armazenamento
- VS Code

## 💡 Aprendizados

- Estrutura profissional de projeto Python
- Programação orientada a objetos
- Separação de responsabilidades (Models, Services, Utils)
- Validação de dados reais (CPF, email, idade)
- Persistência em arquivo JSON
- Controle de versão com Git e Conventional Commits
- API REST com FastAPI
- Documentação automática com Swagger

## 🔜 Próximos Passos

- Substituir JSON por banco de dados PostgreSQL
- Autenticação com JWT
- Deploy na nuvem (Railway/Render)
- Testes automatizados com pytest
- Container Docker

## 👤 Autor

Gustavo Tognela
- GitHub: Tognela (https://github.com/Tognela)
- Email: gustavo.tognella@gmail.com

---

Projeto em constante evolução como parte da jornada de aprendizado em Engenharia de Software.