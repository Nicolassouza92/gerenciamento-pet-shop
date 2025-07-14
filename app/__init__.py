class OperacaoCancelada(Exception):
    pass

from .cadastrar_cliente import cadastrar_cliente
from .cadastrar_pet import cadastrar_pet
from .registrar_servico import registrar_servico
from .consultar_servicos import consultar_servicos
from .calcular_receita import calcular_receita