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
- ✅ Criar conta via POST
- ✅ Autenticação via POST
- ✅ Consultar saldo via GET
- ✅ Depósito e saque via POST
- ✅ Transferência via POST
- ✅ Empréstimo via POST
- ✅ Extrato via GET
- ✅ Documentação automática com Swagger

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
```bash
git clone https://github.com/Tognela/bank-system-python.git
cd bank-system-python
python main.py

### VERSÃO API REST

pip install fastapi uvicorn
python api.py

-> Acesse a documentação em: http://localhost:8000/docs <-

|| -> 📚 Endpoints da API <- ||

Método	  ||    Rota	      ||       Descrição
POST	        // contas	         // Criar nova conta
POST	        // login	         // Autenticar usuário
GET	          // saldo	         // Consultar saldo
POST        	// deposito	       // Realizar depósito
POST	        // saque	         // Realizar saque
POST	        // transferencia   // Transferir entre contas
POST	        // emprestimo	     // Solicitar empréstimo
GET	          // extrato         // Consultar extrato

|| -> 🛠️ Tecnologias <- ||

|| Python 3

|| FastAPI

|| Git/GitHub

|| JSON

|| Uvicorn

|| -> 💡 Aprendizados <- ||

-> Estrutura profissional de projeto

-> Programação orientada a objetos

-> Separação de responsabilidades

-> Validação de dados reais

-> Persistência em arquivo

-> Versionamento com Git

-> API REST com FastAPI

-> Documentação Swagger

|| -> 🔜 Próximos Passos <- ||

-> Substituir JSON por PostgreSQL

-> Deploy na nuvem (Railway/Render)

-> Autenticação com JWT

-> Testes automatizados com pytest

-> Container Docker

|| -> 👤 Autor <- ||

-> Gustavo Tognela

-> GitHub: Tognela

-> Email: gustavo.tognella@gmail.com

|| -> Projeto em constante evolução como parte da jornada de aprendizado em Engenharia de Software.||

