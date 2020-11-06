document.addEventListener('DOMContentLoaded',()=>{
    const elementosCarousel = document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel,{
        duration: 400,
        padding: 5,
        dist: -80,
        shift: 5,
        numVisible: 3,
        indicators: true,
        noWrap: true

    });

});
function textosMayusc(){  
    var b = document.getElementById("idNombre");
    b.value = b.value.toUpperCase();

}

function textosMayuscv(){  
    var b = document.getElementById("idApellido_cliente");
    b.value = b.value.toUpperCase();

}

function textosMayuscc(){  
    var b = document.getElementById("idEmail_cliente");
    b.value = b.value.toUpperCase();

}