from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('lines/', views.LinesView.as_view(), name='lines'),
    path('lines/new/', views.CreateLineView.as_view(), name="create_line")
]
