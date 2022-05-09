from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContatoForm
from .models import Funcionario, Recurso, Servico


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    # em caso de sucesso com o email retorna para a index
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context =  super(IndexView, self).get_context_data(**kwargs)
        # order_by('?') ordea aleatorio
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        return context

    # se o formulario for valido
    def form_valid(self, form, *args, **kwargs):
        form.send_mail() # envia o email
        # envia a mensagem de sucesso
        messages.success(self.request, 'Email enviado com sucesso')
        # retorna o formulario
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # se o formulario for invalido
    def form_invalid(self, form, *args, **kwargs):
        # retorna uma mensagem de erro
        messages.error(self.request, 'Erro ao enviar email')
        # retorna o formulario
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

    


