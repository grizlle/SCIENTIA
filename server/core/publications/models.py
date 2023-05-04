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
    details_of_documents = models.TextField(blank=True, verbose_name = 'Реквизиты документа о регистрации исключительных прав')
    udk = models.CharField(max_length=255, blank=True, verbose_name = 'УДК')
    publication_date = models.DateField(blank=True, null=True, verbose_name = 'Дата поступления публикации в издательство')
    description = models.TextField(blank=True, verbose_name = 'Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата поступления публикации в издательство')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Дата принятия публикации в печать')
    file_url = models.FileField(upload_to="publications/files/%Y/%m/%d", blank=True, null=True, verbose_name = 'Адрес полнотекстовой электронной версии публикации (URL)')
    authors = models.ManyToManyField(CustomUser, related_name="publication_list", verbose_name = 'Авторы публикации')
    #Правки
    WoS_CC =  models.BooleanField(default=False, verbose_name = 'Индексация базой данных Web of Science Core Collection')
    scopus = models.BooleanField(default=False, verbose_name = 'Индексация базой данных Scopus')
    RINC = models.BooleanField(default=False, verbose_name = 'Индексация базой данных РИНЦ')
    elib_ID = models.PositiveIntegerField(verbose_name = 'eLIBRARY ID')
    if_index_export = models.TextField(blank=True, verbose_name = 'Индексация иными зарубежными базами данных')
    date_publ = models.DateTimeField(auto_now=False, verbose_name = 'Месяц и год публикации')
    DOI = models.TextField(blank=True, verbose_name = 'Цифровой идентификатор объекта')
    ISSN = models.TextField(blank=True, verbose_name = 'ISSN')
    e-ISSN = models.TextField(blank=True, verbose_name = 'e-ISSN')
    ISBN = models.TextField(blank=True, verbose_name = 'ISBN')
    qwart_izd = models.DateField(blank=True, null=True, verbose_name = 'Квартиль издания JCR Science Edition')
    affil = models.TextField(blank=True, verbose_name = 'Аффиляция')
    finans = models.TextField(blank=True, verbose_name = 'Источник финансирования исследования')
    publ_type = models.TextField(blank=True, verbose_name = 'Вид публикации')
    
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
