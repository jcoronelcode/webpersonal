from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'titulo')
    description = models.TextField(verbose_name = 'descripcion')
    image = models.ImageField(upload_to='img', verbose_name = 'imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha actualizacion')
    url = models.URLField(null=True, blank=True, verbose_name = 'URL')
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']
        
    def __str__(self):
        return self.title