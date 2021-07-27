import tempfile
import ssl

from tls_authenticate_app.logic.API_settings import CERTIFICATE_DATA, PRIVATE_KEY_DATA


def make_certificate_and_key(temporary_directory):

    certificate = create_temporary_file(temporary_directory, CERTIFICATE_DATA)
    key = create_temporary_file(temporary_directory, PRIVATE_KEY_DATA)

    return certificate, key


def create_temporary_file(temporary_directory, file_content):
    file = tempfile.NamedTemporaryFile(dir=temporary_directory, delete=False)
    file.write(file_content)
    file.close()
    return file


def prepare_ssl_context(temporary_directory):
    certificate_file, certificate_secret = make_certificate_and_key(temporary_directory)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certificate_file.name, keyfile=certificate_secret.name)
    return context
