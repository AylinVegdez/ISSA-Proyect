
const botonDerecha = document.getElementById('derecha');
const botonAdivinar = document.getElementById('botondos');
const mostrarResultado = document.getElementById('resultado');
var cantidadPuntos = document.getElementById('puntos');


botonDerecha.addEventListener('click',()=> {
   numeroAdivinar = num_uno.value;
   numeroAdivinar.innerHTML;
   console.log(numeroAdivinar);
   num_uno.value = "";
});
botonAdivinar.addEventListener('click',() => {
    let i;
    let contador = 0;
    numeroParaAdivinar = num_dos.value;
    numeroParaAdivinar.innerHTML;
    if (numeroParaAdivinar == numeroAdivinar) {
        mostrarResultado.innerHTML = `${"Adivinaste"}`
        cantidadPuntos.innerHTML = `${contador++}`;

    } else {
        mostrarResultado.innerHTML = `${"Erraste"}`
    }
});