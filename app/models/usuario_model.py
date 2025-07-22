from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    nome: str
    senha: str