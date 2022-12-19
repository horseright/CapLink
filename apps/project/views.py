from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Project, Faq, Image

# Create your views here.


class IndexView(ListView):
    queryset = Project.objects.all()
    template_name = 'frontend/index.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'frontend/project/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        faqs = Faq.objects.filter(category__name='HashrateMarket')

        context['faqs'] = faqs
        return context


class ProjectsView(TemplateView):
    template_name = 'frontend/project/projects.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data()

        context['hashrate_projects'] = Project.objects.all()
        context['image_projects'] = Image.objects.all()

        return context
