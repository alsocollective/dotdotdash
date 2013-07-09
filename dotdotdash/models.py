from django.db import models
from django.template.defaultfilters import slugify
import os.path

class MediaNode(models.Model):
	title = models.CharField(max_length=600,blank=True)
	description = models.CharField(max_length=300, blank=True)
	link = models.URLField(max_length=1000, blank=True);
	vimeo = models.URLField(max_length=1000, blank=True);
	order = models.IntegerField(blank=True,default=0)

	def slugify_filename(instance, filename):
		fname, dot, extension = filename.rpartition('.')
		slug = slugify(fname)
		instance.title = '%s.%s' % (slug, extension)
		return 'static/uploaded/%s.%s' % (slug, extension)
	location = models.FileField(upload_to=slugify_filename)

	def save(self, *args, **kwargs):
		self.title = os.path.basename(self.location.name)
		super(MediaNode, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	def admin_image(self):
		if self.title:
			return '<img style="width:200px;height:auto;" src="/static/uploaded/%s"/>' % self.title
		return "not an image"
	admin_image.allow_tags = True

	def admin_video(self):
		if self.video:
			return '<iframe src="%s?title=0&amp;byline=0&amp;portrait=0&amp;color=ff0179" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>' % self.video
		return "not an video"
	admin_video.allow_tags = True

class Home(models.Model):
	class Meta:
		verbose_name_plural = "Home"
	quote1 = models.TextField(max_length=1000)
	quote2 = models.TextField(max_length=1000)

	mp4 = models.ForeignKey(MediaNode,blank=True,null=True,related_name="mp4+")
	ogv = models.ForeignKey(MediaNode,blank=True,null=True,related_name="ogv+")
	webm = models.ForeignKey(MediaNode,blank=True,null=True,related_name="webm+")
	workbackgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")

class About(models.Model):
	class Meta:
		verbose_name_plural = "About"
	about =	models.TextField(max_length=4000)
	process = models.TextField(max_length=4000)
	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")

class Services(models.Model):
	class Meta:
		verbose_name_plural = "Services"
	services = models.TextField(max_length=2000)

	socialmediastrategyplanning = models.TextField(max_length=2000)
	branding = models.TextField(max_length=2000)
	research = models.TextField(max_length=2000)

	creativedevelopment = models.TextField(max_length=2000)
	contentproduction = models.TextField(max_length=2000)
	resultsanalytics = models.TextField(max_length=2000)

	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")
	socimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="1img+")
	brandingimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="2img+")
	researchimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="3img+")
	creativedevimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="4img+")
	contentproductionimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="5img+")
	resultsimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="6img+")

class Clients(models.Model):
	class Meta:
		verbose_name_plural = "Clients"
	text = models.TextField(max_length=2000)
	clientimages = models.ManyToManyField(MediaNode,blank=True,related_name="imageFields+")
	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")

class Page(models.Model):
	pageTypes = (
		("text","text"),
		("singleImage","singleImage"),
		("fourImage","fourImage"),
		("imageWText","imageWText"),
		("pdf","pdf"),
	)
	title = models.CharField(max_length=600)
	textFields = models.TextField(max_length=1000)
	mediaField = models.ManyToManyField(MediaNode,blank=True,related_name="images+")
	videoURL = models.URLField(max_length=800, blank=True)
	pageType = models.CharField(max_length=30, choices=pageTypes)
	slug = models.SlugField(blank=True)
	order = models.IntegerField(blank=True,default=0)
	pdf = models.ManyToManyField(MediaNode,blank=True,related_name="pdf+")

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Page, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Work(models.Model):
	title = models.CharField(max_length=600)
	subTitle = models.CharField(max_length=600)
	pages = models.ManyToManyField(Page,blank=True,related_name="pages+")
	description = models.TextField(max_length=1000)
	datefororder = models.DateField(auto_now=True)
	slug = models.SlugField(blank=True)
	order = models.IntegerField(blank=True,default=0)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Work, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Contact(models.Model):
	class Meta:
		verbose_name_plural = "Contact"
	contant = models.TextField(max_length=4000)
	backgroundimage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkimg+")
