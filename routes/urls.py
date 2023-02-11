from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('lines/', views.LinesView.as_view(), name='lines'),
    path('lines/new/', views.CreateLineView.as_view(), name="create_line"),
    path('lines/<pk>/update/', views.UpdateLineView.as_view(), name="update_line"),
    path('lines/<pk>/delete/', views.DeleteLineView.as_view(), name="delete_line"),
    path('stations/', views.StationsView.as_view(), name="stations"),  # Stations
    path('statios/new/', views.CreateStationView.as_view(), name="create_station"),
    path('stations/<pk>/update/', views.UpdateStationView.as_view(), name="update_station"),
    path('stations/<pk>/delete/', views.DeleteStationView.as_view(), name="delete_station")
]
