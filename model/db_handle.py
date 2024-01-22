from controller.db_controller import ManageDB
import requests
db = ManageDB


def search_address(json, uid):
    cep_api = f'https://viacep.com.br/ws/{json["cep"]}/json/'
    try:
        response = requests.get(cep_api)
        data = response.json()
        json["uid"] = uid
        json["information"] = data
        return json
    except Exception as e:
        return {
            'Status': False,
            'Message': e
        }


