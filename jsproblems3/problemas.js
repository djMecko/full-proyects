var array = [4,5,6,7,8];
var contador = 0;
var n=2;
var contadorextra=0;
document.write(n);
for(var i = 0 ; i < array.length; i++) {
	contador=array[i];
	console.log(contador)
	if (contador<n) {
		document.write("<br>Son menores a " +n+ "=" +contador);
	} else {
		document.writeln("<br>Son mayores a "+n+" = "+contador);
		contadorextra=contadorextra+1;

	}
}	
if (contadorextra !=0) {
	document.write("<br>"+"<br>"+"<br>"+"false");	
}else {
	document.write("<br>"+"<br>"+"<br>"+"true");
}