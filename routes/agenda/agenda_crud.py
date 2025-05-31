import sqlite3

CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class Agenda:
    def __init__(self, nome, dia_atividade, hora_atividade, completado=False, observacao=None):
        self.nome = nome
        self.dia_atividade = dia_atividade
        self.hora_atividade = hora_atividade
        self.completado = completado
        self.observacao = observacao

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO agenda (nome, dia_atividade, hora_atividade, completado, observacao)
                VALUES (?, ?, ?, ?, ?)
            """,
            (self.nome, self.dia_atividade, self.hora_atividade, int(self.completado), self.observacao)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_agenda, nome=None, dia_atividade=None, hora_atividade=None, completado=None, observacao=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if nome is not None:
            campos.append("nome = ?")
            valores.append(nome)

        if dia_atividade is not None:
            campos.append("dia_atividade = ?")
            valores.append(dia_atividade)

        if hora_atividade is not None:
            campos.append("hora_atividade = ?")
            valores.append(hora_atividade)

        if completado is not None:
            campos.append("completado = ?")
            valores.append(int(completado))

        if observacao is not None:
            campos.append("observacao = ?")
            valores.append(observacao)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE agenda
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_agenda)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, id_agenda):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM agenda
                WHERE ID = ?
            """,
            (id_agenda,)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def get_by_id(self, id_agenda):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                SELECT * FROM agenda
                WHERE ID = ?
            """,
            (id_agenda,)
        )
        registro = cursor.fetchone()
        cursor.close()
        return registro

    def alternar_completado(self, id_agenda):
        cursor = CONNECTION_DB.cursor()

        # Pega o valor atual
        cursor.execute(
            """
                SELECT completado FROM agenda
                WHERE ID = ?
            """,
            (id_agenda,)
        )
        resultado = cursor.fetchone()

        if resultado is None:
            cursor.close()
            return False  # Registro não encontrado

        novo_valor = 0 if resultado[0] else 1

        cursor.execute(
            """
                UPDATE agenda
                SET completado = ?
                WHERE ID = ?
            """,
            (novo_valor, id_agenda)
        )
        CONNECTION_DB.commit()
        cursor.close()
        return True
