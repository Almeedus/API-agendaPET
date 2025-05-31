import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class Medicamento:
    def __init__(self, nome):
        self.nome = nome

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO medicamentos (nome)
                VALUES (?)
            """,
            (self.nome,)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_medicamento, nome=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if nome is not None:
            campos.append("nome = ?")
            valores.append(nome)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE medicamentos
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_medicamento)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM medicamentos
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
                SELECT * FROM medicamentos
                WHERE ID = ?
            """,
            (ID,)
        )
        medicamento = cursor.fetchone()
        cursor.close()
        return medicamento
