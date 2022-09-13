function metrosParaCentimetros (){
    let metrosJS = document.getElementById("metros").value
    let calculo = (parseFloat(metrosJS) * 100)
    document.getElementById("Resultado").innerHTML = calculo + "cm"
}

var input = document.getElementById("metros");
input.addEventListener("keypress", function(event) {
    // const numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    setTimeout(metrosParaCentimetros, 100)   
});
