import json
from typing import List
from modelos import Cliente

NOME_ARQUIVO_DADOS = "dados_petshop.json"

def carregar_dados() -> List[Cliente]:

    try:
        with open(NOME_ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
            clientes = [Cliente.from_json_dict(cli_data) for cli_data in dados_json]
            return clientes
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON: {NOME_ARQUIVO_DADOS}. Retornando lista vazia.")
        return []

def salvar_dados(clientes: List[Cliente]) -> None:
    lista_clientes_json = [cliente.to_json() for cliente in clientes]
    
    with open(NOME_ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(lista_clientes_json, f, indent=4, ensure_ascii=False)