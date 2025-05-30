import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class Pet:
    def __init__(self, nome, sexo, data_nascimento, data_adocao, raca, cor, alergias,
                 idmedicamentos, idhistorico_consultas, idvacinas, iddieta):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.data_adocao = data_adocao
        self.raca = raca
        self.cor = cor
        self.alergias = alergias
        self.idmedicamentos = idmedicamentos
        self.idhistorico_consultas = idhistorico_consultas
        self.idvacinas = idvacinas
        self.iddieta = iddieta

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO pet (
                    nome, sexo, data_nascimento, data_adocao, raca, cor, alergias,
                    idmedicamentos, idhistorico_consultas, idvacinas, iddieta
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                self.nome, self.sexo, self.data_nascimento, self.data_adocao, self.raca,
                self.cor, self.alergias, self.idmedicamentos, self.idhistorico_consultas,
                self.idvacinas, self.iddieta
            )
        )
        CONNECTION_DB.commit()
        cursor.close()

    def update(self, id_pet, nome=None, sexo=None, data_nascimento=None, data_adocao=None,
               raca=None, cor=None, alergias=None, idmedicamentos=None,
               idhistorico_consultas=None, idvacinas=None, iddieta=None):
        cursor = CONNECTION_DB.cursor()

        campos = []
        valores = []

        if nome is not None:
            campos.append("nome = ?")
            valores.append(nome)

        if sexo is not None:
            campos.append("sexo = ?")
            valores.append(sexo)

        if data_nascimento is not None:
            campos.append("data_nascimento = ?")
            valores.append(data_nascimento)

        if data_adocao is not None:
            campos.append("data_adocao = ?")
            valores.append(data_adocao)

        if raca is not None:
            campos.append("raca = ?")
            valores.append(raca)

        if cor is not None:
            campos.append("cor = ?")
            valores.append(cor)

        if alergias is not None:
            campos.append("alergias = ?")
            valores.append(alergias)

        if idmedicamentos is not None:
            campos.append("idmedicamentos = ?")
            valores.append(idmedicamentos)

        if idhistorico_consultas is not None:
            campos.append("idhistorico_consultas = ?")
            valores.append(idhistorico_consultas)

        if idvacinas is not None:
            campos.append("idvacinas = ?")
            valores.append(idvacinas)

        if iddieta is not None:
            campos.append("iddieta = ?")
            valores.append(iddieta)

        if not campos:
            print("Nenhum campo fornecido para atualizar.")
            return

        sql = f"""
            UPDATE pet
            SET {', '.join(campos)}
            WHERE ID = ?
        """
        valores.append(id_pet)

        cursor.execute(sql, valores)
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM pet 
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
                SELECT * FROM pet 
                WHERE ID = ?
            """,
            (ID,)
        )
        pet = cursor.fetchone()
        cursor.close()
        return pet
