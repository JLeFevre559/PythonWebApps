from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import testboi


class testboiView(RedirectView):
    url = reverse_lazy('testy_list')


class testboiListView(ListView):
    template_name = 'testy/list.html'
    model = testboi
    context_object_name = 'testys'


class testboiDetailView(DetailView):
    template_name = 'testy/detail.html'
    model = testboi
    context_object_name = 'testy'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     testy = kwargs.get('testy')
    #     kwargs['dependents'] = testy.dependents
    #     return kwargs


class testboiCreateView(LoginRequiredMixin, CreateView):
    template_name = "testy/add.html"
    model = testboi
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.book = 1
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class testboiUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "testy/edit.html"
    model = testboi
    fields = '__all__'


class testboiDeleteView(LoginRequiredMixin, DeleteView):
    model = testboi
    template_name = 'testy/delete.html'
    success_url = reverse_lazy('testy_list')
