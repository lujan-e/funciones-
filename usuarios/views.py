from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroFormulario, LoginFormulario, EditarInformacionFormulario
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('menu')
    else:
        form = RegistroFormulario()
    return render(request, 'usuarios/registro.html', {'form': form})

def acceso(request):
    if request.method == 'POST':
        form = LoginFormulario(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                messages.error(request, "Credenciales incorrectas")
    else:
        form = LoginFormulario()
    return render(request, 'usuarios/acceso.html', {'form': form})

@login_required
def menu(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'usuarios/menu.html', {'tareas': tareas})


@login_required
def informacion_del_miembro(request):
    if request.method == 'POST':
        form = EditarInformacionFormulario(request.POST)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')

            # Cambiar la contraseña si se proporcionan las dos contraseñas
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 and password2 and password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, "Información actualizada correctamente")
                return redirect('menu')

            user.save()
            messages.success(request, "Información actualizada correctamente")
            return redirect('menu')
    else:
        form = EditarInformacionFormulario(initial={'username': request.user.username, 'email': request.user.email})

    return render(request, 'usuarios/informacion_del_miembro.html', {'form': form})

@login_required
def eliminar_usuario(request):
    user = request.user
    user.delete()
    return redirect('registro')  # Redirigimos al registro después de eliminar el usuario

# Create your views here.
