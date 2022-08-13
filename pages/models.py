from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class BlogPost(models.Model):
	title = models.CharField(max_length=120, verbose_name='nomi', default='...')
	image = models.ImageField(upload_to="%d-%H-%m/", verbose_name='rasm', blank=True)
	about = models.TextField(verbose_name='malumot')
	time = models.DateTimeField(auto_now_add=True)

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
				return self.image.url
		else:
			return "active = models.BooleanField(default=False)static/image/no_image/no_img.png"

	def __str__(self):
		return self.title

class Comment ( models.Model ):
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField(blank=True, null=True)
	body = models.CharField(max_length=500)
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

class Certificat(models.Model):
	name = models.CharField(max_length=120, verbose_name='nomi', default='.')
	file = models.FileField(null=True, 
                           blank=True, upload_to='certificate/%d-%H',
                           validators=[FileExtensionValidator( ['pdf'] ) ])
	@property
	def file_url(self):
		if self.file and hasattr(self.file, 'url'):
				return self.file.url

	def __str__(self):
		return self.name
		
	
		

		
