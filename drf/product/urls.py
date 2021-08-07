from django.urls import path
from .views import ProductApi


urlpatterns = [
    path('api', ProductApi.as_view()),

]
