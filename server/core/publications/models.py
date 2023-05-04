from django.db import models

from users.models import CustomUser


class Publication(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Название')
    sources = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    publication_year = models.CharField(max_length=4, blank=True, verbose_name = 'Год публикации')
    keywords = models.TextField(blank=True, verbose_name = 'Ключевые слова')
    output_data = models.TextField(blank=True)
    number = models.CharField(max_length=255, blank=True, verbose_name = 'Номер публикации')
    tome = models.CharField(max_length=255, blank=True, verbose_name = 'Том')
    issue_number = models.CharField(max_length=255, blank=True, verbose_name = 'Номер выпуска')
    pages = models.CharField(max_length=255, blank=True, verbose_name = 'Количество страниц')
    details_of_documents = models.TextField(blank=True)
    udk = models.CharField(max_length=255, blank=True, verbose_name = 'УДК')
    publication_date = models.DateField(blank=True, null=True, verbose_name = 'Дата поступления публикации в издательство')
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    file_url = models.FileField(upload_to="publications/files/%Y/%m/%d", blank=True, null=True)
    authors = models.ManyToManyField(CustomUser, related_name="publication_list")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
