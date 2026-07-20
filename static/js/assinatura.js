const canvas =
    document.getElementById("assinaturaCanvas");

if (canvas) {

    const ctx =
        canvas.getContext("2d");

    let desenhando = false;


    function ajustarCanvas() {

        canvas.width =
            canvas.offsetWidth;

        canvas.height =
            canvas.offsetHeight;

    }

    ajustarCanvas();

    window.addEventListener(
        "resize",
        ajustarCanvas
    );


    function iniciar(e) {

        desenhando = true;

        desenhar(e);

    }


    function parar() {

        desenhando = false;

        ctx.beginPath();

    }


    function desenhar(e) {

        if (!desenhando) return;

        const rect =
            canvas.getBoundingClientRect();

        const x =
            (e.clientX ||
            e.touches[0].clientX)
            - rect.left;

        const y =
            (e.clientY ||
            e.touches[0].clientY)
            - rect.top;

        ctx.lineWidth = 2;

        ctx.lineCap = "round";

        ctx.strokeStyle = "#000";

        ctx.lineTo(x, y);

        ctx.stroke();

        ctx.beginPath();

        ctx.moveTo(x, y);

    }


    canvas.addEventListener(
        "mousedown",
        iniciar
    );

    canvas.addEventListener(
        "mouseup",
        parar
    );

    canvas.addEventListener(
        "mousemove",
        desenhar
    );


    canvas.addEventListener(
        "touchstart",
        iniciar
    );

    canvas.addEventListener(
        "touchend",
        parar
    );

    canvas.addEventListener(
        "touchmove",
        desenhar
    );


    const limpar =
        document.getElementById(
            "limparAssinatura"
        );

    limpar.addEventListener(
        "click",
        () => {

            ctx.clearRect(
                0,
                0,
                canvas.width,
                canvas.height
            );

        }
    );

}
const form =
    document.getElementById("formJustificativa");

if(form){

    form.addEventListener("submit",()=>{

        const assinatura =
            canvas.toDataURL("image/png");

        document
        .getElementById("assinaturaInput")
        .value = assinatura;

    });

}