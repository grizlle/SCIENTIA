from django.db import models

from users.models import CustomUser


class Publication(models.Model):
    title = models.CharField(max_length=255)
    sources = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    publication_year = models.CharField(max_length=4, blank=True)
    keywords = models.TextField(blank=True)
    output_data = models.TextField(blank=True)
    number = models.CharField(max_length=255, blank=True)
    tome = models.CharField(max_length=255, blank=True)
    issue_number = models.CharField(max_length=255, blank=True)
    pages = models.CharField(max_length=255, blank=True)
    details_of_documents = models.TextField(blank=True)
    udk = models.CharField(max_length=255, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    file_url = models.FileField(upload_to="publications/files/%Y/%m/%d", blank=True, null=True)
    authors = models.ManyToManyField(CustomUser, related_name="publication_list")
    #Правки
    WoS_CC =  models.BooleanField(default=False)
    scopus = models.BooleanField(default=False)
    RINC = models.BooleanField(default=False)
    elib_ID = models.PositiveIntegerField()
    if_index_export = models.TextField(blank=True)
    date_publ = models.DateTimeField(auto_now=False)
    DOI = models.TextField(blank=True)
    ISSN = models.TextField(blank=True)
    e-ISSN = models.TextField(blank=True)
    ISBN = models.TextField(blank=True)
    qwart_izd = models.DateField(blank=True, null=True)
    affil = models.TextField(blank=True)
    finans = models.TextField(blank=True)
    publ_type = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
