# Justificativa RH

Sistema web para registrar e administrar justificativas de ponto. Colaboradores preenchem a ocorrência e assinam digitalmente; o RH consulta, filtra, arquiva e gera PDFs; e a equipe de TI administra os acessos.

## Funcionalidades

- Registro de justificativas com dados do colaborador, data, horários, competência e descrição.
- Captura de assinatura em canvas, com suporte a mouse e toque, e armazenamento no Cloudinary.
- Painel de RH com indicadores, pesquisa por nome ou matrícula, filtro por competência, consulta detalhada, geração de PDF e arquivamento lógico.
- Autenticação com senhas protegidas por hash e perfis `RH` e `TI`.
- Painel de TI para listar usuários, aprovar cadastros, bloquear contas e redefinir senhas.

## Tecnologias

- Python 3 e Flask
- SQLAlchemy / Flask-SQLAlchemy
- PostgreSQL (neon)
- Cloudinary para as imagens das assinaturas
- ReportLab para geração dos PDFs
- Jinja2, CSS e JavaScript modular no front-end

## Estrutura

```text
app.py                       # Fábrica e inicialização da aplicação
config.py                    # Variáveis de ambiente e configuração
routes/                      # Blueprints e rotas HTTP
database/models.py           # Modelos Usuario e Justificativa
database/services/           # Regras de negócio e acesso a dados
templates/                   # Páginas Jinja2 e componentes
static/                      # CSS, JavaScript, imagens e PDFs gerados
utils/assinatura.py          # Upload de assinaturas ao Cloudinary
```

## Pré-requisitos

- Python 3.10 ou superior
- Uma instância PostgreSQL ou Neon, caso não seja usado SQLite localmente
- Uma conta Cloudinary, pois toda justificativa exige o upload da assinatura

## Configuração e execução

1. Crie e ative um ambiente virtual:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:

   ```powershell
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto:

   ```env
   SECRET_KEY=uma-chave-secreta-longa-e-aleatoria
   DATABASE_URL=sqlite:///justificativas.db
   CLOUDINARY_CLOUD_NAME=seu_cloud_name
   CLOUDINARY_API_KEY=sua_api_key
   CLOUDINARY_API_SECRET=seu_api_secret
   ```

   Para PostgreSQL, use uma URL como:

   ```env
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/justificativa_rh
   ```

4. Inicie a aplicação:

   ```powershell
   py app.py
   ```

5. Acesse `http://127.0.0.1:5000`.

As tabelas são criadas automaticamente na primeira inicialização, por meio de `db.create_all()`.

## Primeiro usuário de TI

O cadastro público cria somente usuários do perfil `RH` com status `PENDENTE`. Portanto, para operar o sistema pela primeira vez, crie um usuário `TI` diretamente no banco ou pelo shell Flask:

```powershell
$env:FLASK_APP = "app"
flask shell
```

```python
from app import app
from database.database import db
from database.models import Usuario
from werkzeug.security import generate_password_hash

with app.app_context():
    usuario = Usuario(
        nome="Administrador TI",
        email="ti@empresa.com",
        senha=generate_password_hash("troque-esta-senha"),
        status="ATIVO",
        perfil="TI",
    )
    db.session.add(usuario)
    db.session.commit()
```

Depois do login em `/login`, um usuário TI é encaminhado a `/ti`; usuários RH ativos são encaminhados a `/admin`.

## Rotas principais

| Método | Rota | Finalidade |
| --- | --- | --- |
| `GET` | `/` | Formulário de justificativa |
| `POST` | `/nova-justificativa` | Salva uma justificativa e a assinatura |
| `POST` | `/login` | Autentica o usuário |
| `POST` | `/cadastro` | Solicita cadastro de usuário RH |
| `GET` | `/admin` | Painel RH |
| `GET` | `/ti` | Painel de gestão de usuários |
| `GET` | `/api/justificativa/<id>` | Dados de uma justificativa em JSON |
| `DELETE` | `/api/justificativa/<id>/excluir` | Arquiva uma justificativa (soft delete) |
| `GET` | `/api/justificativa/<id>/pdf` | Gera e baixa o PDF |
| `GET` | `/api/usuarios` | Lista usuários — requer perfil TI |
| `PATCH` | `/api/usuarios/<id>/ativar` | Ativa usuário — requer perfil TI |
| `PATCH` | `/api/usuarios/<id>/bloquear` | Bloqueia usuário — requer perfil TI |
| `PATCH` | `/api/usuarios/<id>/senha` | Redefine senha — requer perfil TI |

## Dados persistidos

- `usuarios`: nome, e-mail, hash da senha, perfil (`RH` ou `TI`), status (`PENDENTE`, `ATIVO` ou `BLOQUEADO`) e data de criação.
- `justificativas`: dados do colaborador e da ocorrência, URL da assinatura, datas de criação/atualização e estado de arquivamento.

O arquivamento de justificativas é um *soft delete*: o registro permanece no banco com `ativo=False` e `excluido_em` preenchido.

## PDFs e assinaturas

Ao gerar um PDF, o sistema salva o arquivo em `static/pdfs/` e inclui a assinatura hospedada no Cloudinary. Esses PDFs são artefatos gerados em execução e não devem ser versionados. As credenciais ficam apenas no `.env`, que já é ignorado pelo Git.

## Produção

O projeto inclui `gunicorn` nas dependências. Após configurar as variáveis de ambiente e usar um banco PostgreSQL, uma forma de iniciá-lo é:

```bash
gunicorn app:app
```

Antes da publicação, defina uma `SECRET_KEY` forte, proteja as credenciais do Cloudinary e execute a aplicação sem o modo de depuração.
