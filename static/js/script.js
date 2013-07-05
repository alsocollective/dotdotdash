
var useOpacity = (typeof document.createElement("div").style.opacity != 'undefined');

// Element, Element -> EventListener
//element one is the object that is click to scroll to element two
function softScroll(click, endup){
	$("#"+click).click(function(event){
		event.preventDefault();
		goToThisEndPoint(endup);
	});
}

//Element -> Animation
//scrolls html/body to the given element in 1 second
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

function FadeingObject(element){
	var quote = document.getElementById(element);
	var quoteTop = 0;
	var quoteSize = 0;
	var screenHeight = 0;
	var location = 0;
	var midPoint = 0;

	this.resized = function(){
		quoteTop = $(quote).offset().top;
		quoteSize = $(quote).height();
		screenHeight = $(window).height();
	}

	this.makeFade = function(scrollLocation,range){
		location = (quoteTop+(quoteSize/2))-scrollLocation;
		midPoint = screenHeight/2;
		if(location > midPoint - range && location < midPoint + range){
			var transparency = ((quoteTop-scrollLocation)/(screenHeight/2))-1;
			if(transparency < 0){
				transparency = transparency*(-1);
			}
			transparency = 1 - transparency;
			if(useOpacity){
				quote.style.opacity = transparency;
			} else {
				quote.style.filter = "alpha(opacity="+ ((0.5+transparency)*100) + ")";
			}
		}
	}
}

