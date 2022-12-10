from django.urls import path
from .views import teams, new, saveNew, delete, saveDelete, edit,saveEdit

urlpatterns = [
    path('',teams),
    path('novo/', new),
    path('salvarNovo/', saveNew),
    path('excluir/<int:code>', delete),
    path('salvarExclusao/', saveDelete),
    path('alterar/<int:code>', edit),
    path('salvarAlteracao/', saveEdit)
]