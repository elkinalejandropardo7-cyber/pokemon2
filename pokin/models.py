from django.db import models

# Create your models here.
from django.db import models

tipo_naturaleza = [
    ('PL', 'Planta'),
    ('FU', 'Fuego'),
    ('AavG', 'Agua'),
    ('EL', 'Eléctrico'),
    ('NO', 'Normal'),
    ('PS', 'Psíquico'),
    ('LU', 'Lucha'),
    ('VE', 'Veneno'),
    ('TI', 'Tierra'),
    ('VO', 'Volador'),
    ('RO', 'Roca'),
    ('BU', 'Bicho'),
    ('FA', 'Fantasma'),
    ('DR', 'Dragón'),
]


class pokemon(models.Model):

    nombre = models.CharField(max_length=30, unique=True)
    peso = models.FloatField()
    imagen = models.URLField()
    habilidades = models.CharField(max_length=30)

    naturaleza = models.CharField(
        max_length=4,
        choices=tipo_naturaleza
    )

    descripcion = models.CharField(max_length=100)

    entrenador = models.ForeignKey(
        'entrenadores',
        on_delete=models.CASCADE,
        related_name='lista_pokemones'
    )

    def __str__(self):
        return self.nombre


class gimnasio(models.Model):

    lider_del_gym = models.CharField(max_length=30)

    elemnto_del_gym = models.CharField(
        max_length=4,
        choices=tipo_naturaleza
    )

    medallas = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.lider_del_gym}-{self.elemnto_del_gym}-{self.medallas}'


class entrenadores(models.Model):

    id_documento = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    pokemones = models.CharField(max_length=25)

    medallas = models.ManyToManyField(
        'gimnasio',
        blank=True,
        related_name='entrenadores'
    )

    def __str__(self):
        return f'{self.id_documento}-{self.nombre}-{self.apellido}-{self.pokemones}'