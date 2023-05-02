# from django.core.paginator import Paginator
# from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from contest.forms import ContestForm
from .models import Contest


# def proposal(request, pk=None):
#     if pk is not None:
#         instance = get_object_or_404(Contest, pk=pk)
#     else:
#         instance = None
#     form = ContestForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=instance)
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#     return render(request, 'contest/contest_form.html', context)
#
#
# def proposal_list(request):
#     proposals = Contest.objects.all().order_by('id')
#     paginator = Paginator(proposals, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, 'contest/contest_list.html', context)
#
#
# def delete_proposal(request, pk):
#     instance = get_object_or_404(Contest, pk=pk)
#     form = ContestForm(instance=instance)
#     context = {'form': form}
#     if request.method == 'POST':
#         instance.delete()
#         return redirect('contest:list')
#     return render(request, 'contest/contest_form.html', context)


class ContestListView(ListView):
    model = Contest
    ordering = 'id'
    paginate_by = 3


class ContestFormMixin:
    model = Contest
    form_class = ContestForm


class ContestCreateView(ContestFormMixin, CreateView):
   pass


class ContestUpdateView(ContestFormMixin, UpdateView):
    pass


class ContestDeleteView(DeleteView):
    model = Contest
    success_url = reverse_lazy('contest:list')



class ContestDetailView(DetailView):
    model = Contest