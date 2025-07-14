from typing import List
from modelos import Cliente
from app import OperacaoCancelada

def consultar_servicos(clientes: List[Cliente]) -> None:
    print("\n--- Consulta de Serviços ---")

    if not clientes:
        print("Nenhum cliente cadastrado.")
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
                cliente_selecionado = clientes[idx_cliente]
                break
            except (ValueError, IndexError):
                print("Índice inválido. Tente novamente.")
        
        if not cliente_selecionado.pets:
            print(f"O cliente {cliente_selecionado.nome} não possui pets cadastrados.")
            return

        print(f"\nPets de {cliente_selecionado.nome}:")
        for i, pet in enumerate(cliente_selecionado.pets):
            print(f"  {i}: {pet.nome} ({pet.especie})")
        
        while True:
            try:
                idx_pet_str = input("Digite o índice do pet (ou 'C' para cancelar): ")
                if idx_pet_str.upper() == 'C': raise OperacaoCancelada
                idx_pet = int(idx_pet_str)
                pet_selecionado = cliente_selecionado.pets[idx_pet]
                break
            except (ValueError, IndexError):
                print("Índice inválido. Tente novamente.")

        print(f"\n--- Serviços para {pet_selecionado.nome} ---")
        if not pet_selecionado.servicos:
            print("Nenhum serviço registrado para este pet.")
        else:
            for servico in pet_selecionado.servicos:
                data_formatada = servico.data.strftime("%d/%m/%Y")
                print(f"  - Tipo: {servico.tipo}, Data: {data_formatada}, Valor: R$ {servico.valor:.2f}")

    except OperacaoCancelada:
        raise