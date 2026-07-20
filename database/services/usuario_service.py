from werkzeug.security import generate_password_hash

from database.database import db

from database.models import Usuario


def listar_usuarios():
    """
    Retorna todos os usuários.
    """

    return (

        Usuario.query

        .order_by(
            Usuario.nome.asc()
        )

        .all()

    )


def buscar_usuario(id):
    """
    Busca um usuário pelo ID.
    """

    return Usuario.query.get_or_404(id)


def ativar_usuario(id):
    """
    Ativa um usuário.
    """

    usuario = buscar_usuario(id)

    usuario.status = "ATIVO"

    db.session.commit()

    return usuario


def bloquear_usuario(id):
    """
    Bloqueia um usuário.
    """

    usuario = buscar_usuario(id)

    usuario.status = "BLOQUEADO"

    db.session.commit()

    return usuario


def redefinir_senha(
    id,
    nova_senha
):
    """
    Redefine a senha do usuário.
    """

    usuario = buscar_usuario(id)

    usuario.senha = generate_password_hash(
        nova_senha
    )

    db.session.commit()

    return usuario