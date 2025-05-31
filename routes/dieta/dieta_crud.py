import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class Dieta:
    def __init__(self, nome_refeicao, hora_refeicao, alimentado):
        self.nome_refeicao = nome_refeicao
        self.hora_refeicao = hora_refeicao
        self.alimentado = alimentado

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO dieta (nome_refeicao, hora_refeicao, alimentado) 
                VALUES (?, ?, ?)
            """,
            (self.nome_refeicao, self.hora_refeicao, self.alimentado)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_dieta, nome_refeicao=None, hora_refeicao=None, alimentado=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if nome_refeicao is not None:
            campos.append("nome_refeicao = ?")
            valores.append(nome_refeicao)

        if hora_refeicao is not None:
            campos.append("hora_refeicao = ?")
            valores.append(hora_refeicao)

        if alimentado is not None:
            campos.append("alimentado = ?")
            valores.append(alimentado)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE dieta
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_dieta)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM dieta 
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
                SELECT * FROM dieta 
                WHERE ID = ?
            """,
            (ID,)
        )
        dieta = cursor.fetchone()
        cursor.close()
        return dieta

    def alternar_alimentado(self, id_dieta):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            "SELECT alimentado FROM dieta WHERE ID = ?",
            (id_dieta,)
        )
        resultado = cursor.fetchone()
        
        if resultado:
            valor_atual = resultado[0]
            novo_valor = "não" if valor_atual.lower() == "sim" else "sim"
            cursor.execute(
                """
                    UPDATE dieta
                    SET alimentado = ?
                    WHERE ID = ?
                """,
                (novo_valor, id_dieta)
            )
            CONNECTION_DB.commit()
        else:
            print("ID da dieta não encontrado.")
        
        cursor.close()
