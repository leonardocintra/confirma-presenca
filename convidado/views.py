from datetime import date
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView
from .models import Convidado, ListaConvidados


class PresencaConfirmadaView(TemplateView):
    template_name = 'convidado/presenca_confirmada.html'

    def get_context_data(self, **kwargs):
        context = super(PresencaConfirmadaView, self).get_context_data(**kwargs)
        context['data_casamento'] = date(2017, 10, 6)
        return context


class ConvidadoListView(LoginRequiredMixin, ListView):
    model = Convidado
    template_name = 'convidado/convidados_list.html'
    context_object_name = 'convidados_list'

    def get_context_data(self, **kwargs):
        context = super(ConvidadoListView, self).get_context_data(**kwargs)
        context['quantidade_confirmada'] = Convidado.objects.aggregate(Sum('quantidade_convidados')).get('quantidade_convidados__sum', 0)
        return context


class ConvidadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Convidado
    success_url = reverse_lazy('convidado:convidado_list')


class ListaConvidadoList(LoginRequiredMixin, ListView):
    model = ListaConvidados
    context_object_name = 'lista_convidado_list'
    template_name = 'listaConvidado/listaconvidados_list.html'


class ListaConvidadoCreate(LoginRequiredMixin, CreateView):
    model = ListaConvidados
    template_name = 'listaConvidado/listaconvidados_form.html'
    fields = ('nome_convidado', 'quantidade_convidados', 'convidado_por', )
    success_url = reverse_lazy('convidado:lista_convidado_list')


# Convidados Confirma Presença
convidado_list = ConvidadoListView.as_view()
convidado_delete = ConvidadoDeleteView.as_view()
presenca_confirmada = PresencaConfirmadaView.as_view()

# Convidados lista feita pelos noivos
lista_convidado_create = ListaConvidadoCreate.as_view()
lista_convidado_list = ListaConvidadoList.as_view()