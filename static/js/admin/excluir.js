import { excluirJustificativa } from "../services/api.js";

import { mostrarToast } from "./toast.js";

import {
    bloquearBotao,
    liberarBotao
} from "./loading.js";


export function iniciarExclusao() {

    const modal = document.getElementById("modalExcluir");

    const cancelar = document.getElementById("cancelarExcluir");

    const confirmar = document.getElementById("confirmarExcluir");

    let justificativaAtual = null;


    document.addEventListener("click", (evento) => {

        const botao = evento.target.closest(".btn-delete");

        if (!botao) return;

        justificativaAtual = botao.dataset.id;

        modal.classList.add("active");

    });


    cancelar.addEventListener("click", () => {

        modal.classList.remove("active");

    });


    modal.addEventListener("click", (evento) => {

        if (evento.target === modal) {

            modal.classList.remove("active");

        }

    });


    confirmar.addEventListener("click", async () => {

        if (!justificativaAtual) return;

        bloquearBotao(confirmar);

        try {

            await excluirJustificativa(justificativaAtual);

            document
                .getElementById(`linha-${justificativaAtual}`)
                ?.remove();

            mostrarToast(
                "Justificativa arquivada com sucesso."
            );

            modal.classList.remove("active");

        }

        catch (erro) {

            mostrarToast(
                erro.message,
                "error"
            );

        }

        finally {

            liberarBotao(confirmar);

        }

    });

}