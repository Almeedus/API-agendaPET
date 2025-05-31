from flask import Blueprint, request, jsonify
from routes.agenda.agenda_crud import Agenda  # ajuste o import conforme o seu projeto

agenda_bp = Blueprint("agenda_bp", __name__)

@agenda_bp.route("/", methods=["POST"])
def criar_atividade():
    """
    Cria uma nova atividade na agenda
    ---
    tags:
      - Agenda
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
                example: "Consulta veterinária"
              dia_atividade:
                type: string
                example: "2025-06-10"
              hora_atividade:
                type: string
                example: "14:00"
              completado:
                type: boolean
                example: false
              observacao:
                type: string
                example: "Levar carteira de vacinação"
            required:
              - nome
              - dia_atividade
              - hora_atividade
    responses:
      201:
        description: Atividade criada com sucesso
      400:
        description: Erro nos dados enviados
    """
    data = request.get_json()
    nome = data.get("nome")
    dia_atividade = data.get("dia_atividade")
    hora_atividade = data.get("hora_atividade")
    completado = data.get("completado", False)
    observacao = data.get("observacao")

    if not nome or not dia_atividade or not hora_atividade:
        return jsonify({"erro": "Campos 'nome', 'dia_atividade' e 'hora_atividade' são obrigatórios."}), 400

    atividade = Agenda(nome, dia_atividade, hora_atividade, completado, observacao)
    atividade.save()
    return jsonify({"mensagem": "Atividade criada com sucesso!"}), 201


@agenda_bp.route("/<int:id>", methods=["GET"])
def obter_atividade(id):
    """
    Obtém uma atividade pelo ID
    ---
    tags:
      - Agenda
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
        description: ID da atividade
    responses:
      200:
        description: Atividade encontrada
        content:
          application/json:
            schema:
              type: object
              properties:
                ID:
                  type: integer
                nome:
                  type: string
                dia_atividade:
                  type: string
                hora_atividade:
                  type: string
                completado:
                  type: boolean
                observacao:
                  type: string
      404:
        description: Atividade não encontrada
    """
    atividade = Agenda("", "", "").get_by_id(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada."}), 404

    return jsonify({
        "ID": atividade[0],
        "nome": atividade[1],
        "dia_atividade": atividade[2],
        "hora_atividade": atividade[3],
        "completado": bool(atividade[4]),
        "observacao": atividade[5]
    })


@agenda_bp.route("/<int:id>", methods=["PUT"])
def atualizar_atividade(id):
    """
    Atualiza uma atividade pelo ID
    ---
    tags:
      - Agenda
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
        description: ID da atividade
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
              dia_atividade:
                type: string
              hora_atividade:
                type: string
              completado:
                type: boolean
              observacao:
                type: string
    responses:
      200:
        description: Atividade atualizada com sucesso
      400:
        description: Erro nos dados enviados
    """
    data = request.get_json()
    nome = data.get("nome")
    dia_atividade = data.get("dia_atividade")
    hora_atividade = data.get("hora_atividade")
    completado = data.get("completado")
    observacao = data.get("observacao")

    atividade = Agenda("", "", "")
    atividade.update(id, nome, dia_atividade, hora_atividade, completado, observacao)

    return jsonify({"mensagem": "Atividade atualizada com sucesso!"}), 200


@agenda_bp.route("/<int:id>", methods=["DELETE"])
def deletar_atividade(id):
    """
    Deleta uma atividade pelo ID
    ---
    tags:
      - Agenda
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
        description: ID da atividade
    responses:
      200:
        description: Atividade deletada com sucesso
      404:
        description: Atividade não encontrada
    """
    atividade = Agenda("", "", "").get_by_id(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada."}), 404

    Agenda("", "", "").delete(id)
    return jsonify({"mensagem": "Atividade deletada com sucesso!"}), 200


@agenda_bp.route("/<int:id>/alternar-completado", methods=["PATCH"])
def alternar_completado(id):
    """
    Alterna o status de completado de uma atividade
    ---
    tags:
      - Agenda
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
        description: ID da atividade
    responses:
      200:
        description: Status 'completado' alternado com sucesso
      404:
        description: Atividade não encontrada
    """
    atividade = Agenda("", "", "").get_by_id(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada."}), 404

    Agenda("", "", "").alternar_completado(id)
    return jsonify({"mensagem": "Status 'completado' alternado com sucesso!"}), 200
