from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database.database import db
from database.models import Usuario


auth = Blueprint(
    "auth",
    __name__
)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Login do usuário.
    """

    if request.method == "POST":

        email = request.form["email"].strip().lower()

        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(
            email=email
        ).first()

        if usuario is None:

            flash(
                "E-mail ou senha inválidos.",
                "error"
            )

            return redirect(
                url_for(
                    "justificativas.index",
                    login="1"
                )
            )

        if not check_password_hash(
            usuario.senha,
            senha
        ):

            flash(
                "E-mail ou senha inválidos.",
                "error"
            )

            return redirect(
                url_for(
                    "justificativas.index",
                    login="1"
                )
            )

        if usuario.status == "PENDENTE":

            flash(
                "Seu cadastro ainda não foi aprovado.",
                "warning"
            )

            return redirect(
                url_for(
                    "justificativas.index",
                    login="1"
                )
            )

        if usuario.status == "BLOQUEADO":

            flash(
                "Conta bloqueada.",
                "error"
            )

            return redirect(
                url_for(
                    "justificativas.index",
                    login="1"
                )
            )

        session["usuario_id"] = usuario.id

        session["usuario_nome"] = usuario.nome

        session["perfil"] = usuario.perfil

        if usuario.perfil == "TI":

            return redirect(
                url_for("ti.dashboard")
            )

        return redirect(
            url_for("admin.painel")
        )

    return redirect(
        url_for("justificativas.index")
    )


@auth.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    """
    Cadastro de novo usuário.
    """

    if request.method == "POST":

        nome = request.form["nome"].strip()

        email = request.form["email"].strip().lower()

        senha = request.form["senha"]

        existe = Usuario.query.filter_by(
            email=email
        ).first()

        if existe:

            flash(
                "E-mail já cadastrado.",
                "error"
            )

            return redirect(
                url_for(
                    "justificativas.index",
                    cadastro="1"
                )
            )

        usuario = Usuario(

            nome=nome,

            email=email,

            senha=generate_password_hash(senha),

            status="PENDENTE",

            perfil="RH"

        )

        db.session.add(usuario)

        db.session.commit()

        flash(
            "Cadastro realizado com sucesso. Aguarde aprovação do administrador.",
            "success"
        )

        return redirect(
            url_for(
                "justificativas.index",
                login="1"
            )
        )

    return redirect(
        url_for("justificativas.index")
    )


@auth.get("/logout")
def logout():
    """
    Encerra a sessão do usuário.
    """

    session.clear()

    flash(
        "Sessão encerrada.",
        "success"
    )

    return redirect(
        url_for(
            "justificativas.index",
            login="1"
        )
    )