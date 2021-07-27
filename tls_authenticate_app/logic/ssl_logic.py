import tempfile
import ssl

from tls_authenticate_app.logic.API_settings import CERTIFICATE_DATA, PRIVATE_KEY_DATA


def prepare_tls_context(temporary_directory):
    """
    context - данные о сертификате и ключе, которые будут использоваться для авторизации.
    """
    certificate_file, certificate_secret = make_certificate_and_key(temporary_directory)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certificate_file.name, keyfile=certificate_secret.name)
    return context


def make_certificate_and_key(temporary_directory):
    """
    Так как по ТЗ содержимое .crt и .key должно лежать не в файлах, а в строках в настройках, создаются два временных
    файла для авторизации. Как только авторизация будет завершена, файлы удалятся.
    """
    certificate = create_temporary_file(temporary_directory, CERTIFICATE_DATA)
    key = create_temporary_file(temporary_directory, PRIVATE_KEY_DATA)

    return certificate, key


def create_temporary_file(temporary_directory, file_content):
    file = tempfile.NamedTemporaryFile(dir=temporary_directory, delete=False)
    file.write(file_content)
    file.close()
    return file
