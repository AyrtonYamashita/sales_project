from flask import Blueprint, request, jsonify
from controller.db_controller import ManageDB
db = ManageDB()

register_bp_user = Blueprint('register_user', __name__)
register_bp_address_send = Blueprint('register_add_send', __name__)
register_bp_address_recip = Blueprint('register_add_recip', __name__)
register_bp_add_prod = Blueprint('register_add_products', __name__)


# Rota responsável por receber as informações de cadastro do frondend
@register_bp_user.route("/user", methods=["POST"])
def insert_user():
    if not request.json:
        return jsonify({
            'Status': False,
            'Message': 'Aguardando JSON'
        }), 401

    data_info = request.json
    db.add_user_data(**data_info)
    return jsonify({
        'Status': True,
        'Message': {**data_info}
    }), 200


@register_bp_address_send.route("/address_send", methods=["POST"])
def insert_address():
    auth = request.headers.get("Authorization")
    address_info = request.json
    address_info["uid"] = auth
    if not request.authorization:
        return jsonify({
            'Status': False,
            'Message': 'Token de autorização pendente!'
        }), 401
    if not request.json:
        return jsonify({
            'Status': False,
            'Message': 'Aguardando JSON'
        })
    if db.add_address_sender(uid=address_info["uid"],
                             cep=address_info["cep"],
                             street=address_info["logradouro"],
                             neigh=address_info["bairro"],
                             city=address_info["localidade"],
                             state=address_info["uf"],
                             complement=address_info["complemento"],
                             number=address_info["number"]):
        return jsonify({
            'Status': True,
            'Message': {**address_info}
        }), 200


@register_bp_address_recip.route("/address_recipient", methods=["POST"])
def insert_address():
    auth = request.headers.get("Authorization")
    address_info = request.json
    address_info["uid"] = auth
    if not request.authorization:
        return jsonify({
            'Status': False,
            'Message': 'Token de autorização inválido.'
        })
    if not request.json:
        return jsonify({
            'Status': False,
            'Message': 'Aguardando JSON'
        })
    if db.add_address_recipient(uid=address_info["uid"],
                                cep=address_info["cep"],
                                street=address_info["logradouro"],
                                neigh=address_info["bairro"],
                                city=address_info["localidade"],
                                state=address_info["uf"],
                                complement=address_info["complemento"],
                                number=address_info["number"]):
        return jsonify({
            'Status': True,
            'Message': {**address_info}
        })


@register_bp_add_prod.route("/products", methods=["POST"])
def insert_products():
    auth = request.headers.get("Authorization")
    data_products = request.json
    data_products["uid"] = auth

    if not request.authorization:
        return jsonify({
            'Status': False,
            'Message': 'Token de autenticação inválido!'
        })
    if not request.json:
        return jsonify({
            'Status': True,
            'Message': 'Aguardando JSON'
        })