
function Guardar2()
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
    denyButtonText: 'Cancelar',
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
      Swal.fire(window.location = "usuario/inicialusuario")
    } else if (result.isDenied) {
      Swal.fire(window.location = "admin/paginaprincipal")
    }
  })
}

function Guardar(){

Swal.fire(

    {
        title              : "¿Estás seguro?",
        text               : "¿Quieres guardar?",
        type               : "warning",
        allowEscapeKey     : false,
        allowOutsideClick  : false,
        showCancelButton   : true,
        confirmButtonColor : "#DD6B55",
        confirmButtonText  : "Sí",
        showLoaderOnConfirm: true,
        closeOnConfirm     : false
    },

    function (isConfirm) {
        preventDefault();
        if (isConfirm) {
            profileinfo.submit();
            return true;
        }

        return false;

    }

);
}

$(".swa-confirm").on("click", function(e) {
    e.preventDefault();
    Swal.fire({
        title: $(this).data("swa-title"),
        text: $(this).data("swa-text"),
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#cc3f44",
        confirmButtonText: $(this).data("swa-btn-txt"),
        closeOnConfirm: true,
        html: false
    }, function( confirmed ) {
        if( confirmed )
            $(this).closest('form').submit();
    });
});

function submitForm(form) {
        Swal.fire({
            title: "Guardar",
            text: "¿Deseas guardar los cambios?",
            icon: "question",
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

    }