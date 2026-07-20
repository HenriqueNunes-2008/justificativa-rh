import base64
import tempfile

import cloudinary.uploader


def salvar_assinatura(base64_string):
    """
    Recebe uma assinatura em Base64,
    envia ao Cloudinary e retorna a URL.
    """

    if "," in base64_string:
        base64_string = base64_string.split(",")[1]

    imagem = base64.b64decode(base64_string)

    with tempfile.NamedTemporaryFile(
        suffix=".png",
        delete=False
    ) as arquivo:

        arquivo.write(imagem)

        caminho_temporario = arquivo.name

    resultado = cloudinary.uploader.upload(

        caminho_temporario,

        folder="assinaturas"

    )

    return resultado["secure_url"]


def excluir_assinatura(caminho):
    """
    Exclusão será implementada futuramente.
    """
    pass