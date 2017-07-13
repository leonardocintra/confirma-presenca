from datetime import date
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView
from convidado.models import Convidado



class ContatoView(TemplateView):
    template_name = 'core/contato.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class IndexView(CreateView):
    template_name = 'core/index.html'
    model = Convidado
    fields = ['nome_convidado', 'quantidade_convidados', ]
    success_url = reverse_lazy('presenca_confirmada')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data_casamento'] = date(2017, 10, 6)
        return context



index = IndexView.as_view()
contato = ContatoView.as_view()
about = AboutView.as_view()