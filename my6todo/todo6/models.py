from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(to=User, verbose_name='Vartotoja(-s)', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='Pavadinimas', max_length=200, null=True)
    descriptions = models.TextField(verbose_name='Aprašymas', null=True, blank=True)
    created = models.DateTimeField(verbose_name='Sukurta', auto_now_add=True)
    complete = models.BooleanField(verbose_name='Užduotis atlikta', default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'
