from datetime import datetime
from typing import List
from modelos import Cliente, Servico
from app import OperacaoCancelada    

def registrar_servico(clientes: List[Cliente]) -> None:
    print("\n--- Registro de Novo Serviço ---")

    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    print("Clientes disponíveis:")
    for i, cliente in enumerate(clientes):
        print(f"  {i}: {cliente.nome}")

    try:
        while True:
            try:
                idx_cliente_str = input("Digite o índice do cliente (ou 'C' para cancelar): ")
                if idx_cliente_str.upper() == 'C': raise OperacaoCancelada
                idx_cliente = int(idx_cliente_str)
                if 0 <= idx_cliente < len(clientes):
                    cliente_selecionado = clientes[idx_cliente]
                    break
                else: print("Índice de cliente inválido.")
            except ValueError: print("Entrada inválida. Digite um número.")
        
        if not cliente_selecionado.pets:
            print(f"O cliente {cliente_selecionado.nome} não possui pets cadastrados. Cadastre um pet primeiro.")
            return

        print(f"\nPets de {cliente_selecionado.nome}:")
        for i, pet in enumerate(cliente_selecionado.pets):
            print(f"  {i}: {pet.nome} ({pet.especie})")
        
        while True:
            try:
                idx_pet_str = input("Digite o índice do pet (ou 'C' para cancelar): ")
                if idx_pet_str.upper() == 'C': raise OperacaoCancelada
                idx_pet = int(idx_pet_str)
                if 0 <= idx_pet < len(cliente_selecionado.pets):
                    pet_selecionado = cliente_selecionado.pets[idx_pet]
                    break
                else: print("Índice de pet inválido.")
            except ValueError: print("Entrada inválida. Digite um número.")

        print(f"Pet selecionado: {pet_selecionado.nome}")

        while True:
            tipo_servico = input("Digite o tipo do serviço (ex: Banho, Tosa) (ou 'C' para cancelar): ")
            if tipo_servico.upper() == 'C': raise OperacaoCancelada
            if tipo_servico.strip(): break
            print("O tipo de serviço não pode ser vazio.")
            
        while True:
            try:
                data_str = input("Digite a data do serviço (AAAA-MM-DD) (ou 'C' para cancelar): ")
                if data_str.upper() == 'C': raise OperacaoCancelada
                data_servico = datetime.strptime(data_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Formato de data inválido. Use AAAA-MM-DD.")

        while True:
            try:
                valor_str = input("Digite o valor do serviço (ou 'C' para cancelar): ")
                if valor_str.upper() == 'C': raise OperacaoCancelada
                valor_servico = float(valor_str)
                if valor_servico > 0: break
                print("O valor deve ser um número positivo.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

        novo_servico = Servico(tipo=tipo_servico, data=data_servico, valor=valor_servico)
        pet_selecionado.servicos.append(novo_servico)

        print(f"\nServiço '{tipo_servico}' registrado para o pet '{pet_selecionado.nome}' com sucesso!")

    except OperacaoCancelada:
        raise