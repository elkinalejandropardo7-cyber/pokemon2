from django import forms
from .models import pokemon


class PokemonForm(forms.ModelForm):
    class Meta:
        model = pokemon
        fields = [
            'nombre',
            'peso',
            'imagen',
            'habilidades',
            'naturaleza',
            'descripcion',
            'entrenador'
        ]


# class EntrenadorForm(forms.ModelForm):

#     class Meta:
#         model = entrenadores
#         fields = [
#             'id_documento',
#             'nombre',
#             'apellido',
#             'pokemones',
#             'medallas'
#         ]

#         widgets = {
#             'medallas': forms.CheckboxSelectMultiple()
#         }


# class GimnasioForm(forms.ModelForm):

#     class Meta:
#         model = gimnasio
#         fields = [
#             'lider_del_gym',
#             'elemnto_del_gym',
#             'medallas'
#         ]
