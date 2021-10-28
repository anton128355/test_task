from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('log-list/', views.logList, name="log-list"),
	path('log-create/', views.logCreate, name="log-create"),
	path('log-delete/<str:pk>/', views.logDelete, name="log-delete"),
]
