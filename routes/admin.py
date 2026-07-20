from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for
)

from database.services import (

    listar_justificativas,

    listar_competencias,

    buscar_por_competencia,

    pesquisar_justificativas,

    total_justificativas,

    registros_hoje

)

admin = Blueprint(
    "admin",
    __name__
)


@admin.route("/admin")
def painel():

    if "usuario_id" not in session:

        return redirect(
            url_for("auth.login")
        )
    
    if session.get("perfil") != "RH":

        return redirect(
            url_for("auth.login")
        )

    competencia = request.args.get("competencia")

    pesquisa = request.args.get("q")

    if pesquisa:

        justificativas = pesquisar_justificativas(
            pesquisa
        )

    elif competencia:

        justificativas = buscar_por_competencia(
            competencia
        )

    else:

        justificativas = listar_justificativas()


    competencias = listar_competencias()

    total = total_justificativas()

    hoje = registros_hoje()

    return render_template(

        "admin.html",

        justificativas=justificativas,

        competencias=competencias,

        total=total,

        hoje=hoje,

        competencia_atual=competencia

    )