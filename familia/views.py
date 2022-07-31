from django.shortcuts import get_object_or_404, render
from .models import Familia


def create_familiar(request):
    if Familia.objects.all().count() == 0:
        new_familiar1 = Familia.objects.create(
            name='Oscar', lastname='Fratesi', fecha_nacimiento='1952-04-28', relation='Padre')
        new_familiar2 = Familia.objects.create(
            name='Claudia', lastname='López', fecha_nacimiento='1956-06-04', relation='Madre')
        new_familiar3 = Familia.objects.create(
            name='Carla', lastname='Fratesi', fecha_nacimiento='1979-11-22', relation='Hermano/a')
        context = {
            'mensaje': "Familiares creados"
        }
        return render(request, 'familia/create_familia.html', context=context)
    context = {
        'mensaje': "BD ya tiene familiares"
    }
    return render(request, 'familia/create_familia.html', context=context)


def list_familia(request):
    familia = Familia.objects.all()
    context = {
        'familia': familia,
    }
    return render(request, 'familia/familia_list.html', context=context)


def familiar(request, pk):
    familiar = get_object_or_404(Familia, pk=pk)
    context = {
        'familiar': familiar,
    }
    return render(request, 'familia/familia_detail.html', context=context)
