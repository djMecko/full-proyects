var array= [1,2,3,4,5]
var dublicado=0;

for (var i=0; i < array.length; i++) {
	dublicado=array[i]+array[i];
	document.write(i+".-"+array[i]+"="+dublicado+"<br>")
}