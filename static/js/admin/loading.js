export function bloquearBotao(botao) {

    botao.disabled = true;

    botao.dataset.textoOriginal = botao.innerHTML;

    botao.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        Excluindo...
    `;

}


export function liberarBotao(botao) {

    botao.disabled = false;

    botao.innerHTML = botao.dataset.textoOriginal;

}