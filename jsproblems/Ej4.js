function convertir(){
	var var1= parseInt(document.getElementById('var1').value);
	var var2 =0
	for (var i=0 ; i <= var1; i++){
		var2 = var2+i;
		console.log(var2)
	}
		document.getElementById('resultado').value = var2;

}
