from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from . import views
app_name = 'jump'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('thankyou/', views.request_services, name='thankyou'),
    path('sitemap.xml', views.site_map, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="jump_app/robots.txt", content_type="text/plain"),
         name="robots_file")

]