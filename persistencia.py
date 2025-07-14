import json
from typing import List, Dict, Any
from .modelos import Cliente # Importa a classe Cliente de modelos.py

NOME_ARQUIVO_DADOS = "dados_petshop.json" # Definindo como uma constante

def carregar_dados() -> List[Cliente]:

    try:
        with open(NOME_ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
            clientes = [Cliente.from_json_dict(cli_data) for cli_data in dados_json]
            return clientes
    except FileNotFoundError:
        return [] # Se o arquivo não existe, retorna lista vazia
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON: {NOME_ARQUIVO_DADOS}. Retornando lista vazia.")
        return [] # Se houver erro na decodificação, também retorna lista vazia

def salvar_dados(clientes: List[Cliente]) -> None:
    # Convertendo a lista de objetos Cliente para uma lista de dicionários
    lista_clientes_json = [cliente.to_json() for cliente in clientes]
    
    with open(NOME_ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(lista_clientes_json, f, indent=4, ensure_ascii=False)
        # indent=4 para formatação bonita do JSON
        # ensure_ascii=False para permitir caracteres acentuados diretamente no JSON