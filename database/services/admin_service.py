from datetime import datetime

from sqlalchemy import func

from database.database import db
from database.models import Justificativa


def listar_justificativas():
    """
    Lista todas as justificativas.
    """

    return (

        Justificativa.query

        .order_by(
            Justificativa.criado_em.desc()
        )

        .all()

    )


def listar_competencias():
    """
    Lista competências sem repetição.
    """

    return (

        db.session.query(
            Justificativa.competencia
        )

        .distinct()

        .order_by(
            Justificativa.competencia.desc()
        )

        .all()

    )


def buscar_por_competencia(competencia):

    return (

        Justificativa.query

        .filter_by(
            competencia=competencia
        )

        .order_by(
            Justificativa.data.desc()
        )

        .all()

    )


def pesquisar_justificativas(texto):

    pesquisa = f"%{texto}%"

    return (

        Justificativa.query

        .filter(

            (Justificativa.nome.like(pesquisa))

            |

            (Justificativa.matricula.like(pesquisa))

        )

        .order_by(
            Justificativa.data.desc()
        )

        .all()

    )


def total_justificativas():

    return Justificativa.query.count()


def registros_hoje():

    return (

        Justificativa.query

        .filter(

            func.date(
                Justificativa.criado_em
            ) == datetime.today().date()

        )

        .count()

    )