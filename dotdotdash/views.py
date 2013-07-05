from django.shortcuts import render_to_response, get_object_or_404
from dotdotdash.models import *

def home(request):
	home = Home.objects.all()[0]
	homeout = {"q1":home.quote1,"q2":home.quote2,"mp4":home.mp4,"ogv":home.ogv,"webm":home.webm}
	about = About.objects.all()[0]
	aboutout = {"about":about.about,"process":about.process,"bkImg":about.backgroundimage}
	print "breakkkkkkk"
	services = Services.objects.all()[0]
	print services.services
	servicesout = {
		"services":{"text":services.services,"image":services.backgroundimage},
		"smsp":{"text":services.socialmediastrategyplanning,"image":services.socimage},
		"branding":{"text":services.branding,"image":services.brandingimage},
		"research":{"text":services.research,"image":services.researchimage},
		"creativedev":{"text":services.creativedevelopment,"image":services.creativedevimage},
		"contentproduction":{"text":services.contentproduction,"image":services.contentproductionimage},
		"resultsanalytics":{"text":services.resultsanalytics,"image":services.resultsimage},
		}
	clients = Clients.objects.all()[0]
	clientsout = {"text":clients.text,"images":getClients(clients.clientimages.all())}

	contact = Contact.objects.all()[0]
	contactout = {"text":contact.contant}

	return render_to_response('index.html',{
		"home":homeout,
		"about":aboutout,
		"services":servicesout,
		"clients":clientsout,
		"contact":contactout,
		})

def getClients(clist):
	out = []
	for client in clist:
		out.append(getImg(client))
	return out

def getImg(imageIn):
	return {"link":imageIn.link,"title":imageIn.title}

def getBkImg(imageIn):
	return {"bkImg":imageIn.title}



def sticky(request):
	return render_to_response('sticky.html',{"none":"none"})
