from django.urls import path
from .views import *


urlpatterns = [
    path('', list_autores, name="list-autores"),
    path('livro-form', create_livro_form, name="livro-form"),
    path('livro/<int:id>', detail_livro, name="detail-livro"),
    path('autor/<int:id>/livros', create_livro, name="create-livro"),
    path('livro/<int:id>/update', update_livro, name="update-livro"),
    path('livro/<int:id>/delete', delete_livro, name="delete-livro"),
]
