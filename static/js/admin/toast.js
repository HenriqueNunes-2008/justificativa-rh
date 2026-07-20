export function mostrarToast(
    mensagem,
    tipo = "success"
) {

    const toast = document.createElement("div");

    toast.className = `toast ${tipo}`;

    toast.textContent = mensagem;

    document.body.appendChild(toast);

    requestAnimationFrame(() => {
        toast.classList.add("show");
    });

    setTimeout(() => {

        toast.classList.remove("show");

        setTimeout(() => {
            toast.remove();
        }, 300);

    }, 3000);

}