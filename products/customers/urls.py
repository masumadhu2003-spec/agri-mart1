from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('About/',views.About,name='About'),
    path('Register/', views.register, name='Register'),
    path('Login/', views.login_view, name='Login'),
    path('products/',views.products,name='products'),
    path('fertilizers/',views.fertilizers,name='fertilizers'),
    path('liquets/',views.liquids,name='liquids'),
    path('powders/',views.powders,name='powders'),
    path('my profilie/',views.myprofile,name='myprofile'),
]
