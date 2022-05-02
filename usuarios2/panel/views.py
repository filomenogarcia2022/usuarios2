from django.shortcuts import redirect, render
from django.urls import reverse
from panel.models import usuarios2

# Create your views here.
#INSERT SQL
def home(request):
    if request.POST:
        usuario=usuarios2(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            mail=request.POST['mail']
        )
        usuario.save()
    return render(request, 'panel/home.html', locals())
#SELECT
def list(request):
    usuario=usuarios2.objects.all()
    return render(request, 'panel/list.html', locals())
#UPDATE
def edit(request, pk):
    usuario=usuarios2.objects.filter(pk=pk).first()
    if request.POST:
        usuario.nombre=request.POST['nombre']
        usuario.apellido=request.POST['apellido']
        usuario.email=request.POST['email']
        usuario.save()
    return render(request, 'panel/home.html', locals())
#DELETE
def delete(request, pk):
    usuario=usuarios2.objects.get(pk=pk)
    usuario.delete()
    return redirect(reverse('panel:list'))
    

    
