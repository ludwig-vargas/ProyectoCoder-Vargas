from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from service.models import Service, CommentService
from service.forms import ServiceForm, CommentServiceForm
# Create your views here.

class ServiceListView(ListView):
    model = Service
    
# Detalles de Servicio
class ServiceDetailView(DetailView):
    model = Service
    template_name = "service/service_detail.html"
    fields = ['name','code_service','category','price','numberphone','email','description']
    
    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        comments = CommentService.objects.filter(service=service).order_by("-updated_at")
        comment_form = CommentServiceForm()
        context = {
            "service": service,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)
    
# Crear Servicio
class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    #Redirecciona a service_list.html
    success_url = reverse_lazy('service:service-list')
    
    form_class = ServiceForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_object = Service.objects.filter(
            name=data['name'],
            code_service=data['code_service'],
            category=data['category'],
            price=data['price'],
            numberphone=data['numberphone'],
            email=data['email'],
            description=data['description'],
        ).count()
        if actual_object:
            messages.error(
                self.request,
                f"El servicio {data['name']} - {data['code_service']} ya esta creado",
            )
            form.add_error('name_er', ValidationError('Accion no válida'))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"El servicio {data['name']} - {data['code_service']} se creo exitosamente!",
            )
            return super().form_valid(form)

#Actualizar
class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm

    def get_success_url(self):
        service_id = self.kwargs["pk"]
        return reverse_lazy("service:service-detail", kwargs={"pk": service_id})
        

#Eliminar
class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('service:service-list')

#Crear comentario
class CommentServiceCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        service = get_object_or_404(Service, id=pk)
        comment = CommentService(
            text=request.POST["comment_text"], owner=request.user, service=service
        )
        comment.save()
        return redirect(reverse("service:service-detail", kwargs={"pk":pk}))

#Eliminar comentario
class CommentServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = CommentService
    
    def get_success_url(self):
        service = self.object.service
        return reverse("service:service-detail", kwargs={"pk":service.id})