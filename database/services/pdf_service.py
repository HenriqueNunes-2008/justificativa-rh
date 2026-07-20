import os
import tempfile
import requests

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)


def gerar_pdf(justificativa, caminho_saida):
    """
    Gera o PDF da justificativa.
    """

    estilos = getSampleStyleSheet()

    titulo = estilos["Heading1"]
    titulo.alignment = TA_CENTER
    titulo.textColor = HexColor("#145392")

    normal = estilos["BodyText"]

    pdf = SimpleDocTemplate(
        caminho_saida,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    elementos = []

    elementos.append(
        Paragraph(
            "JUSTIFICATIVA DE PONTO",
            titulo
        )
    )

    elementos.append(
        Spacer(1, 0.7 * cm)
    )

    campos = [

        ("Nome", justificativa.nome),

        ("Cargo", justificativa.cargo),

        ("Matrícula", justificativa.matricula),

        ("Competência", justificativa.competencia),

        ("Data", justificativa.data.strftime("%d/%m/%Y")),

        ("Entrada", justificativa.hora_entrada.strftime("%H:%M")),

        ("Saída", justificativa.hora_saida.strftime("%H:%M"))

    ]

    for titulo_campo, valor in campos:

        elementos.append(

            Paragraph(

                f"<b>{titulo_campo}:</b> {valor}",

                normal

            )

        )

    elementos.append(
        Spacer(1, 0.5 * cm)
    )

    elementos.append(
        Paragraph(
            "<b>Justificativa</b>",
            normal
        )
    )

    elementos.append(
        Paragraph(
            justificativa.justificativa,
            normal
        )
    )

    elementos.append(
        Spacer(1, 1 * cm)
    )

    caminho_temporario = None

    try:

        resposta = requests.get(
            justificativa.assinatura,
            timeout=10
        )

        if resposta.status_code == 200:

            with tempfile.NamedTemporaryFile(
                suffix=".png",
                delete=False
            ) as arquivo:

                arquivo.write(
                    resposta.content
                )

                caminho_temporario = arquivo.name

            elementos.append(

                Paragraph(
                    "<b>Assinatura</b>",
                    normal
                )

            )

            elementos.append(

                Image(
                    caminho_temporario,
                    width=8 * cm,
                    height=3 * cm
                )

            )

    except Exception as erro:

        print(
            "Erro ao carregar assinatura:",
            erro
        )

    elementos.append(
        Spacer(1, 1 * cm)
    )

    elementos.append(

        Paragraph(

            f"Emitido em {justificativa.criado_em.strftime('%d/%m/%Y %H:%M')}",

            normal

        )

    )

    pdf.build(
        elementos
    )

    if caminho_temporario:

        try:

            os.remove(
                caminho_temporario
            )

        except Exception:

            pass

    return caminho_saida