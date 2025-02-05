from django.urls import path
from gamers_timeline import views
urlpatterns = [
    path('', views.top,name="top"),
    path('<int:id>/',views.view,name="view"),
    path('index/', views.index,name="index"),
    path('create/', views.create,name="create"),
]