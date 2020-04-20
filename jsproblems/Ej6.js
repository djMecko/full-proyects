function convertir(){
	var var1= parseInt(document.getElementById('var1').value);
	if (var1 % 2 == 0) {
		console.log("es par");
		document.getElementById('resultado').value = "es par";

	}else {
		document.getElementById('resultado').value = "es impar";
		console.log("es impar");
	}
}
