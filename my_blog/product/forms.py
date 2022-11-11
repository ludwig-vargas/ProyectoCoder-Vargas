from django import forms
from ckeditor.widgets import CKEditorWidget
from product.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del Producto:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'product-name',
                'placehikder':'Nombre del producto',
                'required':'True',
            }
        ),
    )
    
    code_product = forms.IntegerField(
        label='Codigo de Producto:',
        required=False,
        widget=forms.TimeInput(
            attrs={
                'class':'product-code',
                'placehikder':'Codigo del producto',
                'required':'True',
            }
        ),
    )
    
    category = forms.CharField(
        label='Categoria del Producto:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'product-category',
                'placehikder':'NCategoriaombre del producto',
                'required':'True',
            }
        ),
    )
    
    price = forms.IntegerField(
        label='Precio de Producto:',
        required=False,
        widget=forms.TimeInput(
            attrs={
                'class':'price-code',
                'placehikder':'Precio del producto',
                'required':'True',
            }
        ),
    )
    
    amount = forms.IntegerField(
        label='En existencia:',
        required=False,
        widget=forms.TimeInput(
            attrs={
                'class':'amount-code',
                'placehikder':'Cantidad del producto',
                'required':'True',
            }
        ),
    )
    
    description = forms.CharField(
        label='Descripcion:',
        required=False,
        widget=CKEditorWidget(
            attrs={
                'class':'product-description',
                'placehikder':'Descripcion del producto',
                'required':'True',
            }
        ),
    )
    
    class Meta:
        model = Product
        fields = ['name','code_product','category','price','amount','description']
    
    