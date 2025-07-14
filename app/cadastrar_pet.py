from typing import List
from ..modelos import Cliente, Pet  
from . import OperacaoCancelada     

def cadastrar_pet(clientes: List[Cliente]) -> None:
    print("\n--- Cadastro de Novo Pet ---")

    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    # Lista os clientes para o usuário escolher
    print("Clientes disponíveis:")
    for i, cliente in enumerate(clientes):
        print(f"  {i}: {cliente.nome}")

    try:
        # Loop para escolher um cliente válido
        while True:
            try:
                indice_cliente_str = input("Digite o índice do cliente (ou 'C' para cancelar): ")
                if indice_cliente_str.upper() == 'C':
                    raise OperacaoCancelada
                
                indice_cliente = int(indice_cliente_str)
                if 0 <= indice_cliente < len(clientes):
                    cliente_selecionado = clientes[indice_cliente]
                    break
                else:
                    print("Índice de cliente inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        print(f"Cliente selecionado: {cliente_selecionado.nome}")

        while True:
            nome_pet = input("Digite o nome do pet (ou 'C' para cancelar): ")
            if nome_pet.upper() == 'C': raise OperacaoCancelada
            if nome_pet.strip(): break
            print("Nome do pet não pode ser vazio.")
        
        while True:
            especie = input("Digite a espécie do pet (ou 'C' para cancelar): ")
            if especie.upper() == 'C': raise OperacaoCancelada
            if especie.strip(): break
            print("Espécie não pode ser vazia.")
            
        while True:
            try:
                peso_str = input("Digite o peso do pet em kg (ou 'C' para cancelar): ")
                if peso_str.upper() == 'C': raise OperacaoCancelada
                peso = float(peso_str)
                if peso > 0: break
                print("O peso deve ser um número positivo.")
            except ValueError:
                print("Peso inválido. Por favor, digite um número.")
                
        while True:
            try:
                idade_str = input("Digite a idade do pet em anos (ou 'C' para cancelar): ")
                if idade_str.upper() == 'C': raise OperacaoCancelada
                idade = int(idade_str)
                if idade >= 0: break
                print("A idade não pode ser negativa.")
            except ValueError:
                print("Idade inválida. Por favor, digite um número inteiro.")

        # Cria e adiciona o pet ao cliente
        novo_pet = Pet(nome=nome_pet, especie=especie, peso=peso, idade=idade)
        cliente_selecionado.pets.append(novo_pet)
        
        print(f"\nPet '{nome_pet}' cadastrado para o cliente '{cliente_selecionado.nome}' com sucesso!")

    except OperacaoCancelada:
        raise