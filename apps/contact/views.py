from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import ContactForm

# Create your views here.


class ContactView(FormView):
    template_name = 'frontend/contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)


class AboutView(TemplateView):
    template_name = 'frontend/contact/about.html'
