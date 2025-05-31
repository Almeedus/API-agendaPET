from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.historico_consulta.historico_consulta_crud import HistoricoConsulta

historico_bp = Blueprint("historico_bp", __name__)

# 🔹 POST: Criar consulta
@historico_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Histórico de Consultas'],
    'description': 'Cria uma nova consulta no histórico',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['data_consulta', 'hora_consulta'],
                'properties': {
                    'data_consulta': {'type': 'string', 'example': '2025-06-01'},
                    'hora_consulta': {'type': 'string', 'example': '14:30'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Consulta criada com sucesso'},
        400: {'description': "Campos obrigatórios 'data_consulta' e 'hora_consulta' não foram informados"}
    }
})
def criar_consulta():
    data = request.get_json()
    data_consulta = data.get("data_consulta")
    hora_consulta = data.get("hora_consulta")

    if not data_consulta or not hora_consulta:
        return jsonify({"erro": "Campos 'data_consulta' e 'hora_consulta' são obrigatórios."}), 400

    consulta = HistoricoConsulta(data_consulta, hora_consulta)
    consulta.save()

    return jsonify({"mensagem": "Consulta criada com sucesso!"}), 201


# 🔹 GET: Obter consulta por ID
@historico_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['Histórico de Consultas'],
    'description': 'Busca uma consulta pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da consulta'
        }
    ],
    'responses': {
        200: {
            'description': 'Consulta encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'data_consulta': {'type': 'string'},
                    'hora_consulta': {'type': 'string'}
                }
            }
        },
        404: {'description': 'Consulta não encontrada'}
    }
})
def obter_consulta(id):
    consulta = HistoricoConsulta("", "").get_by_id(id)
    if not consulta:
        return jsonify({"erro": "Consulta não encontrada."}), 404

    return jsonify({
        "id": consulta[0],
        "data_consulta": consulta[1],
        "hora_consulta": consulta[2]
    })


# 🔹 PUT: Atualizar consulta
@historico_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['Histórico de Consultas'],
    'description': 'Atualiza uma consulta',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da consulta'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_consulta': {'type': 'string', 'example': '2025-06-02'},
                    'hora_consulta': {'type': 'string', 'example': '15:00'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Consulta atualizada com sucesso'}
    }
})
def atualizar_consulta(id):
    data = request.get_json()
    data_consulta = data.get("data_consulta")
    hora_consulta = data.get("hora_consulta")

    HistoricoConsulta("", "").update(id, data_consulta, hora_consulta)
    return jsonify({"mensagem": "Consulta atualizada com sucesso!"})


# 🔹 DELETE: Deletar consulta
@historico_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['Histórico de Consultas'],
    'description': 'Deleta uma consulta pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da consulta'
        }
    ],
    'responses': {
        200: {'description': 'Consulta deletada com sucesso'}
    }
})
def deletar_consulta(id):
    HistoricoConsulta("", "").delete(id)
    return jsonify({"mensagem": "Consulta deletada com sucesso!"})
