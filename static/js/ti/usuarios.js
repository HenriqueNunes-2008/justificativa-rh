import {
    mostrarToast
} from "../admin/toast.js";

let usuarioSelecionado = null;

const modalSenha =
    document.getElementById("redefinirSenhaModal");

const inputNovaSenha =
    document.getElementById("novaSenha");

const fecharModalSenha =
    document.getElementById("fecharRedefinirSenha");

const salvarNovaSenha =
    document.getElementById("salvarNovaSenha");


async function carregarUsuarios() {

    const tbody =
        document.getElementById("usuariosTable");

    try {

        const resposta =
            await fetch("/api/usuarios");

        const usuarios =
            await resposta.json();

        tbody.innerHTML = "";

        if (usuarios.length === 0) {

            tbody.innerHTML = `

                <tr>

                    <td colspan="5">

                        Nenhum usuário encontrado.

                    </td>

                </tr>

            `;

            return;

        }

        let totalPendentes = 0;
        let totalBloqueados = 0;

        usuarios.forEach(usuario => {

            if (usuario.status === "PENDENTE") {

                totalPendentes++;

            }

            if (usuario.status === "BLOQUEADO") {

                totalBloqueados++;

            }

            tbody.innerHTML += `

                <tr>

                    <td>${usuario.nome}</td>

                    <td>${usuario.email}</td>

                    <td>${usuario.status}</td>

                    <td>${usuario.perfil}</td>

                    <td>

                        <button
                            class="btn-reset"
                            data-id="${usuario.id}">

                            Senha

                        </button>

                        ${
                            usuario.status === "ATIVO"

                            ?

                            `

                            <button
                                class="btn-bloquear"
                                data-id="${usuario.id}">

                                Bloquear

                            </button>

                            `

                            :

                            `

                            <button
                                class="btn-ativar"
                                data-id="${usuario.id}">

                                Ativar

                            </button>

                            `
                        }

                    </td>

                </tr>

            `;

        });

        document.getElementById(
            "totalUsuarios"
        ).textContent = usuarios.length;

        document.getElementById(
            "usuariosPendentes"
        ).textContent = totalPendentes;

        document.getElementById(
            "usuariosBloqueados"
        ).textContent = totalBloqueados;

    }

    catch (erro) {

        tbody.innerHTML = `

            <tr>

                <td colspan="5">

                    Erro ao carregar usuários.

                </td>

            </tr>

        `;

        console.error(erro);

    }

}


document.addEventListener(

    "click",

    async (evento) => {

        const reset =
            evento.target.closest(".btn-reset");

        if (reset) {

            usuarioSelecionado =
                reset.dataset.id;

            inputNovaSenha.value = "";

            modalSenha.classList.add("active");

            return;

        }

        const ativar =
            evento.target.closest(".btn-ativar");

        if (ativar) {

            await fetch(

                `/api/usuarios/${ativar.dataset.id}/ativar`,

                {
                    method: "PATCH"
                }

            );
            
            mostrarToast(
                "Usuário ativado."
            )

            carregarUsuarios();

            return;

        }

        const bloquear =
            evento.target.closest(".btn-bloquear");

        if (bloquear) {

            await fetch(

                `/api/usuarios/${bloquear.dataset.id}/bloquear`,

                {
                    method: "PATCH"
                }

            );

            mostrarToast(
                "Uusário bloqueado.",
                "warning"
            )

            carregarUsuarios();

        }

    }

);


salvarNovaSenha.addEventListener(

    "click",

    async () => {

        const novaSenha =
            inputNovaSenha.value.trim();

        if (novaSenha.length < 6) {

            mostrarToast(
                "A senha deve possuir pelo menos 6 caracteres.",
                "warning"
            );

            return;

        }

        const resposta =
            await fetch(

                `/api/usuarios/${usuarioSelecionado}/senha`,

                {

                    method: "PATCH",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify({

                        senha: novaSenha

                    })

                }

            );

        const dados =
            await resposta.json();

        if (dados.success) {

            modalSenha.classList.remove("active");

            inputNovaSenha.value = "";

            mostrarToast(
                "Senha redefinida com sucesso!"
            );

            carregarUsuarios();

        }

        else {

            mostrarToast(
                "Erro ao redefinir senha.",
                "error"
            );

        }

    }

);


fecharModalSenha.addEventListener(

    "click",

    () => {

        modalSenha.classList.remove("active");

    }

);


window.addEventListener(

    "click",

    (evento) => {

        if (evento.target === modalSenha) {

            modalSenha.classList.remove("active");

        }

    }

);


carregarUsuarios();