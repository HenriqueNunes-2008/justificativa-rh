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

const recuperacaoModal =
    document.getElementById("recuperacaoModal");

const abrirRecuperacao =
    document.getElementById("abrirRecuperacao");

const fecharRecuperacao =
    document.getElementById("fecharRecuperacao");

const voltarLoginRecuperacao =
    document.getElementById("voltarLoginRecuperacao");

const abrirModal = (modal) => {

    if (!modal) return;

    loginModal?.classList.remove("active");
    cadastroModal?.classList.remove("active");
    recuperacaoModal?.classList.remove("active");

    modal.classList.add("active");

};

const fecharModalAtual = () => {
    loginModal?.classList.remove("active");
    cadastroModal?.classList.remove("active");
    recuperacaoModal?.classList.remove("active");
};


// ------------------
// Abrir Login
// ------------------

if (abrirLogin) {

    abrirLogin.addEventListener("click", (e) => {

        e.preventDefault();

        abrirModal(loginModal);

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

        abrirModal(cadastroModal);

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
// Abrir recuperação de senha
// ------------------

if (abrirRecuperacao) {

    abrirRecuperacao.addEventListener("click", (e) => {

        e.preventDefault();

        abrirModal(recuperacaoModal);

    });

}


if (fecharRecuperacao) {

    fecharRecuperacao.addEventListener("click", () => {

        recuperacaoModal?.classList.remove("active");

        loginModal?.classList.add("active");

    });

}

if (voltarLoginRecuperacao) {

    voltarLoginRecuperacao.addEventListener("click", () => {

        recuperacaoModal?.classList.remove("active");
        loginModal?.classList.add("active");

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

    if (e.target === recuperacaoModal) {

        recuperacaoModal?.classList.remove("active");

    }

});

const parametros =
    new URLSearchParams(
        window.location.search
    );

if (parametros.get("login") === "1") {

    fecharModalAtual();
    loginModal?.classList.add("active");

}

if (parametros.get("cadastro") === "1") {

    fecharModalAtual();
    cadastroModal?.classList.add("active");

}

if (parametros.get("recuperacao") === "1") {

    fecharModalAtual();
    recuperacaoModal?.classList.add("active");

}