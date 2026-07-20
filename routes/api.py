import os

from flask import (
    Blueprint,
    jsonify,
    send_file,
    request,
    session,
    abort
)

from werkzeug.exceptions import HTTPException

from database.services import (
    buscar_justificativa,
    excluir_justificativa
)

from database.services.pdf_service import gerar_pdf

from database.services import (

    listar_usuarios,

    ativar_usuario,

    bloquear_usuario,

    redefinir_senha

)


api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)

def validar_ti():
    """
    Permite acesso apenas para usuários TI.
    """

    if "usuario_id" not in session:
        abort(401)

    if session.get("perfil") != "TI":
        abort(403)

# Justificativa

@api.get("/justificativa/<int:id>")
def obter_justificativa(id):
    """
    Retorna uma justificativa em formato JSON.
    """

    justificativa = buscar_justificativa(id)

    return jsonify({

        "id": justificativa.id,

        "nome": justificativa.nome,

        "cargo": justificativa.cargo,

        "matricula": justificativa.matricula,

        "competencia": justificativa.competencia,

        "data": justificativa.data.strftime("%d/%m/%Y"),

        "hora_entrada": justificativa.hora_entrada.strftime("%H:%M"),

        "hora_saida": justificativa.hora_saida.strftime("%H:%M"),

        "justificativa": justificativa.justificativa,

        "assinatura": justificativa.assinatura,

        "criado_em": justificativa.criado_em.strftime("%d/%m/%Y %H:%M")

    })


@api.delete("/justificativa/<int:id>/excluir")
def excluir(id):
    """
    Realiza o Soft Delete de uma justificativa.
    """

    try:

        excluir_justificativa(id)

        return jsonify({

            "success": True,

            "message": "Justificativa arquivada com sucesso."

        })

    except HTTPException:
     raise

    except Exception as erro:

     return jsonify({

        "success": False,

        "message": str(erro)

    }), 500

@api.get("/justificativa/<int:id>/pdf")
def gerar_pdf_justificativa(id):
    """
    Gera o PDF da justificativa.
    """

    justificativa = buscar_justificativa(id)

    pasta_pdf = os.path.join(
        "static",
        "pdfs"
    )

    os.makedirs(
        pasta_pdf,
        exist_ok=True
    )

    caminho_pdf = os.path.join(
        pasta_pdf,
        f"justificativa_{id}.pdf"
    )

    gerar_pdf(
        justificativa,
        caminho_pdf
    )

    return send_file(
        caminho_pdf,
        as_attachment=True,
        download_name=f"Justificativa_{id}.pdf",
        mimetype="application/pdf"
    )

# Usuários

@api.get("/usuarios")
def listar_usuarios_api():
    """
    Retorna todos os usuários.
    """
    validar_ti()

    usuarios = listar_usuarios()

    return jsonify([

        {

            "id": usuario.id,

            "nome": usuario.nome,

            "email": usuario.email,

            "status": usuario.status,

            "perfil": usuario.perfil,

            "criado_em": usuario.criado_em.strftime("%d/%m/%Y")

        }

        for usuario in usuarios

    ])

@api.patch("/usuarios/<int:id>/ativar")
def ativar_usuario_api(id):
    """
    Ativa um usuário.
    """
    validar_ti()

    ativar_usuario(id)

    return jsonify({

        "success": True,

        "message": "Usuário ativado."

    })

@api.patch("/usuarios/<int:id>/bloquear")
def bloquear_usuario_api(id):
    """
    Bloqueia um usuário.
    """
    validar_ti()

    bloquear_usuario(id)

    return jsonify({

        "success": True,

        "message": "Usuário bloqueado."

    })

@api.patch("/usuarios/<int:id>/senha")
def redefinir_senha_api(id):
    """
    Redefine a senha do usuário.
    """
    validar_ti()

    dados = request.get_json()

    redefinir_senha(

        id,

        dados["senha"]

    )

    return jsonify({

        "success": True,

        "message": "Senha redefinida."

    })

