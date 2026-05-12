from src.models.account import Account, Transaction
from src.utils.storage import StorageManager


class BankingService:
    """
    Serviço central do banco.
    """
    
    def __init__(self):
        self.storage = StorageManager()
        self._accounts = self.storage.load_accounts()
    
    def create_account(self, name: str, cpf: str, email: str, password: str, birth_date: str):
        """
        Cria uma nova conta bancária.
        """
        if email in self._accounts:
            print(f"Erro: Já existe uma conta com o email {email}.")
            return None
        
        new_account = Account(email, password, name, cpf, birth_date)
        
        if not new_account.is_adult():
            print("Erro: É necessário ser maior de 18 anos para criar uma conta.")
            return None
        
        self._accounts[email] = new_account
        
        print(f"Conta criada com sucesso para {name}!")
        print(f"   Seu identificador é: {email}")
        return new_account
    
    def authenticate(self, email: str, password: str):
        """
        Autentica um usuário por email e senha.
        Retorna a conta se autenticado, None caso contrário.
        """
        account = self._accounts.get(email)
        if account is None:
            print("Erro: Email não encontrado.")
            return None
        
        if account.password != password:
            print("Erro: Senha incorreta.")
            return None
        
        return account
    
    def deposit(self, email: str, amount: float) -> bool:
        """Realiza um depósito."""
        if amount <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return False
        
        account = self._accounts.get(email)
        if account is None:
            print(f"Erro: Conta não encontrada.")
            return False
        
        account.balance += amount
        transaction = Transaction(amount, 'deposit', 'Depósito em conta')
        account.transactions.append(transaction)
        
        print(f"Depósito de R$ {amount:.2f} realizado com sucesso!")
        return True
    
    def withdraw(self, email: str, amount: float) -> bool:
        """Realiza um saque."""
        if amount <= 0:
            print("Erro: O valor do saque deve ser positivo.")
            return False
        
        account = self._accounts.get(email)
        if account is None:
            print(f"Erro: Conta não encontrada.")
            return False
        
        if amount > account.balance:
            print(f"Erro: Saldo insuficiente. Saldo atual: R$ {account.balance:.2f}")
            return False
        
        account.balance -= amount
        transaction = Transaction(amount, 'withdraw', 'Saque em conta')
        account.transactions.append(transaction)
        
        print(f"Saque de R$ {amount:.2f} realizado com sucesso!")
        return True
    
    def transfer(self, from_email: str, to_email: str, amount: float) -> bool:
        """
        Realiza uma transferência entre contas.
        """
        if amount <= 0:
            print("Erro: O valor da transferência deve ser positivo.")
            return False
        
        if from_email == to_email:
            print("Erro: Não é possível transferir para a mesma conta.")
            return False
        
        from_account = self._accounts.get(from_email)
        if from_account is None:
            print("Erro: Conta de origem não encontrada.")
            return False
        
        to_account = self._accounts.get(to_email)
        if to_account is None:
            print("Erro: Conta de destino não encontrada.")
            return False
        
        if amount > from_account.balance:
            print(f"Erro: Saldo insuficiente. Saldo atual: R$ {from_account.balance:.2f}")
            return False
        
        from_account.balance -= amount
        to_account.balance += amount
        
        from_transaction = Transaction(amount, 'transfer_out', f'Transferência para {to_email}')
        to_transaction = Transaction(amount, 'transfer_in', f'Transferência de {from_email}')
        
        from_account.transactions.append(from_transaction)
        to_account.transactions.append(to_transaction)
        
        print(f"Transferência de R$ {amount:.2f} realizada com sucesso!")
        print(f"De: {from_email}")
        print(f"Para: {to_email}")
        return True
    
    def request_loan(self, email: str, amount: float) -> bool:
        """
        Simula um empréstimo.
        Regras: valor máximo de R$ 10.000,00 e não pode ter outro empréstimo ativo.
        """
        if amount <= 0:
            print("Erro: O valor do empréstimo deve ser positivo.")
            return False
        
        account = self._accounts.get(email)
        if account is None:
            print("Erro: Conta não encontrada.")
            return False
        
        if account.loan_balance > 0:
            print(f"Erro: Você já possui um empréstimo ativo de R$ {account.loan_balance:.2f}.")
            print("Quite seu empréstimo antes de solicitar um novo.")
            return False
        
        if amount > 10000:
            print("Erro: Valor máximo de empréstimo é R$ 10.000,00.")
            return False
        
        account.balance += amount
        account.loan_balance = amount
        
        transaction = Transaction(amount, 'loan', 'Empréstimo concedido')
        account.transactions.append(transaction)
        
        print(f"Empréstimo de R$ {amount:.2f} concedido com sucesso!")
        print(f"Taxa de juros: 5% ao mês")
        print(f"Valor a pagar: R$ {amount * 1.05:.2f}")
        return True
    
    def pay_loan(self, email: str, amount: float) -> bool:
        """Paga parcial ou totalmente o empréstimo."""
        account = self._accounts.get(email)
        if account is None:
            print("Erro: Conta não encontrada.")
            return False
        
        if account.loan_balance <= 0:
            print("Você não possui empréstimos ativos.")
            return False
        
        if amount > account.balance:
            print(f"Erro: Saldo insuficiente. Saldo atual: R$ {account.balance:.2f}")
            return False
        
        if amount > account.loan_balance:
            amount = account.loan_balance
        
        account.balance -= amount
        account.loan_balance -= amount
        
        transaction = Transaction(amount, 'loan_payment', 'Pagamento de empréstimo')
        account.transactions.append(transaction)
        
        print(f"Pagamento de R$ {amount:.2f} realizado com sucesso!")
        if account.loan_balance > 0:
            print(f"Saldo devedor restante: R$ {account.loan_balance:.2f}")
        else:
            print("Empréstimo quitado! Parabéns!")
        
        return True
    
    def get_balance(self, email: str):
        """Consulta o saldo."""
        account = self._accounts.get(email)
        if account is None:
            print(f"Erro: Conta não encontrada.")
            return None
        return account.balance
    
    def get_loan_balance(self, email: str):
        """Consulta o saldo do empréstimo."""
        account = self._accounts.get(email)
        if account is None:
            print(f"Erro: Conta não encontrada.")
            return None
        return account.loan_balance
    
    def print_statement(self, email: str):
        """Exibe o extrato formatado."""
        account = self._accounts.get(email)
        if account is None:
            print(f"Erro: Conta não encontrada.")
            return
        
        print("\n" + "=" * 50)
        print("            EXTRATO BANCÁRIO")
        print("=" * 50)
        print(f"Cliente: {account.name}")
        print(f"Conta: {email}")
        print(f"Saldo: R$ {account.balance:.2f}")
        if account.loan_balance > 0:
            print(f"Empréstimo: R$ {account.loan_balance:.2f}")
        print("-" * 50)
        
        if not account.transactions:
            print("Nenhuma transação realizada.")
        else:
            for transaction in account.transactions:
                print(transaction)
        
        print("=" * 50 + "\n")
    
    def save_data(self):
        """Salva os dados."""
        self.storage.save_accounts(self._accounts)
    
    def get_all_emails(self):
        """Retorna emails cadastrados."""
        return list(self._accounts.keys())