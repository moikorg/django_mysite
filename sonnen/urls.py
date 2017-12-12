from django.urls import path
from . import views

app_name = 'sonnen'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sonnen_id>/', views.detail, name='detail'),
    path('status/', views.status, name='status')

#    url(''),
]
