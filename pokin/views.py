
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import pokemon
from .forms import PokemonForm


def index(request):
    pokemones = pokemon.objects.all()

    contexto = {
        'pokemones': pokemones
    }

    return render(request, 'pokin/index.html', contexto)


def crear_pokemon(request):
    if request.method == 'POST':
        forms = PokemonForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'Pokémon registrado correctamente.')
            return redirect('listar')
        else:
            print(forms.errors)

    else:
        forms = PokemonForm()

    return render(request, 'pokin/poken.html', {'forms': forms})


def editar_pokemon(request, nombre):
    pokemon_editar = get_object_or_404(pokemon, nombre=nombre)

    form = PokemonForm(request.POST or None, instance=pokemon_editar)
    form.fields['nombre'].disabled = True

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Pokémon editado correctamente.')
        return redirect('listar')

    return render(request, 'pokin/poken.html', {
        'forms': form,
        'titulo': f'Editar {pokemon_editar.nombre}'
    })


def eliminar(request, nombre):
    pokemon_eliminar = get_object_or_404(pokemon, nombre=nombre)

    if request.method == 'POST':
        pokemon_eliminar.delete()
        messages.success(request, 'Pokémon eliminado correctamente.')
        return redirect('listar')

    return redirect('listar')
