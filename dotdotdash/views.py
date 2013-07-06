from django.shortcuts import render_to_response, get_object_or_404
from dotdotdash.models import *

def home(request):
	home = Home.objects.all()[0]
	homeout = {"q1":home.quote1,"q2":home.quote2,"mp4":home.mp4,"ogv":home.ogv,"webm":home.webm}
	about = About.objects.all()[0]
	aboutout = {"about":about.about,"process":about.process,"bkImg":about.backgroundimage}
	services = Services.objects.all()[0]
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

	work = Work.objects.all()
	workout = []
	for project in work:
		workout.append({"title":project.title ,"subtitle":project.subTitle,"description":project.description})

	contact = Contact.objects.all()[0]
	contactout = {"text":contact.contant}

	return render_to_response('index.html',{
		"home":homeout,
		"about":aboutout,
		"services":servicesout,
		"clients":clientsout,
		"work":workout,
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




def projects(request,project=None,page=None):
	if(project == None or page == None):
		return render_to_response("basic.html",{"none":"data"})


	# work = Category.objects.filter(slug = "work")[0]

	# article = work.articleFields.filter(slug = project)
	# if(len(article) <= 0):
	# 	return render_to_response("basic.html",{"none":"data"})

	# pages = article[0].pages.filter(slug = page)
	# if(len(pages) <= 0):
	# 	return render_to_response("basic.html",{"none":"data"})
	# pages = pages[0]

	# pageObj = {"title":pages.title}
	# pageType = pages.pageType;

	# if(pageType == "imageWText"):
	# 	pageObj.update(getText(pages.textFields.all()))
	# 	if pages.videoURL:
	# 		pageObj.update({"vidLink":pages.videoURL})
	# 	pageObj.update(getImages(pages.mediaField.all()))
	# if(pageType == "fourImage" or pageType == "singleImage"):
	# 	pageObj.update(getImages(pages.mediaField.all()))


	return render_to_response("%s.html"%pageType,{"project":article,"content":pageObj})
