
var useOpacity = (typeof document.createElement("div").style.opacity != 'undefined');


//sticky elements
$("#stickNav").waypoint('sticky');
$('.backgroundImage').waypoint('sticky',{
	wrapper: '<div class="background-wrapper" />',
});

//scrolling effect for nav
softScroll("aboutLink","about")
softScroll("serviceLink","services")
softScroll("clientsLink","clients")
softScroll("ourWorkLink","work")
softScroll("contactLink","contact")

//fading quotes
var fadingElement = [
	new FadeingObject("quote1"),
	new FadeingObject("quote2")
]

var scrollLocation = $(document).scrollTop();

function fadingResized(){
	for(var a = 0; a < fadingElement.length; ++a){
		fadingElement[a].resized();
		fadingElement[a].makeFade(scrollLocation,200);
	}
}
fadingResized();

$(window).scroll(function(eForEvent){
	scrollLocation = $(document).scrollTop();
	for(var a = 0; a < fadingElement.length; ++a){
		fadingElement[a].makeFade(scrollLocation,200);
	}
});

$(window).bind("resize",function(){
	fadingResized();
	windowHeight = $(window).height();
	document.getElementById('servicebackgrounds').style.height = windowHeight;
});
var serviceSection= $(".servicesection");
var serviceBackgrounds = $("#servicebackgrounds").children();
var windowHeight = $(window).height();
document.getElementById('servicebackgrounds').style.height = windowHeight;

for(var a =0; a < serviceBackgrounds.length; ++a){
	serviceBackgrounds[a] = $(serviceBackgrounds[a]).children()[0];
}

var buttons = $("#buttoncontainer").children();
var buttonsClicked = false;

buttons.each(function(index){
	$(buttons[index]).click(function(){
		event.preventDefault();
		hideServicesBut(this);
	});

})

function hideServicesBut(thisEl){
	var first = true;
	serviceSection.each(function(index){
		if(serviceSection[index].id == thisEl.id){
			if($(serviceSection[index]).hasClass("textnoshow")){
				if(first && buttonsClicked){
					$(serviceBackgrounds[index]).fadeIn(0);
					first = false;
				} else {
					$(serviceBackgrounds[index]).fadeIn(1000);
					if(!buttonsClicked){
						buttonsClicked = true;
					}
				}
			}

			$(serviceSection[index]).removeClass("textnoshow");
		} else if(!$(serviceSection[index]).hasClass("textnoshow")){
			$(serviceSection[index]).addClass("textnoshow");
			if(first){
				setTimeout(function(){
					$(serviceBackgrounds[index]).fadeOut(0)
				},1000)
				first = false;
			} else {
				$(serviceBackgrounds[index]).fadeOut(1000)
			}
		}
	});
}




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
			var transparency = (((quoteTop-scrollLocation)/(screenHeight/2))-1)*2;
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
