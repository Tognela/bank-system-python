from src.services.banking_service import BankingService
from src.utils.validators import validate_cpf, validate_email, validate_password, validate_birth_date


def show_welcome() -> None:
    """Tela inicial."""
    bank = BankingService()
    
    while True:
        print("\n" + "=" * 45)
        print("   🏦 BANK TOGNELA SYSTEM")
        print("=" * 45)
        print("1. 🔑 Acessar minha conta")
        print("2. 📝 Criar nova conta")
        print("3. 🚪 Sair")
        print("-" * 45)
        
        choice = input("Escolha uma opção: ").strip()
        
        if choice == "1":
            login_flow(bank)
        elif choice == "2":
            create_account_flow(bank)
        elif choice == "3":
            exit_program(bank)
        else:
            print("Opção inválida.")


def login_flow(bank: BankingService) -> None:
    """Login com senha."""
    print("\n--- ACESSAR CONTA ---")
    email = input("Email: ").strip().lower()
    password = input("Senha: ").strip()
    
    account = bank.authenticate(email, password)
    if account is None:
        return
    
    first_name = account.name.split()[0]
    print(f"\nBem-vindo de volta, {first_name}!")
    show_dashboard(bank, email)


def create_account_flow(bank: BankingService) -> None:
    """Criação de conta com senha e data de nascimento."""
    print("\n--- CRIAR CONTA ---")
    
    name = input("Nome completo: ").strip()
    if not name or len(name) < 3:
        print("Erro: Nome deve ter pelo menos 3 caracteres.")
        return
    
    cpf = input("CPF (apenas números): ").strip()
    if not validate_cpf(cpf):
        print("Erro: CPF inválido.")
        return
    
    birth_date = input("Data de nascimento (DD/MM/AAAA): ").strip()
    valid, msg, is_adult = validate_birth_date(birth_date)
    if not valid:
        print(f"Erro: {msg}")
        return
    
    if not is_adult:
        print("Erro: Você precisa ser maior de 18 anos para criar uma conta.")
        return
    
    email = input("Email: ").strip().lower()
    if not validate_email(email):
        print("Erro: Email inválido.")
        return
    
    print("Crie uma senha (mínimo 6 caracteres, 1 letra e 1 número):")
    password = input("Senha: ").strip()
    valid_pass, msg_pass = validate_password(password)
    if not valid_pass:
        print(f"Erro: {msg_pass}")
        return
    
    confirm_password = input("Confirme a senha: ").strip()
    if password != confirm_password:
        print("Erro: As senhas não coincidem.")
        return
    
    result = bank.create_account(name, cpf, email, password, birth_date)
    
    if result:
        first_name = name.split()[0]
        print(f"\n🎉 Bem-vindo ao Bank Tognela, {first_name}!")
        show_dashboard(bank, email)


def show_dashboard(bank: BankingService, email: str) -> None:
    """Menu principal do usuário logado."""
    while True:
        account = bank._accounts.get(email)
        
        print("\n" + "=" * 45)
        print("        MENU PRINCIPAL")
        print("=" * 45)
        print(f"👤 {account.name}")
        print(f"💰 Saldo: R$ {account.balance:.2f}")
        if account.loan_balance > 0:
            print(f"🏦 Empréstimo: R$ {account.loan_balance:.2f}")
        print("-" * 45)
        print("1. 💰 Saldo")
        print("2. 📥 Depósito")
        print("3. 📤 Saque")
        print("4. 💸 Transferência")
        print("5. 📋 Extrato")
        print("6. 🏦 Empréstimo")
        print("7. 🚪 Sair")
        print("-" * 45)
        
        choice = input("Escolha uma opção: ").strip()
        
        if choice == "1":
            balance_flow(bank, email)
        elif choice == "2":
            deposit_flow(bank, email)
        elif choice == "3":
            withdraw_flow(bank, email)
        elif choice == "4":
            transfer_flow(bank, email)
        elif choice == "5":
            statement_flow(bank, email)
        elif choice == "6":
            loan_flow(bank, email)
        elif choice == "7":
            print(f"\nAté logo, {account.name.split()[0]}! O Bank Tognela agradece!")
            bank.save_data()
            break
        else:
            print("Opção inválida.")


def deposit_flow(bank: BankingService, email: str) -> None:
    print("\n--- DEPÓSITO ---")
    try:
        amount = float(input("Valor do depósito: R$ ").replace(",", "."))
        bank.deposit(email, amount)
    except ValueError:
        print("Erro: Digite um valor numérico válido.")


def withdraw_flow(bank: BankingService, email: str) -> None:
    print("\n--- SAQUE ---")
    try:
        amount = float(input("Valor do saque: R$ ").replace(",", "."))
        bank.withdraw(email, amount)
    except ValueError:
        print("Erro: Digite um valor numérico válido.")


def transfer_flow(bank: BankingService, email: str) -> None:
    print("\n--- TRANSFERÊNCIA ---")
    to_email = input("Email do destinatário: ").strip().lower()
    try:
        amount = float(input("Valor da transferência: R$ ").replace(",", "."))
        bank.transfer(email, to_email, amount)
    except ValueError:
        print("Erro: Digite um valor numérico válido.")


def balance_flow(bank: BankingService, email: str) -> None:
    print("\n--- SALDO ---")
    balance = bank.get_balance(email)
    loan = bank.get_loan_balance(email)
    if balance is not None:
        print(f"Saldo em conta: R$ {balance:.2f}")
        if loan and loan > 0:
            print(f"Empréstimo ativo: R$ {loan:.2f}")


def statement_flow(bank: BankingService, email: str) -> None:
    print("\n--- EXTRATO ---")
    bank.print_statement(email)


def loan_flow(bank: BankingService, email: str) -> None:
    """Menu de empréstimos."""
    account = bank._accounts.get(email)
    
    print("\n--- 🏦 EMPRÉSTIMOS ---")
    
    if account.loan_balance > 0:
        print(f"Você possui um empréstimo ativo de R$ {account.loan_balance:.2f}")
        print("1. Pagar empréstimo")
        print("2. Voltar")
        choice = input("Escolha: ").strip()
        
        if choice == "1":
            try:
                amount = float(input("Valor do pagamento: R$ ").replace(",", "."))
                bank.pay_loan(email, amount)
            except ValueError:
                print("Erro: Valor inválido.")
        return
    
    print("Valor máximo: R$ 10.000,00")
    print("Taxa de juros: 5% ao mês")
    print("1. Solicitar empréstimo")
    print("2. Voltar")
    
    choice = input("Escolha: ").strip()
    
    if choice == "1":
        try:
            amount = float(input("Valor desejado: R$ ").replace(",", "."))
            bank.request_loan(email, amount)
        except ValueError:
            print("Erro: Valor inválido.")


def exit_program(bank: BankingService) -> None:
    """Encerra o programa."""
    print("\nSalvando dados...")
    bank.save_data()
    print("Obrigado por usar o Bank Tognela System!")
    print("Seus dados foram salvos com sucesso.\n")
    exit()