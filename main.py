import sys
from typing import List
from modelos import Cliente
import persistencia
import app

import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def mostrar_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n" + "="*20)
    print("  *** Pet Shop ***")
    print("="*20)
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Pet")
    print("3. Registrar Serviço")
    print("4. Consultar Serviços de um Pet")
    print("5. Calcular Receita por Período")
    print("6. Sair")
    print("="*20)

def main():
    """Função principal que executa o sistema do Pet Shop."""
    
    clientes: List[Cliente] = persistencia.carregar_dados()
    print(f"Dados carregados. {len(clientes)} cliente(s) no sistema.")

    while True:
        mostrar_menu()
        
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                app.cadastrar_cliente(clientes)
            elif opcao == '2':
                app.cadastrar_pet(clientes)
            elif opcao == '3':
                app.registrar_servico(clientes)
            elif opcao == '4':
                app.consultar_servicos(clientes)
            elif opcao == '5':
                app.calcular_receita(clientes)
            elif opcao == '6':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except app.OperacaoCancelada:
            print("\nOperação cancelada pelo usuário.")
        
        persistencia.salvar_dados(clientes)

if __name__ == "__main__":
    main()