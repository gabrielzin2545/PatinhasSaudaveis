# Importa o BaseModel do Pydantic.
# O FastAPI utiliza o Pydantic para validar
# os dados recebidos nas requisições.
from pydantic import BaseModel


# Cria o Schema utilizado para receber
# os dados de um usuário.
class UsuarioSchema(BaseModel):

    # id do usuario para identificação do perfil.
    cadastro: int

    # id do usuario para identificação do perfil.
    id_usuario: int

    # Nome completo do usuário.
    nome: str

    # Identificador do perfil do usuário.
    id_perfil: int

    # E-mail utilizado pelo usuário.
    email: str

    # Senha utilizada para autenticação.
    senha: str