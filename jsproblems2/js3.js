var arrayuno = [9,2,3,4,5];
var arraydos = [5,4,3,2,3];

var dos= arraydos.length;
var uno= arrayuno.length;

var suma=0;

if (uno==dos) {
	for (var i = 0 ; i < uno; i++) {
		suma=arrayuno[i]+arraydos[i];
	document.write(i+"-."+arrayuno[i]+"+"+arraydos[i]+"="+suma+"<br>")
	}
} else {
	document.write("Sus arreglos son diferentes")
}