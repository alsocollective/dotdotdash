from django.contrib import admin
from dotdotdash.models import *

class pageAdmin(admin.ModelAdmin):
	list_display = ('title','order','pageType')
	filter_horizontal = ("mediaField",)

	# fieldsets= [
	# 	(None,{'fields':'title','mediaField'})
	# ]


class mediaAdmin(admin.ModelAdmin):
	list_display = ('title','description','admin_image')

	fieldsets = [
		(None,{'fields':['location','link']}),
		('Advance options', {
			'classes':('collapse',),
			'fields':('description','title','order')
			}),
	]

class workAdmin(admin.ModelAdmin):
	list_display = ('title','order',"is_a_sos_project")
	filter_horizontal = ("pages",)
	fieldsets = [(None,{'fields':["title","subTitle","description","pages","order","is_a_sos_project"]})]

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Clients)
admin.site.register(MediaNode,mediaAdmin)
admin.site.register(Work,workAdmin)
admin.site.register(Page,pageAdmin)
admin.site.register(Contact)