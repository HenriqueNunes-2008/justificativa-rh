const abrirLogout =
    document.getElementById(
        "abrirLogout"
    );

const logoutModal =
    document.getElementById(
        "logoutModal"
    );

const cancelarLogout =
    document.getElementById(
        "cancelarLogout"
    );


// ------------------
// Abrir modal
// ------------------

if (abrirLogout) {

    abrirLogout.addEventListener(

        "click",

        () => {

            logoutModal?.classList.add(
                "active"
            );

        }

    );

}


// ------------------
// Cancelar
// ------------------

if (cancelarLogout) {

    cancelarLogout.addEventListener(

        "click",

        () => {

            logoutModal?.classList.remove(
                "active"
            );

        }

    );

}


// ------------------
// Clique fora
// ------------------

window.addEventListener(

    "click",

    (evento) => {

        if (evento.target === logoutModal) {

            logoutModal?.classList.remove(
                "active"
            );

        }

    }

);