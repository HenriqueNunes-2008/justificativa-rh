from datetime import datetime
from flask import abort
from sqlalchemy import func

from database.database import db
from database.models import Justificativa

from utils.assinatura import salvar_assinatura


def salvar_justificativa(formulario):
    """
    Salva uma nova justificativa.
    """

    caminho_assinatura = salvar_assinatura(
        formulario["assinatura"]
    )

    justificativa = Justificativa(

        nome=formulario["nome"],

        cargo=formulario["cargo"],

        matricula=formulario["matricula"],

        competencia=formulario["competencia"],

        data=datetime.strptime(
            formulario["data"],
            "%Y-%m-%d"
        ).date(),

        hora_entrada=datetime.strptime(
            formulario["hora_entrada"],
            "%H:%M"
        ).time(),

        hora_saida=datetime.strptime(
            formulario["hora_saida"],
            "%H:%M"
        ).time(),

        justificativa=formulario["justificativa"],

        assinatura=caminho_assinatura

    )

    db.session.add(justificativa)

    db.session.commit()

    return justificativa


def listar_justificativas():
    """
    Retorna apenas justificativas ativas.
    """

    return (

        Justificativa.query

        .filter_by(ativo=True)

        .order_by(
            Justificativa.criado_em.desc()
        )

        .all()

    )


def buscar_justificativa(id, incluir_excluidas=False):

    """
    Busca uma justificativa pelo ID.
    """

    consulta = Justificativa.query.filter_by(id=id)

    if not incluir_excluidas:
        consulta = consulta.filter_by(ativo=True)

    justificativa = consulta.first()

    if justificativa is None:
        abort(404)

    return justificativa


def buscar_por_competencia(competencia):
    """
    Lista justificativas por competência.
    """

    return (

        Justificativa.query

        .filter_by(
            ativo=True,
            competencia=competencia
        )

        .order_by(
            Justificativa.data.desc()
        )

        .all()

    )


def pesquisar_justificativas(texto):
    """
    Pesquisa por nome ou matrícula.
    """

    pesquisa = f"%{texto}%"

    return (

        Justificativa.query

        .filter(

            Justificativa.ativo.is_(True),

            (

                Justificativa.nome.like(pesquisa)

                |

                Justificativa.matricula.like(pesquisa)

            )

        )

        .order_by(
            Justificativa.data.desc()
        )

        .all()

    )


def listar_competencias():
    """
    Lista todas as competências existentes.
    """

    return (

        db.session.query(
            Justificativa.competencia
        )

        .filter(
            Justificativa.ativo.is_(True)
        )

        .distinct()

        .order_by(
            Justificativa.competencia.desc()
        )

        .all()

    )


def total_justificativas():
    """
    Total de registros ativos.
    """

    return (

        Justificativa.query

        .filter_by(
            ativo=True
        )

        .count()

    )


def registros_hoje():
    """
    Quantidade de registros criados hoje.
    """

    return (

        Justificativa.query

        .filter(

            Justificativa.ativo.is_(True),

            func.date(
                Justificativa.criado_em
            ) == datetime.today().date()

        )

        .count()

    )


def excluir_justificativa(id):
    """
    Soft Delete.
    """

    justificativa = buscar_justificativa(
        id,
        incluir_excluidas=True
    )

    if not justificativa.ativo:
        return justificativa

    justificativa.ativo = False

    justificativa.excluido_em = datetime.utcnow()

    db.session.commit()

    return justificativa

def listar_excluidas():
    """
    Lista justificativas arquivadas.
    """

    return (

        Justificativa.query

        .filter_by(
            ativo=False
        )

        .order_by(
            Justificativa.excluido_em.desc()
        )

        .all()

    )


def restaurar_justificativa(id):
    """
    Restaura uma justificativa arquivada.
    """

    justificativa = buscar_justificativa(
    id,
    incluir_excluidas=True
)

    justificativa.ativo = True

    justificativa.excluido_em = None

    db.session.commit()

    return justificativa