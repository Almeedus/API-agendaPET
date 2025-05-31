from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.dieta.dieta_crud import Dieta

dieta_bp = Blueprint("dieta_bp", __name__)

# 🔹 POST: Criar dieta
@dieta_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Dieta'],
    'description': 'Cria uma nova dieta',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['nome_refeicao', 'hora_refeicao'],
                'properties': {
                    'nome_refeicao': {'type': 'string', 'example': 'Almoço'},
                    'hora_refeicao': {'type': 'string', 'example': '12:30'},
                    'alimentado': {'type': 'boolean', 'example': False}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Dieta criada com sucesso'},
        400: {'description': "Campos obrigatórios 'nome_refeicao' e 'hora_refeicao' não foram informados"}
    }
})
def criar_dieta():
    data = request.get_json()
    nome_refeicao = data.get("nome_refeicao")
    hora_refeicao = data.get("hora_refeicao")
    alimentado = data.get("alimentado", False)

    if nome_refeicao is None or hora_refeicao is None:
        return jsonify({"erro": "Campos 'nome_refeicao' e 'hora_refeicao' são obrigatórios."}), 400

    dieta = Dieta(nome_refeicao, hora_refeicao, alimentado)
    dieta.save()

    return jsonify({"mensagem": "Dieta criada com sucesso!"}), 201


# 🔹 GET: Obter dieta por ID
@dieta_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['Dieta'],
    'description': 'Busca uma dieta pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da dieta'
        }
    ],
    'responses': {
        200: {
            'description': 'Dieta encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome_refeicao': {'type': 'string'},
                    'hora_refeicao': {'type': 'string'},
                    'alimentado': {'type': 'boolean'}
                }
            }
        },
        404: {'description': 'Dieta não encontrada'}
    }
})
def obter_dieta(id):
    dieta = Dieta("", "", "").get_by_id(id)

    if dieta:
        return jsonify({
            "id": dieta[0],
            "nome_refeicao": dieta[1],
            "hora_refeicao": dieta[2],
            "alimentado": bool(dieta[3])
        }), 200
    else:
        return jsonify({"erro": "Dieta não encontrada."}), 404


# 🔹 PUT: Atualizar dieta
@dieta_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['Dieta'],
    'description': 'Atualiza uma dieta',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da dieta'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome_refeicao': {'type': 'string', 'example': 'Jantar'},
                    'hora_refeicao': {'type': 'string', 'example': '19:00'},
                    'alimentado': {'type': 'boolean', 'example': True}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Dieta atualizada com sucesso'}
    }
})
def atualizar_dieta(id):
    data = request.get_json()
    nome_refeicao = data.get("nome_refeicao")
    hora_refeicao = data.get("hora_refeicao")
    alimentado = data.get("alimentado")

    dieta = Dieta("", "", "")
    dieta.update(id, nome_refeicao, hora_refeicao, alimentado)

    return jsonify({"mensagem": "Dieta atualizada com sucesso!"}), 200


# 🔹 DELETE: Deletar dieta
@dieta_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['Dieta'],
    'description': 'Deleta uma dieta pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da dieta'
        }
    ],
    'responses': {
        200: {'description': 'Dieta deletada com sucesso'}
    }
})
def deletar_dieta(id):
    dieta = Dieta("", "", "")
    dieta.delete(id)

    return jsonify({"mensagem": "Dieta deletada com sucesso!"}), 200


# 🔹 PATCH: Alternar status alimentado
@dieta_bp.route("/<int:id>/alternar", methods=["PATCH"])
@swag_from({
    'tags': ['Dieta'],
    'description': "Alterna o status 'alimentado' de uma dieta",
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da dieta'
        }
    ],
    'responses': {
        200: {'description': "Status 'alimentado' alternado com sucesso"},
        404: {'description': 'Dieta não encontrada'}
    }
})
def alternar_alimentado(id):
    dieta = Dieta("", "", "")
    dieta_existente = dieta.get_by_id(id)

    if not dieta_existente:
        return jsonify({"erro": "Dieta não encontrada."}), 404

    dieta.alternar_alimentado(id)
    return jsonify({"mensagem": "Status 'alimentado' alternado com sucesso!"}), 200
