function Eliminar()
{
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: 'btn btn-success',
      cancelButton: 'btn btn-danger'
    },
    buttonsStyling: false
  })
  
  swalWithBootstrapButtons.fire({
    title: '¿Estás seguro?',
    text: "No podrás revertir esta acción",
    icon: 'warning',
    showCancelButton: true,
    cancelButtonText: 'No. Cancelar',
    confirmButtonText: 'Sí. Eliminar',
  }).then((result) => {
    if (result.isConfirmed) {
      swalWithBootstrapButtons.fire(
        '¡Eliminado!',
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
}


function submitFormEliminar(form) {
        Swal.fire({
            title: "Eliminar",
            text: "¿Desea eliminar el registro?",
            icon: "warning",
            showDenyButton: true,
            denyButtonText: "Cancelar",
            confirmButtonText: 'Aceptar',
            buttons: true,
            dangerMode: true,
        })
        .then(function (result) {
            if (result.isConfirmed) {
                form.submit();
                Swal.fire('¡Guardado!', 'Cambios realizados', 'success')
            }
            else if(result.isDenied){
             Swal.fire('Opps', 'Los cambios no fueron realizados', 'info')

            }
        });
          return false;
