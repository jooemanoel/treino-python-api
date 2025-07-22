#app/models/usuario_model.py

from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    nome: str
    senha: str

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome
        }
