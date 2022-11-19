from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from product.models import Product, Comment
from product.forms import ProductForm, CommentForm
# Create your views here.

class ProductListView(ListView):
    model = Product
    
#Detalles de Producto
class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    fields = ['name','code_product','category','price','amount','description']
    
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        comments = Comment.objects.filter(product=product).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "product": product,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)
    
#Crear Producto
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    #Redirecciona a product_list.html
    success_url = reverse_lazy('product:product-list')
    
    form_class = ProductForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.owner = self.request.user
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
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        product_id = self.kwargs["pk"]
        return reverse_lazy("product:product-detail", kwargs={"pk": product_id})

#Eliminar
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product:product-list')

#Crear comentario
class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, product=product
        )
        comment.save()
        return redirect(reverse("product:product-detail", kwargs={"pk":pk}))

#Eliminar comentario
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    
    def get_success_url(self):
        product = self.object.product
        return reverse("product:product-detail", kwargs={"pk":product.id})