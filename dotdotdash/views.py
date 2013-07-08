from django.shortcuts import render_to_response, get_object_or_404
from dotdotdash.models import *

def home(request):
	if(request.mobile):
		return render_to_response("mobile/index.html",getHome())
	homeout = getHome()
	aboutout = getAbout()
	servicesout = getServices()
	clientsout = getClients()
	workout = getWork()

	contact = Contact.objects.all()[0]
	contactout = {"text":contact.contant, "bkImg":contact.backgroundimage}

	return render_to_response('index.html',{
		"home":homeout,
		"about":aboutout,
		"services":servicesout,
		"clients":clientsout,
		"work":workout,
		"contact":contactout,
		})

def getHome():
	home = Home.objects.all()[0]
	homeout = {"q1":home.quote1,"q2":home.quote2,"mp4":home.mp4,"ogv":home.ogv,"webm":home.webm}
	return homeout

def getAbout():
	about = About.objects.all()[0]
	aboutout = {"about":about.about,"process":about.process,"bkImg":about.backgroundimage}
	return aboutout

def getServices():
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
	return servicesout

def getClients():
	clients = Clients.objects.all()[0]
	clientsout = {"text":clients.text,"images":getClientImages(clients.clientimages.all())}
	return clientsout

def getWork():
	work = Work.objects.all()
	workout = []
	for project in work:
		print project.pages.all()
		workout.append({
			"title":project.title,
			"slug":project.slug,
			"subtitle":project.subTitle,
			"description":project.description,
			"pages":getPages(project.pages.all())
			})
	return workout

def getPages(wlist):
	pages = []
	for page in wlist:
		pages.append({"slug":page.slug})
	return pages

def getContentOfPages(projectName):
	if(projectName == None):
		return {"no":"projects"}
	work = Work.objects.filter(slug = projectName)[0]
	pagesOut = []
	for page in work.pages.all():
		pagesOut.append({
			"title":page.title,
			"text":page.textFields,
			"images":getClientImages(page.mediaField.all()),
			"video":page.videoURL,
			"slug":page.slug,
			})
	return {"pages":pagesOut,"title":work.title}

def getClientImages(clist):
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

def getImages(listIn):
	mediaList = []
	for media in listIn:
		mediaObj = {
			"location":media.title,
			"description":media.description,
			"link":media.link,
			"vimeo":media.vimeo}
		mediaList.append(mediaObj)
	return ({"media":mediaList})


def projects(request,project=None,page=None):
	if(project == None or page == None):
		return render_to_response("basic.html",{"none":"data"})

	article = []
	pageObj = []
	pageType = "text"
	project = Work.objects.filter(slug = project)[0]
	page = project.pages.filter(slug = page)[0]
	pageout = {
		"title":page.title,
		"text":page.textFields,
		"video":page.videoURL,
		"slug":page.slug
		}
	pageout.update(getImages(page.mediaField.all()))

	return render_to_response("%s.html"%pageType,{"project":article,"content":pageout})


def about(request):
	return render_to_response('mobile/about.html',getAbout())

def clients(request):
	return render_to_response('mobile/clients.html',getClients())

def services(request):
	print getServices()
	return render_to_response('mobile/services.html',getServices())

def work(request):
	return render_to_response('mobile/work.html', {"work":getWork()})

def works(request,project=None):
	return render_to_response('mobile/works.html',	getContentOfPages(project))
