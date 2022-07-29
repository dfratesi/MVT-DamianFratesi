from django.db import models
from django.urls import reverse


class Familia(models.Model):
    RELATION = (
        ('Padre', 'Padre'),
        ('Hermano/a', 'Hermano/a'),
        ('Madre', 'Madre'),
    )

    name = models.CharField("Nombre", max_length=20)
    lastname = models.CharField("Apellido", max_length=20)
    fecha_nacimiento = models.DateField(
        "Fecha de nacimiento", blank=True, null=True)
    relation = models.CharField(
        "Relación", max_length=10, choices=RELATION, null=True)

    def age(self):
        from datetime import date
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - \
            ((today.month, today.day) <
             (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age

    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return self.full_name()

    class Meta:
        ordering = ['lastname', 'name']
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"
