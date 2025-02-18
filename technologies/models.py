from django.db import models

# Create your models here.

class Technologies(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'nombre')
    image_url = models.URLField(max_length=200, verbose_name = 'url de la imagen', default='https://www.google.com')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha actualizacion')
    
    class Meta:
        verbose_name = 'tecnologia'
        verbose_name_plural = 'tecnologias'
        ordering = ['-created']
        
    def __str__(self):
        return self.name