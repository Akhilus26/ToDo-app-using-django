from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name="create"),
    path('change_status/<int:id>/', views.edit, name="status_change")
]