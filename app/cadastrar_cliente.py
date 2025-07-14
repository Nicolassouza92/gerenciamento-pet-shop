from typing import List
from modelos import Cliente
from app import OperacaoCancelada

def cadastrar_cliente(clientes: List[Cliente]) -> None:
    print("\n--- Cadastro de Novo Cliente ---")
    try:
        while True:
            nome = input("Digite o nome do cliente (ou 'C' para cancelar): ")
            if nome.upper() == 'C':
                raise OperacaoCancelada
            if nome.strip():
                break
            else:
                print("Nome inválido. Por favor, digite um nome.")

        while True:
            celular = input("Digite o celular no formato (XX) XXXXX-XXXX (ou 'C' para cancelar): ")
            if celular.upper() == 'C':
                raise OperacaoCancelada
            if len(celular) == 15 and celular[0] == '(' and celular[3] == ')' and celular[4] == ' ' and celular[10] == '-':
                break
            else:
                print("Formato de celular inválido. Use (XX) XXXXX-XXXX.")

        while True:
            email = input("Digite o email do cliente (ou 'C' para cancelar): ")
            if email.upper() == 'C':
                raise OperacaoCancelada
            if '@' in email and '.' in email:
                break
            else:
                print("Email inválido. Deve conter '@' e '.'.")

        novo_cliente = Cliente(nome=nome, celular=celular, email=email)
        clientes.append(novo_cliente)
        print(f"\nCliente '{nome}' cadastrado com sucesso!")

    except OperacaoCancelada:
        raise