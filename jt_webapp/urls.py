from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.index, name='jamor_tech'),
    path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
    path('users/',
        views.users_list,
        name='user-list'),
    #path('users/', views.users_list),
    path('users/<int:pk>/',
        views.users_detail,
        name='user-detail'),
    path('users/<int:pk>/', views.users_detail),
    path('', views.api_root),
    #path('login', views.user_login, name='login'),
    #path('signup', views.user_signup, name='signup'),
    #path('logout', views.user_logout, name='logout'),
    
]



	
