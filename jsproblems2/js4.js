var array1= [9,8,7,6,5]
var array2= [7,4,3,3,2]

var uno= array1.length;
var dos= array2.length;

var resta= 0;

if (uno==dos) {
	for (var i=0; i < uno; i++) {
		resta=array1[i]-array2[i];
		document.write(i+"-."+array1[i]+"-"+array2[i]+"="+resta+"<br>")
	}
} else {
	document.write("no son iguales");
}