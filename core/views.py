from datetime import date
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView
from .models import Convidado



class ContatoView(TemplateView):
    template_name = 'core/contato.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'



class IndexView(SuccessMessageMixin, CreateView):
    template_name = 'core/index.html'
    model = Convidado
    fields = ['nome_convidado', 'quantidade_convidados', ]
    success_url = reverse_lazy('index')
    success_message = "Sua presença foi confirmada com sucesso! Muito obrigado!"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data_casamento'] = date(2017, 10, 6)
        return context


class ConvidadoList(LoginRequiredMixin, ListView):
    model = Convidado
    template_name = 'core/convidados_list.html'
    context_object_name = 'convidados_list'

    def get_context_data(self, **kwargs):
        context = super(ConvidadoList, self).get_context_data(**kwargs)
        context['quantidade_confirmada'] = Convidado.objects.aggregate(Sum('quantidade_convidados')).get('quantidade_convidados__sum', 0)
        return context


class ConvidadoDelete(LoginRequiredMixin, DeleteView):
    model = Convidado
    success_url = reverse_lazy('convidados')


contato = ContatoView.as_view()
about = AboutView.as_view()
index = IndexView.as_view()
convidado_list = ConvidadoList.as_view()
convidado_delete = ConvidadoDelete.as_view()