from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from location_field.models.plain import PlainLocationField

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10,blank=True)
    profile_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

class Location(models.Model):
    city = models.CharField(max_length=255,null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7,null=True)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        Location.objects.filter(location=self).delete()

    def update_location(self):
        Location.objects.filter(location=self).update(location=self.location)

class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    ##ImageFields
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='tall')

    ##Related Fiels
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    pic = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.category.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)
    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id=self).delete()

    def update_image(self):
        updated_image = Image.objects.filter(pic=self.id).update(pic=self.pic,title=self.title,description=self.description,editor=self.editor,category=self.category,location=self.location)

@classmethod
def search_by_category(cls, category_term):


        # gallery = cls.objects.filter(category__search=search_term)
        # gallery = cls.objects.annotate(search=SearchVector('category','image_description').filter(search=search_term))

        galleria = cls.objects.filter(category__category=category_term)


        return galleria

@classmethod
def search_by_location(cls, location_term):
    galleria = cls.objects.filter(location__location=location_term)

    return galleria

    




