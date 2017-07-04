from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'core/index.html'


index = IndexView.as_view()