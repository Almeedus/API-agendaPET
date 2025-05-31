import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class HistoricoConsulta:
    def __init__(self, data_consulta, hora_consulta):
        self.data_consulta = data_consulta
        self.hora_consulta = hora_consulta

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO historico_consulta (data_consulta, hora_consulta)
                VALUES (?, ?)
            """,
            (self.data_consulta, self.hora_consulta)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_consulta, data_consulta=None, hora_consulta=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if data_consulta is not None:
            campos.append("data_consulta = ?")
            valores.append(data_consulta)

        if hora_consulta is not None:
            campos.append("hora_consulta = ?")
            valores.append(hora_consulta)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE historico_consulta
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_consulta)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM historico_consulta
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
                SELECT * FROM historico_consulta
                WHERE ID = ?
            """,
            (ID,)
        )
        consulta = cursor.fetchone()
        cursor.close()
        return consulta
