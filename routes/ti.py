from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for
)

ti = Blueprint(
    "ti",
    __name__
)


@ti.route("/ti")
def dashboard():

    if "usuario_id" not in session:

        return redirect(
            url_for("auth.login")
        )

    if session.get("perfil") != "TI":

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "ti.html"
    )