from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    last_name = models.CharField("Фамилия", max_length=150, blank=False, null=False)
    first_name = models.CharField("Имя", max_length=150, blank=False, null=False)
    patronymic = models.CharField("Отчество", max_length=150, blank=False, null=False)
    fio = models.CharField('ФИО', max_length=255, default='', blank=True)
    avatar_url = models.ImageField(upload_to="users/files/%Y/%m/%d", blank=True, null=True)
    #Правки
    wos_id = models.PositiveIntegerField()
    scorpus_auth_id = models.PositiveIntegerField()
    orcid = models.PositiveIntegerField()
    spin_kod = models.PositiveIntegerField()
    rinc_auth_id = models.PositiveIntegerField()
    
    
    
    
    
    def __str__(self):
        return self.username
