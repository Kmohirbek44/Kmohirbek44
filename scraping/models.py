import jsonfield
from django.db import models


from .utils import from_cryillic_to_eng
def default_urls():
    return {'hh': "", 'ishkop': "", 'uzjobble': "" }
class City(models.Model):
    name=models.CharField(max_length=50,verbose_name='shahar')
    slug=models.CharField(max_length=50,blank=True)
    class Meta:
        verbose_name_plural='shaharlar'
        verbose_name='shahar'

    def __str__(self):
        return self.name
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug=from_cryillic_to_eng(self.name)
        super().save(*args,**kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='dasturlash tili')
    slug = models.CharField(max_length=50,blank=True)

    class Meta:
        verbose_name_plural = 'dasturlash tillari'
        verbose_name = 'dasturlash tili'

    def __str__(self):
        return self.name

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug=from_cryillic_to_eng(self.name)
        super().save(*args,**kwargs)
class Vakation(models.Model):
    url=models.URLField(verbose_name='url')
    title=models.CharField(max_length=20,blank=True)
    company=models.CharField(max_length=20,blank=True)
    description=models .TextField(blank=True)
    city=models.ForeignKey('City',on_delete=models.CASCADE,blank=True)
    language=models.ForeignKey('Language',on_delete=models.CASCADE,blank=True)
    Rezume = models.BooleanField(default=False)
    timestap=models.DateField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-timestap']
class Errors(models.Model):
    timestap=models.DateField(auto_now_add=True)
    data=jsonfield.JSONField()
    def __str__(self):
        return str(self.timestap)
    class Meta:
        verbose_name_plural='Errors'
class Urls(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, blank=True)
    data=jsonfield.JSONField(default=default_urls)
    class Meta:
        unique_together=('city','language')
        verbose_name_plural='Urls'

class Resume(models.Model):
    name = models.CharField(max_length=128)
    profession=models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128,default='+998')
    email=models.EmailField(unique=False)

    experience=models.TextField()
    education = models.TextField()
    skills=models.TextField()
    about_meu=models.TextField()
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, blank=True)
    telegram_link=models.CharField(max_length=128,blank=True)
    linked = models.CharField(max_length=128, blank=True)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)