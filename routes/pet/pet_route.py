from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.pet.pet_crud import Pet
import sqlite3

pet_bp = Blueprint("pet", __name__)

# 🔹 POST: Criar Pet e associar ao usuário
@pet_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Pets'],
    'description': 'Cria um novo pet e associa ao usuário logado',
    'parameters': [
        {
            'name': 'idusuario',
            'in': 'header',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário logado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['nome'],
                'properties': {
                    'nome': {'type': 'string'},
                    'sexo': {'type': 'string'},
                    'data_nascimento': {'type': 'string'},
                    'data_adocao': {'type': 'string'},
                    'raca': {'type': 'string'},
                    'cor': {'type': 'string'},
                    'alergias': {'type': 'string'},
                    'idmedicamentos': {'type': 'integer'},
                    'idhistorico_consultas': {'type': 'integer'},
                    'idvacinas': {'type': 'integer'},
                    'iddieta': {'type': 'integer'},
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Pet criado e associado ao usuário'}
    }
})
def criar_pet():
    data = request.json
    idusuario = request.headers.get("idusuario")

    if not idusuario:
        return jsonify({"erro": "ID do usuário não fornecido no header"}), 400

    pet = Pet(
        nome=data["nome"],
        sexo=data.get("sexo"),
        data_nascimento=data.get("data_nascimento"),
        data_adocao=data.get("data_adocao"),
        raca=data.get("raca"),
        cor=data.get("cor"),
        alergias=data.get("alergias"),
        idmedicamentos=data.get("idmedicamentos"),
        idhistorico_consultas=data.get("idhistorico_consultas"),
        idvacinas=data.get("idvacinas"),
        iddieta=data.get("iddieta"),
    )
    pet_id = pet.save()

    # Associar ao usuário via pet_usuario
    conn = sqlite3.connect("agendapet.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pet_usuario (idpet, idusuario) VALUES (?, ?)", (pet_id, idusuario))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Pet criado e associado ao usuário com sucesso!"}), 201

# 🔹 GET: Buscar Pet por ID
@pet_bp.route("/<int:id_pet>", methods=["GET"])
@swag_from({
    'tags': ['Pets'],
    'description': 'Busca um pet pelo ID',
    'parameters': [
        {
            'name': 'id_pet',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do pet'
        }
    ],
    'responses': {
        200: {'description': 'Pet encontrado'},
        404: {'description': 'Pet não encontrado'}
    }
})
def buscar_pet(id_pet):
    pet = Pet("", "", "", "", "", "", "", None, None, None, None)
    resultado = pet.get_by_id(id_pet)

    if resultado:
        return jsonify({
            "ID": resultado[0],
            "nome": resultado[1],
            "sexo": resultado[2],
            "data_nascimento": resultado[3],
            "data_adocao": resultado[4],
            "raca": resultado[5],
            "cor": resultado[6],
            "alergias": resultado[7],
            "idmedicamentos": resultado[8],
            "idhistorico_consultas": resultado[9],
            "idvacinas": resultado[10],
            "iddieta": resultado[11]
        })
    else:
        return jsonify({"erro": "Pet não encontrado"}), 404

# 🔹 PUT: Atualizar Pet
@pet_bp.route("/<int:id_pet>", methods=["PUT"])
@swag_from({
    'tags': ['Pets'],
    'description': 'Atualiza um pet pelo ID',
    'parameters': [
        {
            'name': 'id_pet',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do pet'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'sexo': {'type': 'string'},
                    'data_nascimento': {'type': 'string'},
                    'data_adocao': {'type': 'string'},
                    'raca': {'type': 'string'},
                    'cor': {'type': 'string'},
                    'alergias': {'type': 'string'},
                    'idmedicamentos': {'type': 'integer'},
                    'idhistorico_consultas': {'type': 'integer'},
                    'idvacinas': {'type': 'integer'},
                    'iddieta': {'type': 'integer'},
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Pet atualizado com sucesso'}
    }
})
def atualizar_pet(id_pet):
    data = request.json
    pet = Pet("", "", "", "", "", "", "", None, None, None, None)
    pet.update(
        id_pet,
        nome=data.get("nome"),
        sexo=data.get("sexo"),
        data_nascimento=data.get("data_nascimento"),
        data_adocao=data.get("data_adocao"),
        raca=data.get("raca"),
        cor=data.get("cor"),
        alergias=data.get("alergias"),
        idmedicamentos=data.get("idmedicamentos"),
        idhistorico_consultas=data.get("idhistorico_consultas"),
        idvacinas=data.get("idvacinas"),
        iddieta=data.get("iddieta")
    )
    return jsonify({"mensagem": "Pet atualizado com sucesso"})

# 🔹 DELETE: Deletar Pet
@pet_bp.route("/<int:id_pet>", methods=["DELETE"])
@swag_from({
    'tags': ['Pets'],
    'description': 'Deleta um pet pelo ID',
    'parameters': [
        {
            'name': 'id_pet',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do pet'
        }
    ],
    'responses': {
        200: {'description': 'Pet deletado com sucesso'}
    }
})
def deletar_pet(id_pet):
    pet = Pet("", "", "", "", "", "", "", None, None, None, None)
    pet.delete(id_pet)
    return jsonify({"mensagem": "Pet deletado com sucesso"})
