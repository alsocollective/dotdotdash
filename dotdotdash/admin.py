from django.contrib import admin
from dotdotdash.models import *

class mediaAdmin(admin.ModelAdmin):
	list_display = ('title','description','admin_image')

	fieldsets = [
		(None,{'fields':['location','link','order','vimeo']}),
		('Advance options', {
			'classes':('collapse',),
			'fields':('description','title')
			}),
	]

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Clients)
admin.site.register(MediaNode,mediaAdmin)
admin.site.register(Work)
admin.site.register(Page)
admin.site.register(Contact)