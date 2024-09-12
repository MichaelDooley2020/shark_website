# webpages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class AtlanticPageView(TemplateView):
    template_name = 'atlantic.html'

class PacificPageView(TemplateView):
    template_name = 'pacific.html'

class IndianPageView(TemplateView):
    template_name = 'indian.html'

class ArcticPageView(TemplateView):
    template_name = 'arctic.html'

class SouthernPageView(TemplateView):
    template_name = 'southern.html'