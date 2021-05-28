from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('startup/', views.StartUpList, name='startup'),
    path('startup/<int:pk>', views.DetailStartup, name='detailStartUp'),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]