from django.shortcuts import render
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'
