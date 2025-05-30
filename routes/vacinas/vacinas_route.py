from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.vacinas.vacinas_crud import Vacina

vacinas_bp = Blueprint("vacinas", __name__)

# 🔹 POST: Criar vacina
@vacinas_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Vacinas'],
    'description': 'Cria uma nova vacina',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['nome', 'data_vacina', 'tipo_vacina'],
                'properties': {
                    'nome': {'type': 'string', 'example': 'Vacina Antirrábica'},
                    'data_vacina': {'type': 'string', 'example': '2025-05-30'},
                    'tipo_vacina': {'type': 'string', 'example': 'Antirrábica'},
                    'observacao': {'type': 'string', 'example': 'Tomar reforço em 1 ano'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Vacina criada com sucesso'}
    }
})
def criar_vacina():
    data = request.json
    vacina = Vacina(
        nome=data["nome"],
        data_vacina=data["data_vacina"],
        tipo_vacina=data["tipo_vacina"],
        observacao=data.get("observacao", "")
    )
    vacina.save()
    return jsonify({"mensagem": "Vacina criada com sucesso!"}), 201


# 🔹 GET: Buscar vacina por ID
@vacinas_bp.route("/<int:id_vacina>", methods=["GET"])
@swag_from({
    'tags': ['Vacinas'],
    'description': 'Busca uma vacina pelo ID',
    'parameters': [
        {
            'name': 'id_vacina',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da vacina'
        }
    ],
    'responses': {
        200: {
            'description': 'Vacina encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'ID': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'data_vacina': {'type': 'string'},
                    'tipo_vacina': {'type': 'string'},
                    'observacao': {'type': 'string'}
                }
            }
        },
        404: {'description': 'Vacina não encontrada'}
    }
})
def buscar_vacina(id_vacina):
    vacina = Vacina("", "", "", "")
    resultado = vacina.get_by_id(id_vacina)
    if resultado:
        return jsonify({
            "ID": resultado[0],
            "nome": resultado[1],
            "data_vacina": resultado[2],
            "tipo_vacina": resultado[3],
            "observacao": resultado[4]
        })
    else:
        return jsonify({"erro": "Vacina não encontrada"}), 404


# 🔹 PUT: Atualizar vacina
@vacinas_bp.route("/<int:id_vacina>", methods=["PUT"])
@swag_from({
    'tags': ['Vacinas'],
    'description': 'Atualiza uma vacina parcial ou totalmente',
    'parameters': [
        {
            'name': 'id_vacina',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da vacina'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'Vacina Atualizada'},
                    'data_vacina': {'type': 'string', 'example': '2025-06-01'},
                    'tipo_vacina': {'type': 'string', 'example': 'Nova Tipo'},
                    'observacao': {'type': 'string', 'example': 'Nova observação'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Vacina atualizada com sucesso'}
    }
})
def atualizar_vacina(id_vacina):
    data = request.json
    vacina = Vacina("", "", "", "")
    vacina.update(
        id_vacina,
        nome=data.get("nome"),
        data_vacina=data.get("data_vacina"),
        tipo_vacina=data.get("tipo_vacina"),
        observacao=data.get("observacao")
    )
    return jsonify({"mensagem": "Vacina atualizada com sucesso"})


# 🔹 DELETE: Deletar vacina
@vacinas_bp.route("/<int:id_vacina>", methods=["DELETE"])
@swag_from({
    'tags': ['Vacinas'],
    'description': 'Deleta uma vacina pelo ID',
    'parameters': [
        {
            'name': 'id_vacina',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da vacina'
        }
    ],
    'responses': {
        200: {'description': 'Vacina deletada com sucesso'}
    }
})
def deletar_vacina(id_vacina):
    vacina = Vacina("", "", "", "")
    vacina.delete(id_vacina)
    return jsonify({"mensagem": "Vacina deletada com sucesso"})
