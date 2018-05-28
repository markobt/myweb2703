from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListDeploy.as_view()),
    path('<int:pk>/', views.DeployDetail.as_view()),
]
