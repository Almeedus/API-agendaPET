from flask import Blueprint, request, jsonify
from flasgger import swag_from
from routes.usuario.usuario_crud import Usuario

usuario_bp = Blueprint("usuario", __name__)

# 🔹 POST: Criar usuário
@usuario_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Usuários'],
    'description': 'Cria um novo usuário',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['nome', 'sobrenome', 'email', 'senha'],
                'properties': {
                    'nome': {'type': 'string', 'example': 'João'},
                    'sobrenome': {'type': 'string', 'example': 'Silva'},
                    'email': {'type': 'string', 'example': 'joao@email.com'},
                    'senha': {'type': 'string', 'example': '1234'},
                    'descricao': {'type': 'string', 'example': 'Usuário de teste'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Usuário criado com sucesso'}
    }
})
def criar_usuario():
    data = request.json
    usuario = Usuario(
        nome=data["nome"],
        sobrenome=data["sobrenome"],
        email=data["email"],
        senha=data["senha"],
        descricao=data.get("descricao", "")
    )
    usuario.save()
    return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201


# 🔹 GET: Buscar usuário por ID
@usuario_bp.route("/<int:id_usuario>", methods=["GET"])
@swag_from({
    'tags': ['Usuários'],
    'description': 'Busca um usuário pelo ID',
    'parameters': [
        {
            'name': 'id_usuario',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário'
        }
    ],
    'responses': {
        200: {
            'description': 'Usuário encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'ID': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'sobrenome': {'type': 'string'},
                    'email': {'type': 'string'},
                    'senha': {'type': 'string'},
                    'descricao': {'type': 'string'}
                }
            }
        },
        404: {'description': 'Usuário não encontrado'}
    }
})
def buscar_usuario(id_usuario):
    usuario = Usuario("", "", "", "", "")
    resultado = usuario.get_by_id(id_usuario)
    if resultado:
        return jsonify({
            "ID": resultado[0],
            "nome": resultado[1],
            "sobrenome": resultado[2],
            "email": resultado[3],
            "senha": resultado[4],
            "descricao": resultado[5]
        })
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404


# 🔹 PUT: Atualizar usuário
@usuario_bp.route("/<int:id_usuario>", methods=["PUT"])
@swag_from({
    'tags': ['Usuários'],
    'description': 'Atualiza um usuário parcial ou totalmente',
    'parameters': [
        {
            'name': 'id_usuario',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'João Atualizado'},
                    'sobrenome': {'type': 'string', 'example': 'Almeida'},
                    'email': {'type': 'string', 'example': 'joao@novo.com'},
                    'senha': {'type': 'string', 'example': 'novaSenha123'},
                    'descricao': {'type': 'string', 'example': 'Nova descrição'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Usuário atualizado com sucesso'}
    }
})
def atualizar_usuario(id_usuario):
    data = request.json
    usuario = Usuario("", "", "", "", "")
    usuario.update(
        id_usuario,
        nome=data.get("nome"),
        sobrenome=data.get("sobrenome"),
        email=data.get("email"),
        senha=data.get("senha"),
        descricao=data.get("descricao")
    )
    return jsonify({"mensagem": "Usuário atualizado com sucesso"})


# 🔹 DELETE: Deletar usuário
@usuario_bp.route("/<int:id_usuario>", methods=["DELETE"])
@swag_from({
    'tags': ['Usuários'],
    'description': 'Deleta um usuário pelo ID',
    'parameters': [
        {
            'name': 'id_usuario',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário'
        }
    ],
    'responses': {
        200: {'description': 'Usuário deletado com sucesso'}
    }
})
def deletar_usuario(id_usuario):
    usuario = Usuario("", "", "", "", "")
    usuario.delete(id_usuario)
    return jsonify({"mensagem": "Usuário deletado com sucesso"})
