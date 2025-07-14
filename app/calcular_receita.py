from datetime import datetime
from typing import List
from ..modelos import Cliente
from . import OperacaoCancelada

def calcular_receita(clientes: List[Cliente]) -> None:
    print("\n--- Cálculo de Receita por Período ---")

    try:
        while True:
            try:
                inicio_str = input("Digite a data de início (AAAA-MM-DD) (ou 'C' para cancelar): ")
                if inicio_str.upper() == 'C': raise OperacaoCancelada
                data_inicio = datetime.strptime(inicio_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Formato de data inválido. Use AAAA-MM-DD.")

        while True:
            try:
                fim_str = input("Digite a data de fim (AAAA-MM-DD) (ou 'C' para cancelar): ")
                if fim_str.upper() == 'C': raise OperacaoCancelada
                data_fim = datetime.strptime(fim_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Formato de data inválido. Use AAAA-MM-DD.")
        
        if data_inicio > data_fim:
            print("A data de início não pode ser posterior à data de fim.")
            return

        receita_total = 0.0
        for cliente in clientes:
            for pet in cliente.pets:
                for servico in pet.servicos:
                    if data_inicio <= servico.data <= data_fim:
                        receita_total += servico.valor
        
        print(f"\nA receita total no período de {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')} foi de R$ {receita_total:.2f}")

    except OperacaoCancelada:
        raise