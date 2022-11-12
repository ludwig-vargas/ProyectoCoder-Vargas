from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import Product
from product.forms import ProductForm
# Create your views here.

class ProductListView(ListView):
    model = Product
    
#Detalles de Producto
class ProductDetailView(DetailView):
    model = Product
    fields = ['name','code_product','category','price','amount','description']
    
#Crear Producto
class ProductCreateView(CreateView):
    model = Product
    #Redirecciona a product_list.html
    success_url = reverse_lazy('product:product-list')
    
    form_class = ProductForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        actual_object = Product.objects.filter(
            name=data['name'],
            code_product=data['code_product'],
            category=data['category'],
            price=data['price'],
            amount=data['amount'],
            description=data['description'],
        ).count()
        if actual_object:
            messages.error(
                self.request,
                f"El producto {data['name']} - {data['code_product']} ya esta creado",
            )
            form.add_error('name_er', ValidationError('Accion no válida'))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"El producto {data['name']} - {data['code_product']} se creo exitosamente!",
            )
            return super().form_valid(form)

#Actualizar
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        product_id = self.kwargs["pk"]
        return reverse_lazy("product:product-detail", kwargs={"pk": product_id})

#Eliminar
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product-list')