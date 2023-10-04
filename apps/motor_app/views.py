""" Vistas Motors. """
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import MotorCategory, Motor
from .forms import MotorForm


# Create your views here.
def motor_add(request):
    """ Vista para motorizados. """
    if request.method == 'POST':
        form = MotorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # Obtiene los datos válidos del formulario
            # images = request.FILES.getlist('images')
            category_id = request.POST.get('category_id')
            print("Categoría seleccionada:", category_id)

            # Crea un objeto Motor utilizando los datos válidos
            new_motor = Motor.objects.create(
                title=data['title'],
                description=data['description'],
                location=data['location'],
                price=data['price'],
                brand=data['brand'],
                model=data['model'],
                fuel=data['fuel'],
                transmission=data['transmission'],
                year=int(data['year']),
                color=data['color'],
                # images=images,
                # MotorCategory=MotorCategory
            )

            return redirect(reverse('motor_add'))

    else:
        form = MotorForm()

    context = {
        'categories': MotorCategory.objects.all(),
        'form': form,
    }

    return render(request, 'motor_app/motor_form.html', context)
