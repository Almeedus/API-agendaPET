from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.medicamentos.medicamentos_crud import Medicamento

medicamento_bp = Blueprint("medicamento_bp", __name__)

# 🔹 POST: Criar medicamento
@medicamento_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Medicamentos'],
    'description': 'Cria um novo medicamento',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['nome'],
                'properties': {
                    'nome': {'type': 'string', 'example': 'Paracetamol'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Medicamento criado com sucesso'}
    }
})
def criar_medicamento():
    data = request.get_json()
    nome = data.get("nome")

    if not nome:
        return jsonify({"erro": "Campo 'nome' é obrigatório."}), 400

    medicamento = Medicamento(nome)
    medicamento.save()

    return jsonify({"mensagem": "Medicamento criado com sucesso!"}), 201


# 🔹 GET: Obter medicamento por ID
@medicamento_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['Medicamentos'],
    'description': 'Busca um medicamento pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do medicamento'
        }
    ],
    'responses': {
        200: {
            'description': 'Medicamento encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome': {'type': 'string'}
                }
            }
        },
        404: {'description': 'Medicamento não encontrado'}
    }
})
def obter_medicamento(id):
    medicamento = Medicamento("").get_by_id(id)
    if medicamento:
        return jsonify({
            "id": medicamento[0],
            "nome": medicamento[1]
        }), 200
    else:
        return jsonify({"erro": "Medicamento não encontrado."}), 404


# 🔹 PUT: Atualizar medicamento
@medicamento_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['Medicamentos'],
    'description': 'Atualiza um medicamento',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do medicamento'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'Novo nome do medicamento'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Medicamento atualizado com sucesso'}
    }
})
def atualizar_medicamento(id):
    data = request.get_json()
    nome = data.get("nome")

    medicamento = Medicamento("")
    medicamento.update(id, nome)

    return jsonify({"mensagem": "Medicamento atualizado com sucesso!"}), 200


# 🔹 DELETE: Deletar medicamento
@medicamento_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['Medicamentos'],
    'description': 'Deleta um medicamento pelo ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do medicamento'
        }
    ],
    'responses': {
        200: {'description': 'Medicamento deletado com sucesso'}
    }
})
def deletar_medicamento(id):
    medicamento = Medicamento("")
    medicamento.delete(id)
    return jsonify({"mensagem": "Medicamento deletado com sucesso!"}), 200
