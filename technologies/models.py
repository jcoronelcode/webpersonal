from django.db import models

# Create your models here.

class Technologies(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'nombre')
    image = models.ImageField(upload_to='img', verbose_name = 'imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha actualizacion')
    
    class Meta:
        verbose_name = 'tecnologia'
        verbose_name_plural = 'tecnologias'
        ordering = ['-created']
        
    def __str__(self):
        return self.name