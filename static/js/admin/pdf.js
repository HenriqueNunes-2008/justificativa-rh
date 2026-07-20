export function iniciarPdf() {

    document.addEventListener(

        "click",

        (evento) => {

            const botao =
                evento.target.closest(".btn-pdf");

            if (!botao) {

                return;

            }

            const id = botao.dataset.id;

            window.open(

                `/api/justificativa/${id}/pdf`,

                "_blank"

            );

        }

    );

}