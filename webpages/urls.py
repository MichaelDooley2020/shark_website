# webpages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, AtlanticPageView, PacificPageView, IndianPageView, ArcticPageView, SouthernPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('atlantic/', AtlanticPageView.as_view(), name='atlantic'),
    path('pacific/', PacificPageView.as_view(), name='pacific'),
    path('indian/', IndianPageView.as_view(), name='indian'),
    path('arctic/', ArcticPageView.as_view(), name='arctic'),
    path('southern/', SouthernPageView.as_view(), name='southern')
]