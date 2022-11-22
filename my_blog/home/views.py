from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.contrib import messages
from django.db.models import Q
from product.models import Product
from home.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

# Buscador
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = (Q(name=search_param) | Q(code_product=search_param))
        products = Product.objects.filter(query)
        context_dict.update(
            {
                "products": products,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )

# Registrar nuevo usuario
def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente")
            return redirect("login")
    
    return render(
        request=request,
        context={"form": form},
        template_name="registration/registration.html",
    )

# Modificar al usuario
@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect("home:index")
    
    form = UserUpdateForm(model_to_dict(user))
    return render(
        request=request,
        context={"form": form},
        template_name="registration/user_form.html",
    )

# Lista de Usuarios
@login_required
def user_list(request):
    users = User.objects.all()
    context_diac = {"users":users}

    return render(
        request=request,
        context=context_diac,
        template_name="registration/user_list.html",
    )
