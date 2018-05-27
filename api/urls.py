from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ListDeploy.as_view()),
    path('<int:pk>/', views.DetailDeploy.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]
