from django.urls import path
from .  import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('emergency',views.emergency,name='emergency'),
    path('data1',views.data1,name='data1'),
    path('serve',views.serve,name='serve'),
    path('register',views.register,name='register'),
]