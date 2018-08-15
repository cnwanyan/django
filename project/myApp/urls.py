from django.urls import path

from . import views

urlpatterns =[
  path("", views.index),
  path("<int:s>/", views.detail),
  path("grades", views.grades)
]