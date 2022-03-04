from django.shortcuts import render, redirect, get_object_or_404
from . models import Detalle
from ahorroapp.forms import RegistroForm


def home(request):
    return render(request, 'ahorroapp/home.html')


def detalle_ahorro(request):
    detalles = Detalle.objects.all().order_by('-fecha')
    return render(request, 'ahorroapp/detalle_ahorro.html', {'detalles': detalles})


def registro_ahorro(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ahorro:detalle')
    else:
        return render(
            request=request,
            template_name='ahorroapp/registro_ahorro.html',
            context={
                'form': form
                })


def delete(request, pk):
    pk = int(pk)
    try:
        detalle_sel = Detalle.objects.get(pk = pk)
    except Detalle.DoesNotExist:
        return redirect('ahorro:detalle')
    detalle_sel.delete()
    return redirect('ahorro:detalle')


def update(request, pk):
    pk = int(pk)
    try:
        detalle_sel = Detalle.objects.get(id = pk)
    except Detalle.DoesNotExist:
        return redirect('ahorro:detalle')
    detalle_form = RegistroForm(request.POST or None, instance = detalle_sel)
    if detalle_form.is_valid():
        detalle_form.save()
        return redirect('ahorro:detalle')
    return render(request, 'ahorroapp/update_ahorro.html', {'detalle_form': detalle_form})


def proyeccion(request, pk):
    pk = int(pk)
    proyecciones = Detalle.objects.get(id = pk)

    totales = float(
        proyecciones.cuenta_millonaria_dolares*proyecciones.tipo_de_cambio +
        proyecciones.cuenta_millonaria_soles +
        proyecciones.cuenta_AFP_soles +
        proyecciones.cuenta_ahorro_soles +
        proyecciones.cuenta_sueldo_soles
            )

    lista_rango = [ x for x in range(500,3001,500) ]

    ahorro_anios = [ int(totales//anio//12) for anio in lista_rango ]
    # print('ahorro_anios',ahorro_anios)

    ahorro_meses = [ int(totales//mes%12) for mes in lista_rango ]
    print('ahorro_meses',ahorro_meses)

    year_now = proyecciones.fecha.year
    month_now = proyecciones.fecha.month
    print('month_now',month_now)

    year_date_proyection = [x + year_now for x in ahorro_anios ]
    # print('year_date_proyection',year_date_proyection)

    month_date_proyection = []
    months = [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre' ]
    print(months[0])
    for x in ahorro_meses:
        new_month = x + month_now
        if new_month > 12:
            new_month = x
            month_date_proyection.append(months[new_month-1])
        else:
            month_date_proyection.append(months[new_month-1])
    # print('month_date_proyection',month_date_proyection)

    lista_compacta = zip(lista_rango, ahorro_anios,ahorro_meses,year_date_proyection,month_date_proyection)

    context = {
        'proyecciones': proyecciones,
        'totales': totales,
        'lista_compacta':lista_compacta,
        }

    return render(request, 'ahorroapp/proyeccion.html', context=context)
