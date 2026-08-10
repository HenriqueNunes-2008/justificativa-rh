const canvas = document.getElementById("assinaturaCanvas");
const modalCanvas = document.getElementById("assinaturaModalCanvas");
const assinaturaInput = document.getElementById("assinaturaInput");
const form = document.getElementById("formJustificativa");
const assinaturaModal = document.getElementById("assinaturaModal");
const abrirAssinatura = document.getElementById("abrirAssinatura");
const fecharAssinaturaModal = document.getElementById("fecharAssinaturaModal");
const cancelarAssinatura = document.getElementById("cancelarAssinatura");
const confirmarAssinatura = document.getElementById("confirmarAssinatura");
const limparAssinatura = document.getElementById("limparAssinatura");
const limparAssinaturaModal = document.getElementById("limparAssinaturaModal");

function ajustarCanvas(canvasElement) {
    if (!canvasElement) return;

    canvasElement.width = canvasElement.offsetWidth;
    canvasElement.height = canvasElement.offsetHeight;
}

function setupCanvas(canvasElement) {
    if (!canvasElement) return null;

    const ctx = canvasElement.getContext("2d");
    let desenhando = false;

    function iniciar(e) {
        e.preventDefault();
        desenhando = true;
        desenhar(e);
    }

    function parar(e) {
        if (e) e.preventDefault();
        desenhando = false;
        ctx.beginPath();
    }

    function desenhar(e) {
        if (!desenhando) return;
        if (e.cancelable) {
            e.preventDefault();
        }

        const rect = canvasElement.getBoundingClientRect();
        const x = ((e.clientX || (e.touches && e.touches[0].clientX)) || 0) - rect.left;
        const y = ((e.clientY || (e.touches && e.touches[0].clientY)) || 0) - rect.top;

        ctx.lineWidth = 2;
        ctx.lineCap = "round";
        ctx.strokeStyle = "#000";
        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x, y);
    }

    canvasElement.addEventListener("mousedown", iniciar);
    canvasElement.addEventListener("mouseup", parar);
    canvasElement.addEventListener("mousemove", desenhar);
    canvasElement.addEventListener("mouseleave", parar);

    canvasElement.addEventListener("touchstart", iniciar, { passive: false });
    canvasElement.addEventListener("touchend", parar);
    canvasElement.addEventListener("touchmove", desenhar, { passive: false });

    return {
        ctx,
        ajustar: () => ajustarCanvas(canvasElement),
        clear: () => ctx.clearRect(0, 0, canvasElement.width, canvasElement.height),
        toDataURL: () => canvasElement.toDataURL("image/png"),
        loadFromDataURL: (dataURL) => {
            if (!dataURL) return;
            const image = new Image();
            image.onload = () => {
                ajustarCanvas(canvasElement);
                ctx.clearRect(0, 0, canvasElement.width, canvasElement.height);
                ctx.drawImage(image, 0, 0, canvasElement.width, canvasElement.height);
            };
            image.src = dataURL;
        }
    };
}

const desktopCanvas = setupCanvas(canvas);
const mobileCanvas = setupCanvas(modalCanvas);

if (desktopCanvas) {
    desktopCanvas.ajustar();
}

window.addEventListener("resize", () => {
    if (desktopCanvas) desktopCanvas.ajustar();
    if (mobileCanvas && assinaturaModal && assinaturaModal.classList.contains("active")) {
        mobileCanvas.ajustar();
        if (assinaturaInput && assinaturaInput.value) {
            mobileCanvas.loadFromDataURL(assinaturaInput.value);
        }
    }
});

function abrirModalAssinatura() {
    if (!assinaturaModal) return;
    assinaturaModal.classList.add("active");
    document.body.classList.add("signature-modal-open");
    if (mobileCanvas) {
        mobileCanvas.ajustar();
        if (assinaturaInput && assinaturaInput.value) {
            mobileCanvas.loadFromDataURL(assinaturaInput.value);
        }
    }
}

function fecharModalAssinatura() {
    if (!assinaturaModal) return;
    assinaturaModal.classList.remove("active");
    document.body.classList.remove("signature-modal-open");
}

if (abrirAssinatura) {
    abrirAssinatura.addEventListener("click", abrirModalAssinatura);
}

if (fecharAssinaturaModal) {
    fecharAssinaturaModal.addEventListener("click", fecharModalAssinatura);
}

if (cancelarAssinatura) {
    cancelarAssinatura.addEventListener("click", fecharModalAssinatura);
}

if (limparAssinatura) {
    limparAssinatura.addEventListener("click", () => {
        if (desktopCanvas) desktopCanvas.clear();
    });
}

if (limparAssinaturaModal) {
    limparAssinaturaModal.addEventListener("click", () => {
        if (mobileCanvas) mobileCanvas.clear();
    });
}

if (confirmarAssinatura) {
    confirmarAssinatura.addEventListener("click", () => {
        if (!assinaturaInput) return;
        if (mobileCanvas) {
            assinaturaInput.value = mobileCanvas.toDataURL();
        }
        fecharModalAssinatura();
    });
}

if (assinaturaModal) {
    assinaturaModal.addEventListener("click", (event) => {
        if (event.target === assinaturaModal) {
            fecharModalAssinatura();
        }
    });
}

if (form) {
    form.addEventListener("submit", () => {
        const assinaturaValor = assinaturaInput && assinaturaInput.value ? assinaturaInput.value : desktopCanvas ? desktopCanvas.toDataURL() : "";
        if (assinaturaInput) {
            assinaturaInput.value = assinaturaValor;
        }
    });
}