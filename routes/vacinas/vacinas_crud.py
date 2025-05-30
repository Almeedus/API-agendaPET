import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class Vacina:
    def __init__(self, nome, data_vacina, tipo_vacina, observacao):
        self.nome = nome
        self.data_vacina = data_vacina
        self.tipo_vacina = tipo_vacina
        self.observacao = observacao

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO vacinas (nome, data_vacina, tipo_vacina, observacao)
                VALUES (?, ?, ?, ?)
            """,
            (self.nome, self.data_vacina, self.tipo_vacina, self.observacao)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_vacina, nome=None, data_vacina=None, tipo_vacina=None, observacao=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if nome is not None:
            campos.append("nome = ?")
            valores.append(nome)

        if data_vacina is not None:
            campos.append("data_vacina = ?")
            valores.append(data_vacina)

        if tipo_vacina is not None:
            campos.append("tipo_vacina = ?")
            valores.append(tipo_vacina)

        if observacao is not None:
            campos.append("observacao = ?")
            valores.append(observacao)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE vacinas
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_vacina)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM vacinas
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
                SELECT * FROM vacinas
                WHERE ID = ?
            """,
            (ID,)
        )
        vacina = cursor.fetchone()
        cursor.close()
        return vacina
