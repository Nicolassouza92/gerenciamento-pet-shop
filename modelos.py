from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Any

@dataclass
class Servico:
    tipo: str
    data: date
    valor: float

    def to_json(self) -> Dict[str, Any]:
        return {
            "tipo": self.tipo,
            "data": self.data.isoformat(),
            "valor": self.valor
        }

    @classmethod
    def from_json_dict(cls, json_dict: Dict[str, Any]) -> 'Servico':
        return cls(
            tipo=json_dict['tipo'],
            data=date.fromisoformat(json_dict['data']),
            valor=json_dict['valor']
        )

@dataclass
class Pet:
    nome: str
    especie: str
    peso: float
    idade: int
    servicos: List[Servico] = field(default_factory=list)

    def to_json(self) -> Dict[str, Any]:
        return {
            "nome": self.nome,
            "especie": self.especie,
            "peso": self.peso,
            "idade": self.idade,
            "servicos": [s.to_json() for s in self.servicos]
        }

    @classmethod
    def from_json_dict(cls, json_dict: Dict[str, Any]) -> 'Pet':
        return cls(
            nome=json_dict['nome'],
            especie=json_dict['especie'],
            peso=json_dict['peso'],
            idade=json_dict['idade'],
            servicos=[Servico.from_json_dict(s_data) for s_data in json_dict.get('servicos', [])]
        )

@dataclass
class Cliente:
    nome: str
    celular: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def to_json(self) -> Dict[str, Any]:
        return {
            "nome": self.nome,
            "celular": self.celular,
            "email": self.email,
            "pets": [p.to_json() for p in self.pets]
        }

    @classmethod
    def from_json_dict(cls, json_dict: Dict[str, Any]) -> 'Cliente':
        return cls(
            nome=json_dict['nome'],
            celular=json_dict['celular'],
            email=json_dict['email'],
            pets=[Pet.from_json_dict(p_data) for p_data in json_dict.get('pets', [])]
        )