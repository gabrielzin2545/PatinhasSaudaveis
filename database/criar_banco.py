# Importa a classe responsável pela conexão com o banco.
from database.conexao import Conexao


# Classe responsável pela criação do banco
# e das tabelas do sistema.
class CriarBanco:

    # Método estático.
    # Pode ser executado sem criar um objeto da classe.
    @staticmethod
    def criar():

        # Abre uma conexão com o banco SQLite.
        #
        # Caso o arquivo saidinha.db não exista,
        # o SQLite irá criá-lo automaticamente.
        conexao = Conexao.conectar()

        # Cria um cursor para executar comandos SQL.
        cursor = conexao.cursor()

        # Cria a tabela PERFIL caso ela ainda não exista.
        cursor.execute("""

        CREATE TABLE IF NOT EXISTS perfil (
            id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
            ds_perfil TEXT NOT NULL
        )
        """)

        # Cria a tabela USUARIO caso ela ainda não exista.
        cursor.execute("""

        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            id_perfil INTEGER NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            data_cadastro TEXT NOT NULL,
            FOREIGN KEY(id_perfil)
                REFERENCES perfil(id_perfil)
        )
        """)

        # ============================================================
        # INSERIR PERFIS PADRÕES
        # ============================================================

        # Verifica se já existem perfis cadastrados
        cursor.execute("SELECT COUNT(*) FROM perfil")
        count_perfis = cursor.fetchone()[0]

        # Se não houver perfis, insere os padrões do sistema
        if count_perfis == 0:

            # Insere o perfil de Aluno (ID = 1)
            cursor.execute(
                "INSERT INTO perfil (id_perfil, ds_perfil) VALUES (1, ?)",
                ("Cliente",)
            )

            # Insere o perfil de Professor (ID = 2)
            cursor.execute(
                "INSERT INTO perfil (id_perfil, ds_perfil) VALUES (2, ?)",
                ("Dono de Pet",)
            )

            # Insere o perfil de Equipe de Apoio (ID = 3)
            cursor.execute(
                "INSERT INTO perfil (id_perfil, ds_perfil) VALUES (3, ?)",
                ("Equipe de Apoio",)
            )

        # Confirma as alterações realizadas no banco.
        conexao.commit()

        # Fecha a conexão com o banco.
        conexao.close()


# Executa o método responsável por criar
# o banco de dados e suas tabelas.
CriarBanco.criar()