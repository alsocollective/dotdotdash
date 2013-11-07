var myPlayer = $("#youtube-player").Jtube({
		videoId:"RlCKrl1F-PI",
		skipvid:false,
		skipWhash:false,
		timeLeft:false,
		loop:1,
		applyToContainer:true,
		vidHeight:"100%",
		vidWidth:"100%",
		volume:0,
		debugMode:false,
		fallbackImage:"/../static/uploaded/bk-vid-img.png",

		onLoaded:function(){
			$('.backgroundImage').waypoint('sticky',{
				wrapper: '<div class="background-wrapper" />',
				video: $("#backgroundVideo")[0]
			});
		},
		onStart:function(settings){
			console.log("start");
			// $(settings.player.a).removeClass('hide');
			$(settings.player.a).fadeIn('fast');
		},
		onPause: function(settings){
			console.log("pause");
			// $(settings.player.a).addClass('hide')
			$(settings.player.a).fadeOut('fast')
		}
	});
function onYouTubeIframeAPIReady() {
	myPlayer.setupPlayer();
}

var scrolllocation = 0;
function noscroll(event){
	window.scroll(0,scrolllocation);
	event.preventDefault();
}

var useOpacity = (typeof document.createElement("div").style.opacity !== 'undefined');

bttonsHeight();
$("#stickNav").waypoint('sticky');


//scrolling effect for nav
softScroll("aboutLink","about");
softScroll("serviceLink","services");
softScroll("clientsLink","clients");
softScroll("ourWorkLink","work");
softScroll("contactLink","contact");
softScroll("contactLinktwo","contact");

//fading quotes
var fadingElement = [
	new FadeingObject("quote1"),
	new FadeingObject("quote2")
];

var scrollLocation = $(document).scrollTop();

function fadingResized(){
	for(var a = 0; a < fadingElement.length; ++a){
		fadingElement[a].resized();
		fadingElement[a].makeFade(scrollLocation,200);
	}
}
fadingResized();
$(window).scroll(function(){
	scrollLocation = $(document).scrollTop();
	for(var a = 0; a < fadingElement.length; ++a){
		fadingElement[a].makeFade(scrollLocation,200);
	}
});

var serviceSection= $(".servicesection");
var serviceBackgrounds = $("#servicebackgrounds").children();
var windowHeight = $(window).height();
document.getElementById('servicebackgrounds').style.height = windowHeight;

$(window).bind("resize",function(){
	bttonsHeight();
	fadingResized();
	document.getElementById('servicebackgrounds').style.height = windowHeight;

});

for(var a =0; a < serviceBackgrounds.length; ++a){
	serviceBackgrounds[a] = $(serviceBackgrounds[a]).children()[0];
}

var buttons = $("#buttoncontainer").children();
var buttonsClicked = false;

buttons.each(function(index){
	$(buttons[index]).click(function(event){
		event.preventDefault();
		hideServicesBut(this);
	});

});

function bttonsHeight(){
	var bkImages = $(".backgroundImage");
	windowHeight = $(window).height();
	bkImages.each(function(index){
		bkImages[index].style.height = windowHeight+"px";
	});
}

function hideServicesBut(thisEl){
	var first = true;
	serviceSection.each(function(index){
		if(serviceSection[index].id === thisEl.id){
			if($(serviceSection[index]).hasClass("textnoshow")){
				if(first && buttonsClicked){
					$(serviceBackgrounds[index]).fadeIn(0);
					first = false;
				} else {
					$(serviceBackgrounds[index]).fadeIn(500);
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
					$(serviceBackgrounds[index]).fadeOut(0);
				},1000);
				first = false;
			} else {
				$(serviceBackgrounds[index]).fadeOut(500);
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
	$('html, body').animate({scrollTop :  $("#"+location).offset().top-75},1000);
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
	};

	this.makeFade = function(scrollLocation,range){
		location = (quoteTop+(quoteSize/2))-scrollLocation;
		midPoint = screenHeight/2;
		if(location > midPoint - range && location < midPoint + range){
			var transparency = (((quoteTop-scrollLocation)/(screenHeight/2)))*2;
			if(transparency < 1.5){
				transparency = transparency-0.2;
			} else {
				transparency = 1;
			}
			if(useOpacity){
				quote.style.opacity = transparency;
			} else {
				quote.style.filter = "alpha(opacity="+ ((0.5+transparency)*100) + ")";
			}
		}
	};
}


$(".project").click(function(event){
	scrolllocation = $(window).scrollTop();
	event.preventDefault();
	//works defined in the django loop
	var workToShow = works[this.id];

	$(window).on("scroll",noscroll);

	var rsSlider = document.createElement("div");
	rsSlider.style.left = "100%";
	rsSlider.setAttribute("class","royalSlider");
	document.body.appendChild(rsSlider);

	var backButton = document.createElement("a");
	backButton.innerHTML = "Back";
	backButton.style.left = "105%";
	backButton.id = "rsbackButton";
	$(backButton).click(function(){
		rsSlider.style.left = "100%";
		backButton.style.left = "105%";
		$(window).off("scroll",noscroll);
		setTimeout(function(){
			rsSlider.parentNode.removeChild(rsSlider);
			backButton.parentNode.removeChild(backButton);
		},1000);
	});
	document.body.appendChild(backButton);

	rsSlider.innerHTML = "";
	var newElement = document.createElement("div");
	newElement.setAttribute("class","rsContent");

	var numberofslides = workToShow["Links"].length;
	for(var a = 0; a < numberofslides; ++a){
		var temp = newElement.cloneNode(true);
		temp.innerHTML += "  " + a;
		rsSlider.appendChild(temp);
	}

	var rsSliderChildren = rsSlider.childNodes;

	$(rsSliderChildren[0]).load(workToShow["Links"][0],function(){
		rsSlider.style.left = "0%";

		backButton.style.left = "0";

		for(var a = 1; a < rsSliderChildren.length; ++a){
			$(rsSliderChildren[a]).load(workToShow["Links"][a]);
		}

		$(".royalSlider").royalSlider({
			// options go here
			arrowsNav: true,
			controlNavigation: 'bullets',
			keyboardNavEnabled: true,
			loop:true,
			slidesSpacing: 0,
			// numImagesToPreload: 1,
			usePreloader: false,
			easeInOut: true,
			navigateByClick:false
		});
	});


});


function loadVideo(event, parentID, videoLink){
	event.preventDefault();
	// var parentElement = $("#"+parentID)[0].parentNode.parentNode.parentNode.parentNode;
	// parentElement.innerHTML = "";
	var parentElement = document.createElement("div");
	parentElement.id = "vimeo-container";
	$(parentElement).click(function(){
	        this.parentNode.removeChild(this);
	});
	document.body.appendChild(parentElement);

	var sins = document.createElement("div");
	sins.className = "sins";
	parentElement.appendChild(sins);

	var iframe = document.createElement("iframe");
	iframe.src = videoLink;
	iframe.setAttribute("webkitAllowFullScreen","");
	iframe.setAttribute("mozallowfullscreen","");
	iframe.setAttribute("allowFullScreen","");
	iframe.setAttribute("frameborder","0");
	iframe.setAttribute("width","500");
	iframe.setAttribute("height","281");
	sins.appendChild(iframe);
}
