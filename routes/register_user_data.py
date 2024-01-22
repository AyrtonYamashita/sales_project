from flask import Blueprint, request, jsonify
from controller.db_controller import ManageDB
db = ManageDB()

register_bp_user = Blueprint('register_user', __name__)
register_bp_address_send = Blueprint('register_add_send', __name__)
register_bp_address_recip = Blueprint('register_add_recip', __name__)


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

    if not request.authorization:
        return jsonify({
            'Status': False,
            'Message': 'Token de autorização ausente'
        }), 401

    if not request.json:
        return jsonify({
            'Status': False,
            'Message': 'Aguardando JSON'
        })
    try:
        auth = request.authorization
        address_info = request.json
        address_info["uid"] = auth
        db.add_address_sender(**address_info)
        return jsonify({
            'Status': True,
            'Message': {**address_info}
        })
    except Exception as e:
        return jsonify({
            'Status': False,
            'Message': e
        })

#
# @register_bp_address_recip.route("/address_recipient", methods=["POST"])
# def insert_address():
#     if not request.json:
#         return jsonify({
#             'Status': False,
#             'Message': 'Aguardando JSON'
#         })
#     try:
#         address_info = request.json
#         db.add_address_recipient(**address_info)
#         return jsonify({
#             'Status': True,
#             'Message': 'Informações de endereço adicionadas.'
#         })
#     except Exception as e:
#         return jsonify({
#             'Status': False,
#             'Message': e
#         })
