
function calcular_formulas() {
    console.log()
    const a = parseInt(document.getElementById("a").value)
    const b = parseInt(document.getElementById("b").value)
    const c = parseFloat(document.getElementById("c").value)
    const linha1 = `O produto do dobro do primeiro com metade do segundo é, ${a*2*b/2}\n`
    const linha2 = `A soma do triplo do primeiro com o terceiro é, ${a*3+c}\n`
    const linha3 = `O terceiro elevado ao cubo é, ${Math.pow(c,3).toFixed(2)}`
    document.getElementById("resultado").innerHTML = linha1 + linha2 + linha3
}
