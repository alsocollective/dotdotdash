from django.contrib import admin
from dotdotdash.models import *

class pageAdmin(admin.ModelAdmin):
	list_display = ('title','order','pageType')
	filter_horizontal = ("mediaField",)
	list_filter = ('project', )

	fieldsets = [
		(None,{'fields':['title','project','mediaField',("pageType","order")]}),

		('Viemo',{
			'description':("Add the Viemo url(from the embeded method) here it should look something like this... http://player.vimeo.com/video/52542094?title=0&amp;byline=0&amp;portrait=0&amp;color=ff0179"),
			'fields':['videoURL'],
			}),

		("PDF",{
			'description':("Upload the pdf here, and a jpg of the PDF in the mediaField"),
			'fields':['pdf'],
			}),
		("Text",{
			'description':("This text will be displayed when the proper pageType"),
			'fields':['textFields'],
			}),

	]


class mediaAdmin(admin.ModelAdmin):
	list_display = ('title','admin_image')


	fieldsets = [
		(None,{'fields':['location','link']}),
		('Advance options', {
			'classes':('collapse',),
			'fields':('description','title','order'),
			}),
	]

class workAdmin(admin.ModelAdmin):
	list_display = ('title','order',"is_a_sos_project")
	filter_horizontal = ("pages",)
	fieldsets = [(None,{'fields':[("title","subTitle"),"description",("order","is_a_sos_project"),"pages"]})]

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Clients)
admin.site.register(MediaNode,mediaAdmin)
admin.site.register(Work,workAdmin)
admin.site.register(Page,pageAdmin)
admin.site.register(Contact)