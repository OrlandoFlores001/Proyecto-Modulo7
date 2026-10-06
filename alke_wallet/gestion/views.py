import random
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Cuenta, Transaccion
from .forms import ClienteForm

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        num_cuenta = f"AW-{random.randint(100000, 999999)}"
        
        Cuenta.objects.create(
            cliente=self.object,
            numero_cuenta=num_cuenta,
            saldo=0.00
        )
        
        return response

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


class ReporteTransaccionesView(LoginRequiredMixin, ListView):
    template_name = 'gestion/reporte.html'
    context_object_name = 'transacciones'

    def get_queryset(self):
        query = """
            SELECT t.id, t.tipo, t.monto, t.fecha, c.numero_cuenta 
            FROM gestion_transaccion t
            JOIN gestion_cuenta c ON t.cuenta_id = c.id
            ORDER BY t.fecha DESC
        """
        return Transaccion.objects.raw(query)