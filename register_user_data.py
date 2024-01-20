from flask import Blueprint, request, jsonify
from .controller.db_controller import ManageDB
db = ManageDB

register_bp = Blueprint('register', __name__)


# Rota responsável por receber as informações de cadastro do frondend
@register_bp.route("/user", methods=["GET"])
def teste():
    return jsonify({
        'io': 'teste'
    })
# def insert_user():
#     if not request.json:
#         return jsonify({
#             'Status': False,
#             'Message': 'Aguardando JSON'
#         })
#     try:
#         data_info = request.json
#         db.add_user_data(**data_info)
#         return jsonify({
#             'Status': True,
#             'Message': 'Informações de usuário adicionada.'
#         }), 200
#     except Exception as e:
#         return jsonify({
#             'Status': False,
#             'Message': e
#         }), 400
        


# @register_bp("/address_send", methods=["POST"])
# def insert_address():
#     if not request.json:
#         return jsonify({
#             'Status': False,
#             'Message': 'Aguardando JSON'
#         })
#     try:
#         address_info = request.json
#         db.add_address_sender(**address_info)
#         return jsonify({
#             'Status': True,
#             'Message': 'Informações de endereço adicionadas.'
#         })
#     except Exception as e:
#         return jsonify({
#             'Status': False,
#             'Message': e
#         })
        
# @register_bp("/address_recipient", methods=["POST"])
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
