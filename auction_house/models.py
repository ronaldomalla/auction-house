from django.db import models
from django.db.models import Q

class productqueryset(models.QuerySet):
    def search(self,query=None):
        qs=self
        if query is not None:
            or_lookup=(Q(title_icontains=query)| Q(description_icontains=query)| Q(slug_icontains=query))
            qs= qs.filter(or_lookup).distinct()
            return qs


class productmanager(models.Manager):

    def get_queryset(self):
        return productqueryset(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)


class contact(models.Model):

    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    number=models.IntegerField(null=True)
    message=models.TextField(max_length=200)
    def __str__(self):

        return self.full_name
class drawing_product(models.Model):
    # lot=models.DecimalField(decimal_places=2,max_digits=8)
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=150,unique=True)
    pub_date=models.DateTimeField()
    price=models.DecimalField(decimal_places=2,max_digits=20)
    image=models.ImageField(upload_to='images/',max_length=100)
    discription=models.TextField()
    artist_name = models.CharField(max_length=100)
    produced_date = models.DateField()
    auction_date = models.DateField()
    objects=productmanager()
    # general_classification = models.CharField(max_length=10)
    # drawing_median= models.CharField(max_length=10)
    # dimension = models.DecimalField(decimal_places=2,max_digits=20)
    # frame = models.CharField(max_length=100)


    def summary(self):
        return self.discription[:20]
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:

        ordering = ['-pub_date']
class painting_product(models.Model):
    # lot=models.DecimalField(decimal_places=2,max_digits=8)
    title=models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)
    pub_date=models.DateTimeField()
    price=models.DecimalField(decimal_places=2,max_digits=20)
    image=models.ImageField(upload_to='images/',max_length=100)
    discription=models.TextField()
    artist_name = models.CharField(max_length=100)
    produced_date = models.DateField()
    auction_date = models.DateField()
    objects = productmanager()
    # general_classification = models.CharField(max_length=10)
    # median_used= models.TextField(max_length=10)
    # dimension = models.DecimalField(decimal_places=2,max_digits=20)
    # frame = models.CharField(max_length=100)

    def summary(self):
        return self.discription[:20]
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:

        ordering = ['-pub_date']
class carving_product(models.Model):
    #lot=models.DecimalField(decimal_places=2,max_digits=8)
    title=models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)
    pub_date=models.DateTimeField()
    price=models.DecimalField(decimal_places=2,max_digits=20)
    image=models.ImageField(upload_to='images/',max_length=100)
    discription=models.TextField()
    artist_name = models.CharField(max_length=100)
    produced_date = models.DateField()
    auction_date = models.DateField()
    objects = productmanager()
    # dimension = models.DecimalField(decimal_places=2,max_digits=20)
    # Image_type=models.CharField(max_length=10)

    def summary(self):
        return self.discription[:20]
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-pub_date']



class sculpture_product(models.Model):
   #lot=models.DecimalField(decimal_places=2,max_digits=8)
    title=models.CharField(max_length=255)
    slug= models.SlugField(max_length=150, unique=True)
    pub_date=models.DateTimeField()
    price=models.DecimalField(decimal_places=2,max_digits=20)
    image=models.ImageField(upload_to='images/',max_length=100)
    discription=models.TextField()
    artist_name = models.CharField(max_length=100)
    produced_date = models.DateField()
    auction_date = models.DateField()


    objects = productmanager()
    # dimension = models.DecimalField(decimal_places=2,max_digits=20)
    # material_used=models.CharField(max_length=100)
    # weight=models.DecimalField(decimal_places=2,max_digits=5)

    def summary(self):
        return self.discription[:20]
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:

        ordering = ['-pub_date']
class photographic_product(models.Model):
    # lot=models.DecimalField(decimal_places=2,max_digits=8)
    title=models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)
    pub_date=models.DateTimeField()
    price=models.DecimalField(decimal_places=2,max_digits=20)
    image=models.ImageField(upload_to='images/',max_length=100)
    discription=models.TextField()
    artist_name = models.CharField(max_length=100)
    produced_date = models.DateField()
    auction_date = models.DateField()
    objects = productmanager()
    # dimension = models.DecimalField(decimal_places=2,max_digits=20)
    # material_used=models.CharField(max_length=100)
    # weight=models.DecimalField(decimal_places=2,max_digits=5)


    def summary(self):
        return self.discription[:20]
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:

        ordering = ['-pub_date']
class Userprofile(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
class bid(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    contact_number=models.IntegerField(max_length=15)
    idproof=models.FileField(upload_to='uploads/')
    amount=models.DecimalField(max_digits=19, decimal_places=10)