from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import Product
from product.forms import ProductForm
# Create your views here.

class ProductListView(ListView):
    model = Product
    
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