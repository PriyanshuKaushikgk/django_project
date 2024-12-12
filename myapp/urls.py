from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.handleBlog,name='handleBlog'),
    path('login',views.handlelogin,name='login'),
    path('search',views.search,name='search'),
    path('signup/',views.signuphandle,name='signuphandle'),
    path('logout',views.handlelogout,name="logout")
]
