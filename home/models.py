from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    sumario = RichTextField()
    content = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Manchete(models.Model):
    titulo_destaque = models.CharField(max_length=36)
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.titulo_destaque