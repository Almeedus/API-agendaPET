import sqlite3
CONNECTION_DB = sqlite3.connect("agendapet.db", check_same_thread=False)

class PetUsuario:
    def __init__(self, idpet, idusuario):
        self.idpet = idpet
        self.idusuario = idusuario

    def save(self):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                INSERT INTO pet_usuario (idpet, idusuario)
                VALUES (?, ?)
            """,
            (self.idpet, self.idusuario)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def delete(self, ID_pet_usuario):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                DELETE FROM pet_usuario
                WHERE ID_pet_usuario = ?
            """,
            (ID_pet_usuario,)
        )
        CONNECTION_DB.commit()
        cursor.close()

    def get_by_id(self, ID_pet_usuario):
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                SELECT * FROM pet_usuario
                WHERE ID_pet_usuario = ?
            """,
            (ID_pet_usuario,)
        )
        pet_usuario = cursor.fetchone()
        cursor.close()
        return pet_usuario

    def get_pets_by_usuario(self, idusuario):
        """Retorna todos os pets associados ao usuário logado."""
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                SELECT * FROM pet_usuario
                WHERE idusuario = ?
            """,
            (idusuario,)
        )
        pets = cursor.fetchall()
        cursor.close()
        return pets

    def get_um_pet_do_usuario(self, idusuario):
        """Retorna um único pet do usuário (por exemplo, o primeiro)."""
        cursor = CONNECTION_DB.cursor()
        cursor.execute(
            """
                SELECT * FROM pet_usuario
                WHERE idusuario = ?
                LIMIT 1
            """,
            (idusuario,)
        )
        pet = cursor.fetchone()
        cursor.close()
        return pet
