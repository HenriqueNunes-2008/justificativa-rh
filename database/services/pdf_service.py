import os

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

    elementos.append(Spacer(1, 0.7 * cm))

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

    elementos.append(Spacer(1, 0.5 * cm))

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

    elementos.append(Spacer(1, 1 * cm))

    assinatura = os.path.join(
        "static",
        justificativa.assinatura
    )

    if os.path.exists(assinatura):

        elementos.append(
            Paragraph(
                "<b>Assinatura</b>",
                normal
            )
        )

        elementos.append(
            Image(
                assinatura,
                width=8 * cm,
                height=3 * cm
            )
        )

    elementos.append(Spacer(1, 1 * cm))

    elementos.append(
        Paragraph(
            f"Emitido em {justificativa.criado_em.strftime('%d/%m/%Y %H:%M')}",
            normal
        )
    )

    pdf.build(elementos)

    return caminho_saida