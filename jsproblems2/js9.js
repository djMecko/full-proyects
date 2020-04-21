var array = [1,2,3,4,5];
var contador= 0;

for (var i = 0; i < array.length; i++) {
	contador= array[i]*0;
	document.write(i+".-"+array[i]+"="+contador+"<br>");
}