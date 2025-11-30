
document.addEventListener("DOMContentLoaded", () => {

  const formulario = document.querySelector("#contacto form");

  formulario.addEventListener("submit", (event) => {
    const nombre = document.getElementById("nombre").value.trim();
    const correo = document.getElementById("correo").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();


    if (nombre === "" || correo === "" || mensaje === "") {
      alert("Por favor completa todos los campos antes de enviar.");
      event.preventDefault(); // evita que el formulario se envíe
      return;
    }


    if (!correo.includes("@") || !correo.includes(".")) {
      alert("Por favor ingresa un correo válido.");
      event.preventDefault();
      return;
    }

    alert("Formulario enviado correctamente 🎉");
  });

});



const foto = document.querySelector(".foto");

foto.addEventListener("mouseenter", () => {
  foto.style.transform = "scale(1.05)";
  foto.style.transition = "0.3s";
});

foto.addEventListener("mouseleave", () => {
  foto.style.transform = "scale(1)";
});



window.addEventListener("load", () => {
  console.log("Sitio cargado correctamente ✔");
});
