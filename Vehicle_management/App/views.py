from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from .models import Vehicle


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('vehicle')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('vehicle')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('vehicle')
        return super(RegisterView, self).get(*args, **kwargs)


class VehicleList(LoginRequiredMixin, ListView):
    model = Vehicle
    context_object_name = 'vehicle'
    template_name = 'list.html'


class VehicleCreate(LoginRequiredMixin, CreateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('create')
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VehicleCreate, self).form_valid(form)


class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicle')
    template_name = 'create.html'


class VehicleDelete(LoginRequiredMixin, DeleteView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicle')
    template_name = 'delete.html'


class VehicleView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'details.html'