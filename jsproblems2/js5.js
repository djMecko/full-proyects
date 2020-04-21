var array1= [5,4,3,2,1];
var array2= [5,4,3,2,1];
var multiplicacion = 0;

if (array1.length==array2.length) {

	for (var i = 0; i < array1.length; i++) {
		multiplicacion=array1[i]*array2[i];
		document.write(i+".-"+array1[i]+"*"+array2[i]+"="+multiplicacion+"<br>")
	}
}else {
	document.write("Soy la mera verga :v")
}