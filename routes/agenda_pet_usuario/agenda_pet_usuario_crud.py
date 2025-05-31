import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class AgendaPetUsuario:
    def __init__(self, idagenda, idpet_usuario):
        self.idagenda = idagenda
        self.idpet_usuario = idpet_usuario

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO agenda_pet_usuario (idagenda, idpet_usuario) 
                VALUES (?, ?)
            """,
            (self.idagenda, self.idpet_usuario)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, ID, idagenda=None, idpet_usuario=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if idagenda is not None:
            campos.append("idagenda = ?")
            valores.append(idagenda)

        if idpet_usuario is not None:
            campos.append("idpet_usuario = ?")
            valores.append(idpet_usuario)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE agenda_pet_usuario
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(ID)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM agenda_pet_usuario 
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
                SELECT * FROM agenda_pet_usuario 
                WHERE ID = ?
            """,
            (ID,)
        )
        registro = cursor.fetchone()
        cursor.close()
        return registro
