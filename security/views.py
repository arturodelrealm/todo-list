from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Cuenta creada con éxito. Ahora puedes iniciar sesión.'
            )
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = UserCreationForm()
    print(form.errors)
    return render(request, 'registration/register.html', {'form': form})
