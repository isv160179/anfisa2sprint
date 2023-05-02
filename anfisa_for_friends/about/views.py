# from django.shortcuts import render
from django.views.generic import TemplateView

from contest.models import Contest


# def description(request):
#     template = 'about/description.html'
#     return render(request, template)

class Description(TemplateView):
    template_name = 'about/description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_proposal'] = Contest.objects.count()
        return context

