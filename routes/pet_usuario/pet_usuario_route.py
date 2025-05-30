from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.pet_usuario.pet_usuario_crud import PetUsuario

pet_usuario_bp = Blueprint("pet_usuario", __name__)

# 🔹 POST: Associar pet ao usuário
@pet_usuario_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Pet-Usuário'],
    'description': 'Associa um pet a um usuário logado',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['idpet', 'idusuario'],
                'properties': {
                    'idpet': {'type': 'integer', 'example': 1},
                    'idusuario': {'type': 'integer', 'example': 10}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Associação criada com sucesso'}
    }
})
def associar_pet_usuario():
    data = request.json
    relacao = PetUsuario(
        idpet=data["idpet"],
        idusuario=data["idusuario"]
    )
    relacao.save()
    return jsonify({"mensagem": "Associação criada com sucesso!"}), 201

# 🔹 GET: Buscar um pet do usuário
@pet_usuario_bp.route("/um/<int:idusuario>", methods=["GET"])
@swag_from({
    'tags': ['Pet-Usuário'],
    'description': 'Retorna apenas um pet do usuário (ex: o primeiro)',
    'parameters': [
        {
            'name': 'idusuario',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário logado'
        }
    ],
    'responses': {
        200: {
            'description': 'Pet encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'ID_pet_usuario': {'type': 'integer'},
                    'idpet': {'type': 'integer'},
                    'idusuario': {'type': 'integer'}
                }
            }
        },
        404: {'description': 'Nenhum pet encontrado para o usuário'}
    }
})
def buscar_um_pet(idusuario):
    relacao = PetUsuario(None, None)
    pet = relacao.get_um_pet_do_usuario(idusuario)
    if pet:
        return jsonify({
            "ID_pet_usuario": pet[0],
            "idpet": pet[1],
            "idusuario": pet[2]
        })
    else:
        return jsonify({"erro": "Nenhum pet encontrado para esse usuário"}), 404

# 🔹 GET: Buscar todos os pets do usuário
@pet_usuario_bp.route("/todos/<int:idusuario>", methods=["GET"])
@swag_from({
    'tags': ['Pet-Usuário'],
    'description': 'Retorna todos os pets do usuário',
    'parameters': [
        {
            'name': 'idusuario',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário logado'
        }
    ],
    'responses': {
        200: {
            'description': 'Pets encontrados',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'ID_pet_usuario': {'type': 'integer'},
                        'idpet': {'type': 'integer'},
                        'idusuario': {'type': 'integer'}
                    }
                }
            }
        }
    }
})
def buscar_todos_pets(idusuario):
    relacao = PetUsuario(None, None)
    pets = relacao.get_pets_by_usuario(idusuario)
    return jsonify([
        {
            "ID_pet_usuario": pet[0],
            "idpet": pet[1],
            "idusuario": pet[2]
        }
        for pet in pets
    ])

# 🔹 DELETE: Desassociar pet do usuário
@pet_usuario_bp.route("/<int:id_pet_usuario>", methods=["DELETE"])
@swag_from({
    'tags': ['Pet-Usuário'],
    'description': 'Remove a associação entre pet e usuário',
    'parameters': [
        {
            'name': 'id_pet_usuario',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da associação pet-usuário'
        }
    ],
    'responses': {
        200: {'description': 'Associação removida com sucesso'}
    }
})
def remover_associacao(id_pet_usuario):
    relacao = PetUsuario(None, None)
    relacao.delete(id_pet_usuario)
    return jsonify({"mensagem": "Associação removida com sucesso!"})
