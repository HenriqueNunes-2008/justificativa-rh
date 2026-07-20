from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
)

from database.services import (salvar_justificativa as salvar_justificativa_service)

justificativas = Blueprint(
    "justificativas",
    __name__
)


@justificativas.get("/")
def index():

    return render_template("index.html")


@justificativas.post("/nova-justificativa")
def salvar_justificativa():

    salvar_justificativa_service(request.form)

    flash(
        "Justificativa enviada com sucesso!",
        "success"
    )

    return redirect(
        url_for("justificativas.index")
    )