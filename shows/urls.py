from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('new', views.add_shows),
    path('create', views.create),
    path('edit/<int:ids>', views.edit_shows),
    path('update/<int:ids>', views.update),
    path('<int:ids>', views.pointed_show),
    path('destroy/<int:ids>', views.destroy),
]
