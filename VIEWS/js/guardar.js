
function Guardar()
{
  Swal.fire({
    title: '¿Desea Guardar los cambios?',
    showDenyButton: true,
    color: '#5FAD2D',
    confirmButtonText: 'Confirmar',
    denyButtonText: `No Guardar`,
    icon:'question',
    position: 'center',
    allowOutsideClick:false,
    allowEscapeKey:false,
    alloeWnterKey:false,
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      Swal.fire('¡Guardado!', 'Cambios realizados', 'success')
    } else if (result.isDenied) {
      Swal.fire('Opps', 'Los cambios no fueron realizados', 'info')
    }
  })
}

function Actualizar()
{
  Swal.fire({
    title: '¿Desea modificar el registro?',
    showDenyButton: true,
    color: '#5FAD2D',
    confirmButtonText: 'Confirmar',
    denyButtonText: `Cancelar`,
    icon:'question',
    position: 'center',
    allowOutsideClick:false,
    allowEscapeKey:false,
    alloeWnterKey:false,
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      Swal.fire('¡Actualizado!', 'Cambios realizados', 'success')
    } else if (result.isDenied) {
      Swal.fire('Opps', 'Los cambios no fueron realizados', 'info')
    }
  })
}

function Noautorizado()
{
  Swal.fire({
    icon: 'error',
    title: 'NO APROBADO',
    text: 'No se autorizaron las calificaciones',
  })
}

function Sesion()
{
  Swal.fire({
    title: 'Ingrese a la página',
    showDenyButton: true,
    color: '#5FAD2D',
    confirmButtonText: 'Usuario',
    denyButtonText: `Admin`,
    icon:'question',
    position: 'center',
    allowOutsideClick:false,
    allowEscapeKey:false,
    alloeWnterKey:false,
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      Swal.fire(window.location = "Menuusuario.html")
    } else if (result.isDenied) {
      Swal.fire(window.location = "adminMenuP.html")
    }
  })
}