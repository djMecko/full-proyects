function convertir(){
	var var1= parseInt(document.getElementById('var1').value);
	var var2 =1;
	for (var i=1 ; i <= var1; i++){
		var2 = var2*i;
				document.getElementById('resultado').value = var2;

		console.log(var2)
	}

}
