import json
from .ssl_logic import prepare_ssl_context
from .API_settings import API_HOST, API_ENDPOINT
import http.client
import tempfile


def get_external_api_data(request):
    api_data_response = send_api_request(request.POST).getresponse()

    api_data = api_data_response.read().decode('UTF-8')
    return api_data


def send_api_request(POST):
    api_connection = establish_api_connection()
    validated_method_params = validate_method_params(POST['method_params'])
    json_rpc = json.dumps({"jsonrpc": "2.0", "method": POST['method_name'], "params": validated_method_params, 'id': 1})
    api_connection.request(method="POST", body=json_rpc, headers={'Content-Type': 'application/json'}, url=API_ENDPOINT)
    return api_connection


def establish_api_connection():
    """
    Функция создает во временной папке сертификат и ключ. Данные для них указаны в настройках (API_settings.py).
    Возвращает подключение к api сервису. Временные файлы удаляются контекстным менеджером.
    """
    with tempfile.TemporaryDirectory() as temporary_directory:
        tsl_context = prepare_ssl_context(temporary_directory)
        connection = http.client.HTTPSConnection(API_HOST, port=443, context=tsl_context)
        return connection


def validate_method_params(method_params):
    validated_method_params = dict()
    splited_params_pairs = method_params.split()
    for param_pair in splited_params_pairs:
        param_name, param_value = param_pair.split(':')
        validated_method_params[param_name] = param_value

    return validated_method_params
