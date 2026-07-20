document
.querySelectorAll(".toggle-password")
.forEach((icone) => {

    icone.addEventListener("click", () => {

        const input =
            document.getElementById(
                icone.dataset.target
            );

        if (input.type === "password") {

            input.type = "text";

            icone.classList.remove("fa-eye");

            icone.classList.add("fa-eye-slash");

        }

        else {

            input.type = "password";

            icone.classList.remove("fa-eye-slash");

            icone.classList.add("fa-eye");

        }

    });

});