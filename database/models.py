from datetime import datetime

from database.database import db


class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="PENDENTE"
    )

    perfil = db.Column(
        db.String(20),
        nullable=False,
        default="RH"
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Justificativa(db.Model):

    __tablename__ = "justificativas"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(150), nullable=False)

    cargo = db.Column(db.String(100), nullable=False)

    matricula = db.Column(db.String(50), nullable=False)

    competencia = db.Column(db.String(20), nullable=False)

    data = db.Column(db.Date, nullable=False)

    hora_entrada = db.Column(db.Time, nullable=False)

    hora_saida = db.Column(db.Time, nullable=False)

    justificativa = db.Column(db.Text, nullable=False)

    assinatura = db.Column(
        db.String(255),
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    excluido_em = db.Column(
        db.DateTime,
        nullable=True
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

atualizado_em = db.Column(
    db.DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow
)