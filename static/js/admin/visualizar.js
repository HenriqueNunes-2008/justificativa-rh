import { buscarJustificativa } from "../services/api.js";

export function iniciarVisualizacao() {

    const modal = document.getElementById("visualizarModal");
    const conteudo = document.getElementById("conteudoModal");
    const fechar = document.getElementById("fecharVisualizar");

    document.addEventListener("click", async (evento) => {

        const botao = evento.target.closest(".btn-view");

        if (!botao) return;

        const id = botao.dataset.id;

        try {

            const j = await buscarJustificativa(id);

            conteudo.innerHTML = `

                <div class="info-grid">

                    <div class="info">
                        <label>Nome</label>
                        <span>${j.nome}</span>
                    </div>

                    <div class="info">
                        <label>Cargo</label>
                        <span>${j.cargo}</span>
                    </div>

                    <div class="info">
                        <label>Matrícula</label>
                        <span>${j.matricula}</span>
                    </div>

                    <div class="info">
                        <label>Competência</label>
                        <span>${j.competencia}</span>
                    </div>

                    <div class="info">
                        <label>Data</label>
                        <span>${j.data}</span>
                    </div>

                    <div class="info">
                        <label>Entrada</label>
                        <span>${j.hora_entrada}</span>
                    </div>

                    <div class="info">
                        <label>Saída</label>
                        <span>${j.hora_saida}</span>
                    </div>

                </div>

                <div class="justificativa-box">

                    <strong>Justificativa</strong>

                    <p>${j.justificativa}</p>

                </div>

                <div class="assinatura">

                    <h3>Assinatura</h3>

                    <img
                        src="/static/${j.assinatura}"
                        alt="Assinatura">

                </div>

            `;

            modal.classList.add("active");

        }

        catch (erro) {

            console.error(erro);

            alert("Não foi possível carregar a justificativa.");

        }

    });

    fechar.addEventListener("click", () => {

        modal.classList.remove("active");

    });

    modal.addEventListener("click", (evento) => {

        if (evento.target === modal) {

            modal.classList.remove("active");

        }

    });

}