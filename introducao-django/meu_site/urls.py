from django.contrib import admin
from django.urls import path
from principal.views import inicio, editar_filme, excluir_filme

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('editar/<int:id>/', editar_filme, name='editar_filme'),
    path('excluir/<int:id>/', excluir_filme, name='excluir_filme'),
]
