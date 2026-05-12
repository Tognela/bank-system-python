from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.banking_service import BankingService
from src.utils.validators import validate_cpf, validate_email, validate_password, validate_birth_date

router = APIRouter()
bank = BankingService()


class CreateAccountRequest(BaseModel):
    name: str
    cpf: str
    birth_date: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class AmountRequest(BaseModel):
    email: str
    amount: float


class TransferRequest(BaseModel):
    from_email: str
    to_email: str
    amount: float


class EmailRequest(BaseModel):
    email: str


@router.post("/contas")
def criar_conta(data: CreateAccountRequest):
    if not data.name or len(data.name) < 3:
        raise HTTPException(status_code=400, detail="Nome deve ter pelo menos 3 caracteres")
    
    if not validate_cpf(data.cpf):
        raise HTTPException(status_code=400, detail="CPF invalido")
    
    valid, msg, is_adult = validate_birth_date(data.birth_date)
    if not valid:
        raise HTTPException(status_code=400, detail=msg)
    if not is_adult:
        raise HTTPException(status_code=400, detail="E necessario ser maior de 18 anos")
    
    if not validate_email(data.email):
        raise HTTPException(status_code=400, detail="Email invalido")
    
    valid_pass, msg_pass = validate_password(data.password)
    if not valid_pass:
        raise HTTPException(status_code=400, detail=msg_pass)
    
    result = bank.create_account(data.name, data.cpf, data.email, data.password, data.birth_date)
    
    if result is None:
        raise HTTPException(status_code=400, detail="Email ja cadastrado")
    
    bank.save_data()
    
    return {
        "status": "success",
        "message": f"Conta criada com sucesso para {data.name}",
        "email": data.email
    }


@router.post("/login")
def login(data: LoginRequest):
    account = bank.authenticate(data.email, data.password)
    
    if account is None:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    return {
        "status": "success",
        "message": f"Bem-vindo, {account.name}",
        "email": data.email,
        "name": account.name
    }


@router.post("/deposito")
def depositar(data: AmountRequest):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser positivo")
    
    success = bank.deposit(data.email, data.amount)
    
    if not success:
        raise HTTPException(status_code=404, detail="Conta nao encontrada")
    
    bank.save_data()
    
    return {
        "status": "success",
        "message": f"Deposito de R$ {data.amount:.2f} realizado",
        "balance": bank.get_balance(data.email)
    }


@router.post("/saque")
def sacar(data: AmountRequest):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser positivo")
    
    success = bank.withdraw(data.email, data.amount)
    
    if not success:
        raise HTTPException(status_code=400, detail="Saldo insuficiente ou conta nao encontrada")
    
    bank.save_data()
    
    return {
        "status": "success",
        "message": f"Saque de R$ {data.amount:.2f} realizado",
        "balance": bank.get_balance(data.email)
    }


@router.post("/transferencia")
def transferir(data: TransferRequest):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser positivo")
    
    if data.from_email == data.to_email:
        raise HTTPException(status_code=400, detail="Nao e possivel transferir para a mesma conta")
    
    success = bank.transfer(data.from_email, data.to_email, data.amount)
    
    if not success:
        raise HTTPException(status_code=400, detail="Transferencia falhou. Verifique os dados")
    
    bank.save_data()
    
    return {
        "status": "success",
        "message": f"Transferencia de R$ {data.amount:.2f} realizada",
        "from_balance": bank.get_balance(data.from_email),
        "to_balance": bank.get_balance(data.to_email)
    }


@router.post("/emprestimo")
def solicitar_emprestimo(data: AmountRequest):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser positivo")
    
    success = bank.request_loan(data.email, data.amount)
    
    if not success:
        raise HTTPException(status_code=400, detail="Emprestimo recusado")
    
    bank.save_data()
    
    return {
        "status": "success",
        "message": f"Emprestimo de R$ {data.amount:.2f} concedido",
        "balance": bank.get_balance(data.email),
        "loan_balance": bank.get_loan_balance(data.email)
    }


@router.get("/saldo")
def consultar_saldo(email: str):
    balance = bank.get_balance(email)
    
    if balance is None:
        raise HTTPException(status_code=404, detail="Conta nao encontrada")
    
    loan = bank.get_loan_balance(email)
    
    return {
        "status": "success",
        "email": email,
        "balance": balance,
        "loan_balance": loan
    }


@router.get("/extrato")
def consultar_extrato(email: str):
    account = bank._accounts.get(email)
    
    if account is None:
        raise HTTPException(status_code=404, detail="Conta nao encontrada")
    
    transactions = []
    for t in account.transactions:
        transactions.append({
            "date": t.timestamp.strftime('%d/%m/%Y %H:%M:%S'),
            "type": t.type,
            "amount": t.amount,
            "description": t.description
        })
    
    return {
        "status": "success",
        "email": email,
        "name": account.name,
        "balance": account.balance,
        "loan_balance": account.loan_balance,
        "transactions": transactions
    }


@router.get("/")
def root():
    return {
        "app": "Bank Tognela API",
        "version": "1.0",
        "docs": "/docs",
        "endpoints": [
            "POST /contas",
            "POST /login",
            "GET /saldo?email=",
            "POST /deposito",
            "POST /saque",
            "POST /transferencia",
            "POST /emprestimo",
            "GET /extrato?email="
        ]
    }