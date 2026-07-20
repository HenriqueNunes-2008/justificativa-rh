const competencia =
    document.getElementById("competencia");

if (competencia) {

    competencia.addEventListener("input", () => {

        let valor =
            competencia.value
            .replace(/\D/g, "");

        if (valor.length > 2) {

            valor =
                valor.substring(0,2)
                + "/"
                + valor.substring(2,6);

        }

        competencia.value = valor;

    });

}


function mascaraHora(input) {

    input.addEventListener("input", () => {

        let valor =
            input.value
            .replace(/\D/g, "");

        if (valor.length > 2) {

            valor =
                valor.substring(0,2)
                + ":"
                + valor.substring(2,4);

        }

        input.value = valor;

    });

}


const entrada =
    document.getElementById("entrada");

const saida =
    document.getElementById("saida");


if (entrada) mascaraHora(entrada);

if (saida) mascaraHora(saida);