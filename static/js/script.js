function softScroll(click, endup){
	$("#"+click).click(function(event){
		event.preventDefault();
		goToThisEndPoint(endup);
	});
}

function goToThisEndPoint(location){
	$('html, body').animate({scrollTop :  $("#"+location).offset().top},1000);
	setTimeout(function(){
		setHashTag(location);
	},1005);
}

function setHashTag(newTag){
	var element = document.getElementById(newTag);
	element.id = "";
	window.location.replace("#"+newTag);
	element.id = newTag;
}