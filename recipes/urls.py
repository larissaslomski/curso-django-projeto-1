from django.urls import path
from recipes.views import home, contact, about


urlpatterns = [
    path('sobre/', about),
    path('', home),
    path('contato/', contact),
]
