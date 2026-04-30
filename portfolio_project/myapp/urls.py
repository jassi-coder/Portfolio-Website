from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('', views.home, name='home'),
     path('contact/', views.contact_submit, name='contact_submit'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  # yeh add karo

]
