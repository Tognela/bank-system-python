from datetime import datetime
from typing import List


class Transaction:
    """
    Representa uma única movimentação na conta.
    """
    
    def __init__(self, amount: float, transaction_type: str, description: str = ""):
        self.amount = amount
        self.type = transaction_type
        self.description = description
        self.timestamp = datetime.now()
    
    def __str__(self) -> str:
        date_str = self.timestamp.strftime('%d/%m/%Y %H:%M:%S')
        desc = f" - {self.description}" if self.description else ""
        return f"{date_str} | {self.type.upper():12} | R$ {self.amount:>10.2f}{desc}"


class Account:
    """
    Representa uma conta bancária.
    """
    
    def __init__(self, user_email: str, password: str, name: str, cpf: str, birth_date: str):
        self.user_email = user_email
        self.password = password
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date
        self.balance: float = 0.0
        self.transactions: List[Transaction] = []
        self.loan_balance: float = 0.0
    
    def __str__(self) -> str:
        return f"Conta de {self.name} | Saldo: R$ {self.balance:.2f}"
    
    def to_dict(self) -> dict:
        return {
            "user_email": self.user_email,
            "password": self.password,
            "name": self.name,
            "cpf": self.cpf,
            "birth_date": self.birth_date,
            "balance": self.balance,
            "loan_balance": self.loan_balance,
            "transactions_count": len(self.transactions)
        }
    
    def is_adult(self) -> bool:
        """Verifica se o titular é maior de 18 anos."""
        birth = datetime.strptime(self.birth_date, '%d/%m/%Y')
        today = datetime.now()
        age = today.year - birth.year
        
        if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
            age -= 1
        
        return age >= 18