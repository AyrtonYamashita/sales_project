from flask import Blueprint, request, jsonify
from model.db_handle import search_email

user_access_bp = Blueprint('access', __name__)

@user_access_bp.route('/validate', methods=["POST"])
def validate():
    cpf_cnpj = request.headers.get("user_identity")
    if not cpf_cnpj:
        return jsonify({
            'Status': False,
            'Message': 'Identidade de usuario ausente!'
        })
    else:
        return jsonify({
            'Status': True,
            'Message': search_email(cpf_cnpj)
        })
