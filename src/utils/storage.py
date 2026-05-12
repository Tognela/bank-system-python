"""
Módulo de persistência de dados.
Salva e carrega contas bancárias usando arquivo JSON.
"""

import json
import os
from typing import Dict
from datetime import datetime
from src.models.account import Account, Transaction


class StorageManager:
    """
    Gerencia a persistência dos dados em arquivo JSON.
    """
    
    def __init__(self, filename: str = "bank_data.json"):
        self.filename = filename
    
    def save_accounts(self, accounts: Dict[str, Account]) -> bool:
        """
        Salva todas as contas em um arquivo JSON.
        """
        try:
            data = {}
            for email, account in accounts.items():
                data[email] = {
                    "user_email": account.user_email,
                    "password": account.password,
                    "name": account.name,
                    "cpf": account.cpf,
                    "birth_date": account.birth_date,
                    "balance": account.balance,
                    "loan_balance": account.loan_balance,
                    "transactions": []
                }
                for transaction in account.transactions:
                    data[email]["transactions"].append({
                        "amount": transaction.amount,
                        "type": transaction.type,
                        "description": transaction.description,
                        "timestamp": transaction.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    })
            
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            
            return True
        
        except Exception as error:
            print(f"Erro ao salvar dados: {error}")
            return False
    
    def load_accounts(self) -> Dict[str, Account]:
        """
        Carrega as contas do arquivo JSON.
        """
        accounts = {}
        
        if not os.path.exists(self.filename):
            print("Nenhum dado anterior encontrado. Iniciando sistema limpo.")
            return accounts
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for email, account_data in data.items():
                account = Account(
                    user_email=account_data["user_email"],
                    password=account_data["password"],
                    name=account_data["name"],
                    cpf=account_data["cpf"],
                    birth_date=account_data["birth_date"]
                )
                account.balance = account_data.get("balance", 0.0)
                account.loan_balance = account_data.get("loan_balance", 0.0)
                
                for trans_data in account_data.get("transactions", []):
                    transaction = Transaction(
                        trans_data["amount"],
                        trans_data["type"],
                        trans_data.get("description", "")
                    )
                    if "timestamp" in trans_data:
                        transaction.timestamp = datetime.strptime(
                            trans_data["timestamp"],
                            '%Y-%m-%d %H:%M:%S'
                        )
                    account.transactions.append(transaction)
                
                accounts[email] = account
            
            print(f"Dados carregados com sucesso! {len(accounts)} conta(s) encontrada(s).")
        
        except Exception as error:
            print(f"Erro ao carregar dados: {error}")
        
        return accounts