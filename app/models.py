from django.db import models

class Client(models.Model):
    fullname = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'
    
class Sponsor(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='sponsors/%Y/%d')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Спонсора'
        verbose_name_plural = 'Спонсоры'

class Blog(models.Model):
    image = models.ImageField('blogs/%Y/%d')
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
    
    