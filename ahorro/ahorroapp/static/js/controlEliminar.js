(function(){
    const confirmaEliminar = document.querySelectorAll(".confirmaEliminar");

    confirmaEliminar.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('¿Está seguro de eliminar?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });
})();