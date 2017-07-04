from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Convidado



class IndexView(CreateView):
    template_name = 'core/index.html'
    model = Convidado
    fields = ['nome_convidado', 'quantidade_convidados', ]


class ConvidadoList(LoginRequiredMixin, ListView):
    pass



index = IndexView.as_view()