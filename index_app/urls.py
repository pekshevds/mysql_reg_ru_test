from django.urls import path
from index_app.views import Index


urlpatterns = [
    path('', Index.as_view(), name='index'),
]
