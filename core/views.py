from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Convidado



class IndexView(SuccessMessageMixin, CreateView):
    template_name = 'core/index.html'
    model = Convidado
    fields = ['nome_convidado', 'quantidade_convidados', ]
    success_url = reverse_lazy('index')
    success_message = "Sua presença foi confirmada com sucesso! Muito obrigado!"


class ConvidadoList(LoginRequiredMixin, ListView):
    model = Convidado
    template_name = 'core/convidados_list.html'
    context_object_name = 'convidados_list'


index = IndexView.as_view()
convidado_list = ConvidadoList.as_view()