from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_up,name='signup'),
    path('login/',views.user_login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.user_logout,name="logout"),
]
