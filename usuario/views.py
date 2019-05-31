from django.shortcuts import render, redirect
from .forms import UsuarioForm


def registrar(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('/dashboard/')
            except:
                pass
    else:
        form = UsuarioForm()
    return render(request, 'usuario/registrarUsuario.html', {'form': form})
