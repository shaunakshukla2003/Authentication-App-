from django.urls import path
from .import views
urlpatterns = [
    path('',views.base,name='base'),
    path('signup/',views.signup_view,name='signup_view'),
    path('login/',views.login_view,name='login_view'),
    
]
