import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db")

class Usuario:
    def __init__(self, nome, sobrenome, email, senha, descricao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.descricao = descricao

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO usuario (nome, sobrenome, email, senha, descricao) 
                VALUES (?, ?, ?, ?, ?)
            """,
            (self.nome, self.sobrenome, self.email, self.senha, self.descricao)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_usuario, nome=None, sobrenome=None, email=None, senha=None, descricao=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if nome is not None:
            campos.append("nome = ?")
            valores.append(nome)

        if sobrenome is not None:
            campos.append("sobrenome = ?")
            valores.append(sobrenome)

        if email is not None:
            campos.append("email = ?")
            valores.append(email)

        if senha is not None:
            campos.append("senha = ?")
            valores.append(senha)

        if descricao is not None:
            campos.append("descricao = ?")
            valores.append(descricao)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE usuario
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_usuario)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()


    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM usuario 
                WHERE ID = ?
            """,
            (ID,)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def get_by_id(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                SELECT * FROM usuario 
                WHERE ID = ?
            """,
            (ID,)
        )
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
