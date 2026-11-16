from datetime import datetime

class Usuario:

    def __init__(
        self, 
        id_usuario = 0,
        nome = "",
        id_perfil = 0,
        data_cadastro = None,
        email = "",
        senha = ""):

        # Data do cadastro do usuário.
        self.data_cadastro = data_cadastro

        # Código identificador do usuário.
        self.id_usuario = id_usuario

        # Código do perfil do usuário.
        self.id_perfil = id_perfil
        
        # Nome completo do usuário.
        self.nome = nome
        
        # E-mail utilizado para login.
        self.email = email
        
        # Senha do usuário.
        self.senha = senha
        
        # Caso nenhuma data seja informada,
        # utiliza a data e hora atuais.
        if data_cadastro is None:
            self.data_cadastro = datetime.now()
        else:
            self.data_cadastro = data_cadastro