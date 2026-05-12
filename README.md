# 🏦 Bank System Python

Sistema bancário interativo via terminal desenvolvido como projeto de aprendizado em Engenharia de Software.

## 📋 Funcionalidades

- ✅ Criar conta com validação de CPF e email
- ✅ Depósito com registro de transação
- ✅ Saque com verificação de saldo
- ✅ Consulta de saldo
- ✅ Extrato detalhado com data/hora
- ✅ Persistência de dados em JSON
- ✅ Menu interativo via terminal

## 🏗️ Estrutura do Projeto
 
 bank-system-python/ 
  |--- main.py
  |--- README.MD
  |--- .gitignore
  |--- src/
  |--- models/
  | '--- account.py
  |--- services/
  | '--- banking_service.py
  |--- utils/
  |--- menu.py
  |--- storage.py
  |--- Validators.py

  
## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/Tognela/bank-system-python.git
cd bank-system-python

#EXECUTE O SISTEMA:
python main.py

💡 Funcionalidades Detalhadas

Criar Conta

Validação de CPF com algoritmo oficial

Validação de formato de email

Nome com no mínimo 3 caracteres

Depósito -'-

Aceita valores com vírgula ou ponto

Registra data e hora da transação

Valor máximo de R$ 1.000.000,00

Saque -'-

Verifica saldo disponível

Impede saque maior que o saldo

Registra no extrato

Extrato -'- 

Exibe todas as transações

Mostra data, hora e tipo

Saldo atualizado

Persistência -'-

Salva automaticamente ao sair

Carrega dados ao iniciar

Arquivo JSON local

🛠️ Tecnologias Utilizadas

Python 3

Git e GitHub

JSON para armazenamento

VS Code

📚 Aprendizados

Este projeto foi desenvolvido para praticar:

Estrutura profissional de projeto Python

Programação orientada a objetos

Separação de responsabilidades (Models, Services, Utils)

Validação de dados

Persistência em arquivo

Controle de versão com Git

Conventional Commits

Documentação de projeto

🔜 Próximos Passos

Substituir JSON por banco de dados SQLite

Criar API REST com FastAPI

Adicionar autenticação de usuários

Implementar transferências entre contas

Criar testes automatizados com pytest

Interface gráfica ou web

👤 Autor
[GUSTAVO TOGNELA]

Desenvolvido como parte da jornada de aprendizado em Engenharia de Software.