from django.db import models

# Create your models here.

class Education(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'titulo')
    school = models.CharField(max_length=100, verbose_name = 'centro educativo', default='Default school')
    description = models.TextField(verbose_name = 'descripcion')
    image = models.ImageField(upload_to='img', verbose_name = 'imagen')
    start_date = models.DateField(verbose_name = 'Fecha de inicio')
    end_date = models.DateField(verbose_name = 'Fecha de finalizacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha actualizacion')
    
    class Meta:
        verbose_name = 'educacion'
        verbose_name_plural = 'educaciones'
        ordering = ['-created']
        
    def __str__(self):
        return self.title
