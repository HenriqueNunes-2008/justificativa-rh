import os
import base64
from datetime import datetime

from flask import current_app


def salvar_assinatura(base64_string):
    """
    Recebe uma assinatura em Base64,
    salva como PNG e retorna o caminho do arquivo.
    """

    if "," in base64_string:
        base64_string = base64_string.split(",")[1]

    imagem = base64.b64decode(base64_string)

    nome = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    ) + ".png"

    pasta = os.path.join(
        current_app.static_folder,
        "assinaturas"
    )

    os.makedirs(pasta, exist_ok=True)

    caminho = os.path.join(
        pasta,
        nome
    )

    with open(caminho, "wb") as arquivo:
        arquivo.write(imagem)

    return f"assinaturas/{nome}"


def excluir_assinatura(caminho):
    """
    Exclui o arquivo de assinatura do disco.
    """

    arquivo = os.path.join(
        current_app.static_folder,
        caminho
    )

    if os.path.exists(arquivo):
        os.remove(arquivo)