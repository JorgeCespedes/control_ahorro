from ahorroapp import views

from django.urls import path

urlpatterns = [
    path(
        route='',
        view=views.home,
        name='home'
        ),
    path(
        route='detalle_ahorro/',
        view=views.detalle_ahorro,
        name='detalle'
        ),
    path(
        route='registro_ahorro/',
        view=views.registro_ahorro,
        name='registro'
        ),
    path(
        route='delete/<int:pk>',
        view=views.delete,
        name='delete'
        ),
    path(
        route='update/<int:pk>',
        view=views.update,
        name='update'
        ),
    path(
        route='proyeccion/<int:pk>',
        view=views.proyeccion,
        name='proyeccion'
        ),
]