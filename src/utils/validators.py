"""
Utilitários de validação para o sistema bancário.
"""

import re
from datetime import datetime


def validate_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro.
    Remove caracteres não numéricos e verifica os dígitos.
    """
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    
    if resto != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    
    if resto != int(cpf[10]):
        return False
    
    return True


def validate_email(email: str) -> bool:
    """
    Valida formato básico de email.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password: str) -> tuple:
    """
    Valida a senha.
    Requisitos: mínimo 6 caracteres, pelo menos 1 número e 1 letra.
    
    Returns:
        Tupla (senha_valida, mensagem_erro)
    """
    if len(password) < 6:
        return False, "Senha deve ter pelo menos 6 caracteres."
    
    if not re.search(r'[A-Za-z]', password):
        return False, "Senha deve conter pelo menos uma letra."
    
    if not re.search(r'[0-9]', password):
        return False, "Senha deve conter pelo menos um número."
    
    return True, ""


def validate_birth_date(date_str: str) -> tuple:
    """
    Valida data de nascimento no formato DD/MM/AAAA.
    
    Returns:
        Tupla (data_valida, mensagem_erro, is_adult)
    """
    try:
        birth = datetime.strptime(date_str, '%d/%m/%Y')
        today = datetime.now()
        
        if birth > today:
            return False, "Data não pode ser no futuro.", False
        
        age = today.year - birth.year
        if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
            age -= 1
        
        if age > 150:
            return False, "Data inválida.", False
        
        is_adult = age >= 18
        return True, "", is_adult
    
    except ValueError:
        return False, "Formato inválido. Use DD/MM/AAAA.", False


def validate_amount(amount_str: str) -> tuple:
    """
    Valida e converte string de valor monetário.
    
    Returns:
        Tupla (valor_float, mensagem_erro)
    """
    try:
        amount_str = amount_str.replace(',', '.')
        amount = float(amount_str)
        
        if amount <= 0:
            return None, "Valor deve ser positivo."
        
        if amount > 1000000:
            return None, "Valor máximo permitido: R$ 1.000.000,00"
        
        return amount, None
    
    except ValueError:
        return None, "Formato de valor inválido."