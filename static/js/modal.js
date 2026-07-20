const abrirLogin =
    document.getElementById("abrirLogin");

const loginModal =
    document.getElementById("loginModal");

const cadastroModal =
    document.getElementById("cadastroModal");

const fecharLogin =
    document.getElementById("fecharLogin");

const fecharCadastro =
    document.getElementById("fecharCadastro");

const abrirCadastro =
    document.getElementById("abrirCadastro");


// ------------------
// Abrir Login
// ------------------

if (abrirLogin) {

    abrirLogin.addEventListener("click", (e) => {

        e.preventDefault();

        cadastroModal?.classList.remove("active");

        loginModal?.classList.add("active");

    });

}


// ------------------
// Fechar Login
// ------------------

if (fecharLogin) {

    fecharLogin.addEventListener("click", () => {

        loginModal?.classList.remove("active");

    });

}


// ------------------
// Abrir Cadastro
// ------------------

if (abrirCadastro) {

    abrirCadastro.addEventListener("click", (e) => {

        e.preventDefault();

        loginModal?.classList.remove("active");

        cadastroModal?.classList.add("active");

    });

}


// ------------------
// Fechar Cadastro
// ------------------

if (fecharCadastro) {

    fecharCadastro.addEventListener("click", () => {

        cadastroModal?.classList.remove("active");

    });

}


// ------------------
// Clique fora
// ------------------

window.addEventListener("click", (e) => {

    if (e.target === loginModal) {

        loginModal?.classList.remove("active");

    }

    if (e.target === cadastroModal) {

        cadastroModal?.classList.remove("active");

    }

});