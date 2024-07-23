from django.urls import path
from portifolio_app.views import index

app_name = 'portifolio_app'

urlpatterns = [
    path('', index, name="index")
]