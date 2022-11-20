const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: 'btn btn-success',
      cancelButton: 'btn btn-danger'
    },
    buttonsStyling: false
  })
  
  swalWithBootstrapButtons.fire({
    title: '¿Estas seguro?',
    text: "No podrás revertir esta accioón",
    icon: 'warning',
    showCancelButton: true,
    cancelButtonText: 'No,  Cancelar',
    confirmButtonText: 'Si,  Eliminar',
  }).then((result) => {
    if (result.isConfirmed) {
      swalWithBootstrapButtons.fire(
        'Eliminado!',
        'El registro ha sido eliminado.',
        'success'
      )
    } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Operación Cancelada',
        ' Se ha interrumpido la acción ',
        'error'
      )
    }
  })