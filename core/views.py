from re import template

from django.views.generic import TemplateView

from .models import Funcionario, Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super(IndexView, self).get_context_data(**kwargs)
        # order_by('?') ordea aleatorio
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context


