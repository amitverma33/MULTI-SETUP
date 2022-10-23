from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change/', views.change_pass, name='change'),
    path('list/', views.ShowUser, name='users'),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
