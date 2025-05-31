from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.agenda_pet_usuario.agenda_pet_usuario_crud import AgendaPetUsuario

agenda_pet_usuario_bp = Blueprint("agenda_pet_usuario_bp", __name__)

# POST - Criar
@agenda_pet_usuario_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['AgendaPetUsuario'],
    'description': 'Cria um novo registro de agenda_pet_usuario',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['idagenda', 'idpet_usuario'],
                'properties': {
                    'idagenda': {'type': 'integer', 'example': 1},
                    'idpet_usuario': {'type': 'integer', 'example': 2}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Registro criado com sucesso'},
        400: {'description': 'Campos obrigatórios não fornecidos'}
    }
})
def criar_agenda_pet_usuario():
    data = request.get_json()
    idagenda = data.get("idagenda")
    idpet_usuario = data.get("idpet_usuario")

    if idagenda is None or idpet_usuario is None:
        return jsonify({"erro": "Campos 'idagenda' e 'idpet_usuario' são obrigatórios."}), 400

    agenda = AgendaPetUsuario(idagenda, idpet_usuario)
    agenda.save()

    return jsonify({"mensagem": "Registro criado com sucesso!"}), 201


# GET - Obter por ID
@agenda_pet_usuario_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['AgendaPetUsuario'],
    'description': 'Busca um registro pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do registro'
        }
    ],
    'responses': {
        200: {
            'description': 'Registro encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'ID': {'type': 'integer'},
                    'idagenda': {'type': 'integer'},
                    'idpet_usuario': {'type': 'integer'}
                }
            }
        },
        404: {'description': 'Registro não encontrado'}
    }
})
def obter_agenda_pet_usuario(id):
    agenda = AgendaPetUsuario(None, None).get_by_id(id)

    if agenda:
        return jsonify({
            "ID": agenda[0],
            "idagenda": agenda[1],
            "idpet_usuario": agenda[2]
        }), 200
    else:
        return jsonify({"erro": "Registro não encontrado."}), 404


# PUT - Atualizar
@agenda_pet_usuario_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['AgendaPetUsuario'],
    'description': 'Atualiza um registro pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do registro'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'idagenda': {'type': 'integer', 'example': 3},
                    'idpet_usuario': {'type': 'integer', 'example': 4}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Registro atualizado com sucesso'},
        400: {'description': 'Nenhum campo fornecido para atualizar'}
    }
})
def atualizar_agenda_pet_usuario(id):
    data = request.get_json()
    idagenda = data.get("idagenda")
    idpet_usuario = data.get("idpet_usuario")

    agenda = AgendaPetUsuario(None, None)
    agenda.update(id, idagenda=idagenda, idpet_usuario=idpet_usuario)

    return jsonify({"mensagem": "Registro atualizado com sucesso!"}), 200


# DELETE - Deletar
@agenda_pet_usuario_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['AgendaPetUsuario'],
    'description': 'Deleta um registro pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do registro'
        }
    ],
    'responses': {
        200: {'description': 'Registro deletado com sucesso'}
    }
})
def deletar_agenda_pet_usuario(id):
    agenda = AgendaPetUsuario(None, None)
    agenda.delete(id)

    return jsonify({"mensagem": "Registro deletado com sucesso!"}), 200
