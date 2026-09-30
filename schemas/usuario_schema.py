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

    # ID do usuário logado (para validação de permissão).
    # Usado apenas para verificar se tem direito de gerenciar usuários.
    # Em produção, seria extraído do token JWT.
    id_usuario_logado: int = 0

    # Perfil do usuário logado (opcional, para validação).
    id_perfil_logado: int = 0


class LoginSchema(BaseModel):
    """Schema para requisição de login."""
    email: str
    senha: str

# Observação:
# - `LoginSchema` valida os dados recebidos na rota de autenticação.
# - Usamos `email` como campo de identificação, mas o frontend aceita
#   também o valor especial 'admin' (caso de desenvolvimento).