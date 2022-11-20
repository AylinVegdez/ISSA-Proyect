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
      Swal.fire('Guardado!', 'Cambios realizados', 'success')
    } else if (result.isDenied) {
      Swal.fire('Opps', 'Los cambios no fueron realizados', 'info')
    }
  })