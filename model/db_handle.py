from controller.db_controller import ManageDB
import requests
db = ManageDB


def search_address(cep):
    cep_api = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(cep_api)
        data = response.json()
        return data
    except Exception as e:
        return {
            'Status': False,
            'Message': e
        }


