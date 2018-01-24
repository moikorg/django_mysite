from django.urls import path
from . import views

app_name = 'sonnen'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('status/', views.status, name='status'),

]
