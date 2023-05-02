from django.urls import path

from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.ContestCreateView.as_view(), name='create'),
    path('list/', views.ContestListView.as_view(), name='list'),
    path('<int:pk>/', views.ContestDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.ContestUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ContestDeleteView.as_view(), name='delete'),

]
