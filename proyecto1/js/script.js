$(document).ready(function() {

	// ------------ mouse events

	$("#main-title1").click(function() {
		alert("titulo1")
	})
	
	$("#main-title2").dblclick(function() {
		alert("titulo2")
	})

	$("#main-title3").mouseenter(function() {
		console.log("titulo3 entro")
	});

	$("#main-title3").mouseleave(function() {
		console.log("titulo3 salio")
	});

	$("#main-title4").mouseover(function() {
		console.log("titulo4")
	});
	
	$("#main-title5").contextmenu(function() {
		console.log("titulo5")
	});

	$("#main-title6").mouseout(function() {
		console.log("titulo6")
	});
})

