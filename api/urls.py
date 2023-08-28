from django.urls import path
from api.views import getRoutes

urlpatterns = [
    path('', getRoutes, name='routes'),
]
